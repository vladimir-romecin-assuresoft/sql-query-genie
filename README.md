# 🧠 SQL Query Genie

> Convert natural language into executable SQL queries using AI — with self-healing and explainability.

---

## 🚀 Overview

**SQL Query Genie** is an AI-powered web application that transforms plain English queries into SQL, executes them against a database, and explains the reasoning behind the generated query.

This project demonstrates:

* LLM orchestration
* Prompt engineering
* Self-healing systems
* Full-stack AI integration

---

## ✨ Features

* 🔤 Natural Language → SQL conversion
* ⚡ Real-time query execution (SQLite)
* 🔁 Self-healing loop for failed queries
* 🧠 AI-powered reasoning
* 🌐 Interactive UI with Streamlit
* 📊 Ready for analytics extension

---

## 🏗️ Architecture

```
User Input (Natural Language)
        ↓
   Streamlit UI
        ↓
   SQL Generator (LLM)
        ↓
   SQLite Execution
        ↓
   Error?
     ↳ Yes → Self-Healing Loop → Retry
        ↓
     Results Display
```

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Database:** SQLite
* **LLM:** OpenAI API
* **Orchestration:** LangChain (optional extension)

---

## 📁 Project Structure

```
sql-query-genie/
│
├── main.py                  # Streamlit app
├── requirements.txt
├── .env
├── README.md
│
├── database/
│   ├── schema.sql           # Database schema (DDL)
│   └── init_db.py           # DB initialization script
│
├── llm/
│   ├── sql_generator.py     # LLM SQL generation
│   └── self_healing.py      # Query correction loop
│
└── utils/
    └── db.py               # Database connection + execution
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/sql-query-genie.git
cd sql-query-genie
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 4. Initialize the database

```bash
python database/init_db.py
```

---

### 5. Run the app

```bash
streamlit run main.py
```

---

## 🧪 Example Queries

Try inputs like:

```
Show all customers
```

```
Top 5 customers who spent the most last month
```

```
Total revenue grouped by customer
```

---

## 🧠 Prompt Engineering Strategy

The system uses structured prompts that include:

* Database schema (context injection)
* User request
* Strict instruction to return SQL only

### Example Prompt

```
You are an expert SQL generator.

Database schema:
[SCHEMA]

User request:
[USER INPUT]

Return ONLY the SQL query.
```

---

## 🔁 Self-Healing Mechanism

If a query fails:

1. Capture SQL error
2. Send error + query back to LLM
3. Regenerate corrected SQL
4. Retry execution

This creates a **feedback loop** that significantly improves reliability.

---

## 📊 Future Improvements

* ✅ SQL explanation (chain-of-thought UI)
* 📈 Data visualization (Chart.js / Plotly)
* 🧾 Query history tracking
* 🔐 Authentication layer
* 🌍 Multi-database support (PostgreSQL, MySQL)
* 🧠 Fine-tuned models for SQL

---

## 🎯 Use Cases

* Data analysts without SQL knowledge
* Business intelligence tools
* AI-assisted dashboards
* Educational SQL tools

---

## ⚠️ Limitations

* Dependent on LLM accuracy
* Requires well-defined schema
* May generate inefficient queries (no optimization layer yet)

---

## 📌 Deliverables

* ✅ Source code (GitHub repo)
* ✅ Working application (local or deployed)
* ✅ Documented architecture & prompts

---

## 👨‍💻 Author

Built as part of an AI engineering training project focused on:

* LLM systems design
* AI-assisted development
* Practical GenAI applications

---

## 📝 License

MIT License — free to use and modify.

---

## ⭐ Final Thoughts

This project showcases how AI can bridge the gap between human language and structured data systems, enabling a new class of intelligent interfaces.

---

**If you found this useful, consider starring the repo ⭐**
