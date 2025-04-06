import streamlit as st
import json
from kafka import KafkaConsumer

st.title("📊 即時客服情緒分析")

consumer = KafkaConsumer(
    'chat-sentiment',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    group_id='dashboard',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

st.write("等待 Kafka 訊息中...")

for msg in consumer:
    data = msg.value
    sentiment = data["sentiment"]
    st.markdown(f"**{data['user']}**: {data['text']}")
    st.progress((sentiment + 1) / 2)  # 轉成 0~1
