# 📘 ScholarSight  
### AI-Powered Research Paper Summarization System

---

## 🔍 Project Overview
ScholarSight is an end-to-end AI system that processes academic research papers and generates structured summaries.  
The system ingests research paper PDFs, extracts meaningful sections using heuristic NLP techniques, and produces concise academic summaries using large language models (LLMs), with a graceful fallback mechanism when external APIs are unavailable.

This project focuses on **system design, robustness, and explainability**, rather than black-box model usage.

---

## ✨ Features
- 📄 PDF text extraction from academic research papers  
- 🧠 Automatic section detection (Introduction, Methodology, etc.)  
- ✍️ AI-based structured summarization  
- 🔁 Graceful fallback when LLM APIs are unavailable  
- 🧩 Modular and extensible backend architecture  

---

## 🏗️ System Architecture

## 🛠️ Tech Stack
- **Language:** Python  
- **PDF Processing:** PyMuPDF (fitz)  
- **NLP:** Heuristic & regex-based section parsing  
- **AI:** OpenAI API (optional, with fallback summarization)  

## 📂 Project Structure
SCHOLARSIGHT/
├── backend/
│ ├── pdf_parser.py
│ ├── sectionizer.py
│ └── summarizer.py
│
├── data/
│ └── papers/
│ └── sample.pdf
│
└── README.md


## 🚀 How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt

Step-2
setx OPENAI_API_KEY "your_api_key_here"

Step-3
cd backend
python pdf_parser.py

Step-4
Example
TOTAL SECTIONS FOUND: 2
===== INTRODUCTION SUMMARY =====
[Fallback summary due to API quota]
This section discusses the importance of social connections and defines social anxiety as a psychological condition...

===== METHODOLOGY SUMMARY =====
[Fallback summary due to API quota]
The study systematically reviews peer-reviewed literature focusing on VR-based interventions...
