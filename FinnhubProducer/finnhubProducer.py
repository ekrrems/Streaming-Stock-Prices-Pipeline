import os 
from dotenv import load_dotenv
from confluent_kafka import Producer
import json
import finnhub
import websocket


class ApiDataProducer:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("FINNHUB_API_KEY")

        bootstrap_servers = 'localhost:9092'
        producer_config = {
            'bootstrap.servers': bootstrap_servers
        }

        self.producer = Producer(producer_config)

        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={self.api_key}",
                                    on_message = self.on_message,
                                    on_error = self.on_error,
                                    on_close = self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()

        # Setup client
    def on_message(self, ws, message):
        #message = json.loads(message)
        self.send_kafka_topic(message)
        #print(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def on_open(self, ws):
        ws.send('{"type":"subscribe","symbol":"AAPL"}')
        ws.send('{"type":"subscribe","symbol":"AMZN"}')
        ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
        ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')

    def send_kafka_topic(self, message):
        topic = "finnhub-topic"
        self.producer.produce(topic, value=message)
        self.producer.flush()


if __name__ == "__main__":
    ApiDataProducer()