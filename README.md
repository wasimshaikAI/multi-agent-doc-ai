# 🧠 Multi-Agent AI System – Flowbit Challenge Submission

## 🚀 Overview  
An intelligent multi-agent system that processes unstructured documents (PDF, JSON, Email), automatically detects the format and intent, routes them to specialized agents, and shares context via a shared memory module.

## 📁 Folder Structure  
- `agents/` – Specialized agents for PDF, JSON, and Email  
- `memory/` – Shared memory module  
- `router/` – Format & intent classification logic  
- `sample_inputs/` – Sample input files for testing  
- `output_logs/` – Sample output logs and screenshots  

## 🎥 Demo Video  
▶️ [Click to Watch the Demo](https://github.com/wasimshaikAI/multi-agent-doc-ai/raw/refs/heads/main/live-demo.mp4)

## 🖼️ Output Screenshots  
View screenshots of the system in action:  
📸 [Output Screenshots Folder](https://github.com/wasimshaikAI/multi-agent-doc-ai/tree/main/multi_agent_system/output%20ss)

## 📦 How to Run
```bash
git clone https://github.com/wasimshaikAI/multi-agent-doc-ai.git
cd multi-agent-doc-ai
pip install -r requirements.txt
python main.py --input sample_inputs/sample.json
