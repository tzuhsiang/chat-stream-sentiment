# Chat Stream Sentiment Analysis

用 Kafka 架設的即時客服訊息情緒分析系統。

## 架構簡介

- 🧾 Producer: 模擬聊天訊息 (Python)
- 🧠 Consumer: 進行情緒分析（TextBlob）
- 📦 Kafka Topic: chat-messages → chat-sentiment
- 📊 Dashboard: 用 Streamlit 顯示分析結果

## 如何啟動

### 1. 啟動 Kafka 系統
```bash
docker compose up -d
```

### 2. 安裝 Python 套件
```bash
pip install -r requirements.txt
```

### 3. 執行模擬聊天產生器
```bash
python producer/simulate_chat.py
```

### 4. 執行情緒分析器
```bash
python consumer/sentiment_analyzer.py
```

### 5. 啟動儀表板（可選）
```bash
streamlit run dashboard/app.py
```
