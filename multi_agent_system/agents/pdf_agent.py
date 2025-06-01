import fitz  # PyMuPDF
import re

def process_pdf(file_path):
    try:
        # Load PDF and extract full text
        with fitz.open(file_path) as doc:
            text = ' '.join(page.get_text().strip() for page in doc)

        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)

        # Extract fields using flexible patterns
        invoice_number = re.search(r'Invoice\s*Number[:\-]?\s*(\S+)', text, re.IGNORECASE)
        date = re.search(r'Date[:\-]?\s*([\d]{2,4}[-/][\d]{1,2}[-/][\d]{1,4})', text, re.IGNORECASE)
        customer_name = re.search(r'Customer\s*Name[:\-]?\s*(.*?)(?=\s+\w+:)', text, re.IGNORECASE)
        total_amount = re.search(r'Total\s*Amount[:\-]?\s*\$?\s*([\d,]+\.\d{2})', text, re.IGNORECASE)

        extracted = {
            "invoice_number": invoice_number.group(1) if invoice_number else None,
            "date": date.group(1) if date else None,
            "customer_name": customer_name.group(1).strip() if customer_name else None,
            "total_amount": total_amount.group(1).replace(',', '') if total_amount else None
        }

        missing = [k for k, v in extracted.items() if v is None]

        return extracted, missing

    except Exception as e:
        print(f"❌ Error processing PDF: {e}")
        return {}, ["error"]
