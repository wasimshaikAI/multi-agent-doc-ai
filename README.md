# 🧠 Multi-Agent AI System – Flowbit Challenge Submission

## 🚀 Overview  
An intelligent multi-agent system that processes unstructured documents like PDF, JSON, and Email. It automatically detects the document format and its intent, routes the data to a specialized agent for processing, and maintains a shared memory for context retention.

---

## 📁 Folder Structure  
- `agents/` – Specialized agents for PDF, JSON, and Email  
- `memory/` – Shared memory module to store extracted values and metadata  
- `router/` – Handles format and intent classification  
- `sample_inputs/` – Contains sample files in JSON, PDF, and Email formats  
- `output_logs/` – Contains screenshots and logs of system output  
- `main.py` – The main script to run the system  
- `requirements.txt` – All Python dependencies  
- `README.md` – Project documentation  
- `live-demo.mp4` – Demo video (under 118 MB)

---

## 🎥 Demo Video  
▶️ [Click to Watch the Demo](https://github.com/wasimshaikAI/multi-agent-doc-ai/raw/refs/heads/main/live-demo.mp4)

---

## 🖼️ Output Screenshots  
Screenshots of the system output are available here:  
📸 [Output Screenshots Folder](https://github.com/wasimshaikAI/multi-agent-doc-ai/tree/main/multi_agent_system/output%20ss)

---

## 📦 How to Run

```bash
git clone https://github.com/wasimshaikAI/multi-agent-doc-ai.git
cd multi-agent-doc-ai
pip install -r requirements.txt
python main.py --input sample_inputs/sample.json
