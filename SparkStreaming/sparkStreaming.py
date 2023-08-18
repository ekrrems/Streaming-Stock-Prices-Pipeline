from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, LongType, FloatType
import psycopg2
import json
from utils.connectPostgre import write_to_database


# Create a Spark session
spark = SparkSession.builder \
    .appName("KafkaToSparkStreaming") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0") \
    .getOrCreate()

# Read streaming data 
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "finnhub-topic") \
    .load()

# Create schema for the data
schema = StructType([
    StructField("data", ArrayType(StructType([
        StructField("c", ArrayType(StringType())),
        StructField("p", StringType()),
        StructField("s", StringType()),
        StructField("t", StringType()),
        StructField("v", StringType())
    ]))),
    StructField("type", StringType())
])

# Parse streaming data
df = df.selectExpr("CAST(value AS STRING)")
parsed = df.select(F.from_json(F.col("value"), schema).alias("value"))\
    .select(F.col("value.*")).select("data")

# Create a new dataframe 
exploded_df = parsed.selectExpr("explode(data) as exploded_data")

parsed_data = exploded_df.select(
    "exploded_data.c",
    "exploded_data.p",
    "exploded_data.s",
    "exploded_data.t",
    "exploded_data.v"
)

# Write streaming data
console_query = parsed_data.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Add streaming data to PostgreSQL database
database_query = parsed_data.writeStream \
    .outputMode("append") \
    .foreachBatch(write_to_database) \
    .start()

console_query.awaitTermination()

# Stop the Spark session
spark.stop()