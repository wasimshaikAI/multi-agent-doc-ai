from agents.classifier_agent import detect_format, extract_text, detect_intent
from agents.json_agent import process_json
from agents.email_agent import process_email
from agents.pdf_agent import process_pdf
from memory.memory_store import log_to_memory


def orchestrator(file_path):
    print(f"\n\ud83d\udcdd Processing: {file_path}")
    file_format = detect_format(file_path)
    text = extract_text(file_path)
    intent = detect_intent(text)

    extracted = None
    if file_format == "JSON":
        extracted, missing = process_json(file_path)
        if missing:
            print(f"\u26a0\ufe0f Missing in JSON: {missing}")
    elif file_format == "Email":
        extracted = process_email(text)
    elif file_format == "PDF":
        extracted, missing = process_pdf(file_path)
        if missing:
            print(f"\u26a0\ufe0f Missing in PDF: {missing}")
    else:
        print("\u274c Unsupported format.")
        return

    log_to_memory(file_path, file_format, intent, extracted)
    print("\u2705 Extracted Data:", extracted)
