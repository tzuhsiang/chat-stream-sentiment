from kafka import KafkaConsumer, KafkaProducer
from textblob import TextBlob
import json

consumer = KafkaConsumer(
    'chat-messages',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='sentiment-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for msg in consumer:
    text = msg.value['text']
    sentiment = TextBlob(text).sentiment.polarity
    result = {
        "user": msg.value['user'],
        "text": text,
        "sentiment": sentiment,
        "timestamp": msg.value['timestamp']
    }
    print(f"分析結果：{result}")
    producer.send('chat-sentiment', result)
