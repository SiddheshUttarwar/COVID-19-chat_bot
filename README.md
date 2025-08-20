# COVID-19 Chatbot 🤖🦠

An AI-powered chatbot that provides **real-time COVID-19 information**, safety guidelines, and FAQs.  
Built with **Python, Flask, and NLP** to assist users with reliable COVID-19-related queries.  

---

## 📌 Features
- 🧾 **COVID-19 FAQs** – Get answers to common COVID-related questions.  
- 🌍 **Latest Case Updates** – Fetches real-time COVID-19 statistics.  
- 🤝 **User-Friendly Interface** – Simple chatbot-like interaction.  
- ⚡ **Lightweight Backend** – Powered by Flask and Python.  
- 🧠 **Extensible** – Can be integrated with APIs like WHO or local government data.  

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **NLP:** Python-based NLP libraries  
- **APIs:** COVID-19 data APIs (for real-time case numbers)  

---

## 🚀 Getting Started

Follow these steps to set up the chatbot locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SiddheshUttarwar/COVID-19-chat_bot.git
cd COVID-19-chat_bot
```
### 2️⃣ Create a Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
###3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Run the Flask App
```bash
python app.py
```

## 📖 How It Works
1. User enters a query about COVID-19.
2. The chatbot processes the input using NLP techniques.
3. If it matches FAQs → returns predefined answers.
4. If it’s a data request → fetches live data via COVID-19 API.
5. Response is displayed back in a friendly chatbot format.

