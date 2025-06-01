import re
from agents.classifier_agent import detect_intent  # ✅ Fix: import this

def process_email(email_text):
    sender = re.search(r'From:\s*(.*)', email_text)
    sender = sender.group(1).strip() if sender else "Unknown"
    urgency = any(word in email_text.lower() for word in ["urgent", "asap", "immediately", "at the earliest"])
    intent = detect_intent(email_text)
    return {
        "sender": sender,
        "urgency": urgency,
        "intent": intent
    }
