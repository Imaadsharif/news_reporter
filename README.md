---

# 📰 Multi-Agent News Generator

An AI-powered web application that generates structured news articles using a **multi-agent architecture**. Built with **Flask + Azure OpenAI**, this project simulates a real-world enterprise AI pipeline.

---

## 📌 Overview

This system transforms a user-provided topic into a complete news article through a sequence of specialized AI agents:

```
User Input → Research Agent → Summarizer Agent → Writer Agent → Final Output
```

Each agent performs a distinct role, making the system modular, scalable, and easy to extend.

---

## 🚀 Features

* 🔍 **Research Agent**
  Collects detailed and relevant information on the given topic

* 📌 **Summarizer Agent**
  Extracts key insights and condenses the content

* 📰 **Writer Agent**
  Produces a structured and readable news article

* ✅ **Validation Layer**
  Ensures output quality and consistency

* 🌐 **Flask Web Interface**
  Simple and interactive user experience

* 🎨 **Modern UI**
  Clean design with gradient styling

* 🧠 **Markdown Rendering**
  Converts AI responses into formatted HTML

* ⏳ **Loading Animation**
  Enhances user experience during processing

---

## 🏗️ Architecture

```
            ┌──────────────┐
            │   User Input │
            └──────┬───────┘
                   ↓
        ┌────────────────────┐
        │  Research Agent    │
        └────────┬───────────┘
                 ↓
        ┌────────────────────┐
        │ Summarizer Agent   │
        └────────┬───────────┘
                 ↓
        ┌────────────────────┐
        │   Writer Agent     │
        └────────┬───────────┘
                 ↓
        ┌────────────────────┐
        │   Final Output     │
        └────────────────────┘
```

---

## 🛠️ Tech Stack

* 🐍 Python
* 🌐 Flask
* ☁️ Azure OpenAI
* 🎨 HTML + CSS
* 🧠 Markdown

---

## 📁 Project Structure

```
news_agent_pro/
│
├── src/
│   ├── agents/          # Research, Summarizer, Writer agents
│   ├── validators/      # Output validation logic
│   ├── orchestrator.py  # Pipeline controller
│
├── web/
│   ├── app.py           # Flask application
│   ├── templates/       # HTML templates
│   ├── static/          # CSS files
│
├── .env                 # Environment variables
├── requirements.txt     # Dependencies
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd news_agent_pro
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

**Activate:**

* Windows:

  ```bash
  .venv\Scripts\activate
  ```
* Mac/Linux:

  ```bash
  source .venv/bin/activate
  ```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_KEY=your_key
AZURE_OPENAI_DEPLOYMENT=your_deployment
```

---

### 5️⃣ Run the Application

```bash
python web/app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Usage

1. Enter a topic (e.g., *AI in Healthcare*)
2. Click **Generate**
3. Wait for processing ⏳
4. View:

   * 🔍 Research Output
   * 📌 Summary
   * 📰 Final Article

---

## 🧠 Key Learnings

* Multi-agent system design
* LLM orchestration
* Prompt engineering
* Validation pipelines
* Full-stack integration (Flask + frontend)

---

## 🎯 Outcome

This project demonstrates:

* ✅ Agent-based architecture
* ✅ Structured content generation
* ✅ Scalable AI pipeline design
* ✅ Real-world AI workflow simulation

---

## 🚀 Future Improvements

* ⚡ Real-time streaming responses
* 🌙 Dark mode UI
* 📋 Copy-to-clipboard
* 📊 Export (PDF / DOCX)
* 🔎 Web search integration

---

## 🤝 Contributing

Contributions are welcome! Fork the repository and submit a pull request.

---

## 📄 License

Licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

---
