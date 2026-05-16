import pdfplumber


def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

    return text


pdf_file = "uploads/sample_report.pdf"

text = extract_text(pdf_file)

print("Extracted Text:")
print(text)