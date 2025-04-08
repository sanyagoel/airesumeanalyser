# 🤖 AI Recruiter Agency

An end-to-end intelligent recruitment assistant that automates resume parsing, job matching, screening, and personalized recommendations using a swarm of AI agents. This system simulates a real-world recruiting agency — from analyzing candidate profiles to providing clear recommendations for hiring success.

---

## 🧠 Core Features

- **Resume Extraction**  
  Extracts detailed candidate information like skills, experience, education, and achievements from PDFs using LangChain's community loader.

- **Profile Analysis**  
  Breaks down strengths, weaknesses, and improvement areas based on extracted data.

- **Job Matching**  
  Compares candidate profiles with available job descriptions and calculates a match score.

- **Candidate Screening**  
  Evaluates qualifications, experience, skill alignment, red flags (like long employment gaps), and cultural fit.

- **Final Recommendations**  
  Provides personalized suggestions and next steps to enhance resume and job readiness.

---

## 🛠️ Tech Stack

- **Python**
- **Swarm Framework** for agent creation and orchestration
- **LangChain** (with **community loader** for PDF parsing)
- **Ollama** (using **locally downloaded LLaMA model** instead of OpenAI)
- **Modular Agent System** (`baseAgent`, `orchestrator`, etc.)

---

## 📁 Project Structure
AI-Recruiter/ │
├── Agents/ 
│ ├── baseagent.py
│ ├── extractorAgent.py
│ ├── analysisAgent.py
│ ├── matcherAgent.py
│ ├── screenerAgent.py
│ └── recommendationAgent.py
│── pdfs/ 
│ └── Jane_Smith_Resume.pdf 
├── .env
├── .gitignore 
├── requirements.txt
└── app.py


---

## ✨ Highlights

- Built using the **Swarm Framework** to modularize agents with distinct responsibilities.
- Replaced the OpenAI API key with a **locally downloaded LLaMA model** using Ollama for full offline AI capabilities.
- Used **LangChain’s community loader** for extracting structured data from PDF resumes.
- Agents work in sequence: `extractor → analyzer → matcher → screener → recommender`.

---

## 🔮 Future Improvements

- Add UI layer for uploading resumes and viewing reports visually.
- Add more context-aware reasoning for red flag detection.
- Fine-tune LLaMA model on HR-specific datasets for improved outputs.

---

## 🧪 How to Run the Project

1. **Install Python 3.10.15**  
   (Important: Other versions may cause issues with `onnx` dependencies.)

2. **Set up a virtual environment**
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

