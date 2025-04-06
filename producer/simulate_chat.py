from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

messages = [
    "我覺得這產品真的很棒！",
    "客服好爛，我要投訴",
    "還可以接受啦",
    "超快回覆，推推～",
    "這是什麼垃圾服務？"
]

while True:
    message = {
        "user": f"user{random.randint(1,10)}",
        "text": random.choice(messages),
        "timestamp": time.time()
    }
    producer.send('chat-messages', message)
    print(f"Sent: {message}")
    time.sleep(1)
