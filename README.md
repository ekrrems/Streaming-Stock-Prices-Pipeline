![Alt Text](https://springflee.files.wordpress.com/2020/03/new-project.png?w=1230)
# Streaming Stock Prices Pipeline
This project demonstrates the process of creating a real-time data pipeline for processing stock prices data using Apache Kafka, Apache Spark Streaming, PostgreSQL, and Power BI. The project uses the Finnhub API to fetch financial data, processes it using Spark Streaming, stores the data in a PostgreSQL database, and visualizes it using Power BI.

## Overview
This project showcases the end-to-end process of creating a real-time data processing and visualization pipeline:
1. <b>Data Collection:</b> Fetch financial data using the Finnhub API.
2. <b>Streaming Processing:</b> Use Apache Kafka and Spark Streaming to process and transform the incoming data in real-time.
3. <b>Data Storage:</b> Store the processed data in a PostgreSQL database.
4. <b>Data Visualization:</b> Visualize the stored data using Power BI for real-time insights and analytics.

## Prerequisites
Before you begin, ensure you have the following software and tools installed:
* <b>Apache Kafka</b> - Version 2.12
* <b>Apache Spark</b> - Version 3.4.0
* <b>PostgreSQL</b> - Version 14.9
* <b>Power BI Desktop</b>
* <b>Python</b> - Version 3.10
* <b>Git</b> (for version control)

## Setup
1. Clone this repository to your local machine:
```
git clone https://github.com/ekrrems/Streaming-Stock-Prices-Pipeline.git
```
2. Set up your Finnhub API credentials and other configuration settings in the appropriate files
3. Configure Apache Kafka, Spark Streaming, PostgreSQL, and Power BI based on your environment.
 

## Usage
1. Run the Finnhub producer script to fetch data from the Finnhub API and send it to the Kafka topic.

2. Configure the PostgreSQL database and run the appropriate SQL scripts to set up the database schema. (You can find the required schema on the console of spark streaming script)

3. Start the Spark Streaming application to process the streaming data from Kafka. 

3. Use Power BI Desktop to connect to the PostgreSQL database and create real-time visualizations.

4. Run your Spark Streaming script before running Finnhub Producer script

## Contribution
Contributions are welcome! If you have suggestions, improvements, or bug fixes, please create a pull request.

## Licence
This project is licensed under the MIT License.

  
