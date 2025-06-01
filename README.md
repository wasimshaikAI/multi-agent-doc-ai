# 🧠 Multi-Agent AI System – Flowbit Challenge Submission

## 🚀 Overview  
An intelligent multi-agent system that processes unstructured documents (PDF, JSON, Email), automatically detects the format and intent, routes them to specialized agents, and shares context via a shared memory module.

## 📁 Folder Structure  
multi-agent-doc-ai/
├── agents/
│ ├── pdf_agent.py # Handles PDF inputs and extraction
│ ├── json_agent.py # Handles structured JSON validation
│ └── email_agent.py # Processes email content
├── memory/
│ └── shared_memory.py # Lightweight shared memory module
├── router/
│ └── intent_router.py # Classifies format and intent
├── sample_inputs/
│ ├── sample.json # Example structured JSON input
│ ├── sample.pdf # Sample PDF for testing
│ └── sample_email.txt # Raw email text format
├── output_logs/
│ ├── run_log.txt # Output logs after processing
│ └── screenshot.png # Output screenshot
├── main.py # Main execution script
├── requirements.txt # List of Python dependencies
├── README.md # Project documentation (this file)
└── live-demo.mp4 # (Optional) Video demo under 118 MB
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
