import json
import fitz


def detect_format(file_path):
    if file_path.endswith(".json"):
        return "JSON"
    elif file_path.endswith(".pdf"):
        return "PDF"
    elif file_path.endswith(".txt"):
        return "Email"
    return "Unknown"


def extract_text(file_path):
    if file_path.endswith(".json"):
        with open(file_path, 'r') as f:
            return json.dumps(json.load(f))
    elif file_path.endswith(".pdf"):
        doc = fitz.open(file_path)
        return ''.join([page.get_text() for page in doc])
    elif file_path.endswith(".txt"):
        with open(file_path, 'r') as f:
            return f.read()
    return ""


def detect_intent(text):
    text_lower = text.lower()
    if "invoice" in text_lower:
        return "Invoice"
    elif "rfq" in text_lower or "quotation" in text_lower:
        return "RFQ"
    elif "complaint" in text_lower:
        return "Complaint"
    elif "regulation" in text_lower or "compliance" in text_lower:
        return "Regulation"
    return "General"
