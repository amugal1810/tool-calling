
# 🧠 OpenFDA Drug Recall Assistant (OpenAI Function Calling Version)

This project implements an AI assistant that answers questions about **FDA drug recalls** using:

- **Live OpenFDA Drug Enforcement API**
- **OpenAI Function Calling (tools)**
- **FastAPI backend**
- **Simple browser UI**

This version uses **OpenAI’s official API** (gpt‑4.1, gpt‑4.1‑mini, gpt‑o1, etc.)

---

# 🚀 Features

- Natural‑language Q&A about drug recalls  
- Searches real data from **OpenFDA Drug Enforcement API**  
- Two OpenAI tools:  
  - `search_recalls` — search recalls by keyword/classification  
  - `get_recall_stats` — aggregated statistics  
- End‑to‑end tool calling workflow  
- Clean FastAPI backend  
- Minimal web frontend  

---

# 📁 Project Structure

```
.
├── main.py                # FastAPI backend + OpenAI tool calling
├── tools.py               # Tool implementations
├── function_schemas.py    # Tool schemas for OpenAI
├── openfda/
│   ├── client.py          # OpenFDA fetch logic
│   └── transforms.py      # Data normalization
├── web/
│   ├── index.html         # Simple UI
│   └── app.js             # Frontend logic
├── requirements.txt
└── README_OPENAI.md
```

---

# 🔑 Requirements

- Python 3.10+
- OpenAI API key  
  Add to `.env`:

```
OPENAI_API_KEY=your_key_here
```

---

# ⚙️ Backend Setup

### 1. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key  
Create `.env`:

```
OPENAI_API_KEY=your_key_here
```

### 4. Run backend

```bash
uvicorn main:app --reload --port 8000
```

Backend runs at:

```
http://localhost:8000
```

---

# 🌐 Frontend Setup

```bash
cd web
python3 -m http.server 3000
```

Open browser:

```
http://localhost:3000
```

---

# 🛠 How Function Calling Works

### Step 1 — User asks:  
> “Show Class II ibuprofen recalls”

### Step 2 — OpenAI decides to call a tool  
Example:

```json
{
  "name": "search_recalls",
  "arguments": {
    "query": "ibuprofen",
    "classification": "Class II",
    "limit": 10
  }
}
```

### Step 3 — Backend executes tool  
Pulls data from OpenFDA.

### Step 4 — Result is passed back to model  
Model returns natural language summary.

### Step 5 — UI displays final result.

---

# 🧩 Tools

### 🔍 `search_recalls(query, classification, limit)`
Fetches recall list from OpenFDA, the tool calling function for search is made as specific as possible, the agent can search using the following params:
    query,
    classification,
    state,
    firm,
    status,

### 📊 `get_recall_stats()`
Returns:
- total recalls  
- by classification  
- by firm  
- by year  
- by state
---

# 🧪 Example Queries

- "Which states had the most recalls in 2022?"
- “Find recent ibuprofen recalls”  
- “Which firms had the most recalls in 2020?”  
- “How many Class I recalls in 2021?”  
- “Give recall stats by year”  


