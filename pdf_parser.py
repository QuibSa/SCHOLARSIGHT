import fitz  # PyMuPDF

from sectionizer import extract_sections
from summarizer import summarize_sections


def extract_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = []
    for page in doc:
        text.append(page.get_text())
    return "\n".join(text)


if __name__ == "__main__":
    print("PDF_PARSER FILE IS RUNNING")

    pdf_path = "../data/papers/sample.pdf"
    text = extract_text_from_pdf(pdf_path)

    sections = extract_sections(text)
    print(f"\nTOTAL SECTIONS FOUND: {len(sections)}")

    # 🔥 AI SUMMARIZATION STEP
    summaries = summarize_sections(sections)

    for section, summary in summaries.items():
        print(f"\n===== {section.upper()} SUMMARY =====")
        print(summary)
