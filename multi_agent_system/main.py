import os
from tkinter import Tk, filedialog
from orchestrator import orchestrator

def select_file():
    # Hide the root Tk window
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)  # Bring dialog to front

    file_path = filedialog.askopenfilename(
        initialdir="sample_inputs",
        title="Select a file to process",
        filetypes=(
            ("All files", "*.*"),
            ("Text files", "*.txt"),
            ("PDF files", "*.pdf"),
            ("JSON files", "*.json"),
        ),
    )
    return file_path

if __name__ == "__main__":
    file_path = select_file()
    if file_path:
        print(f"\n📝 Processing: {file_path}")
        orchestrator(file_path)
    else:
        print("❌ No file selected.")
