import pdfplumber

def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_all(pdf1_path, pdf2_path, nepqa_path):
    print("Reading Manufacturer PDF 1...")
    pdf1 = extract_text(pdf1_path)

    print("Reading Manufacturer PDF 2...")
    pdf2 = extract_text(pdf2_path)

    print("Reading NEPQA 2025...")
    nepqa = extract_text(nepqa_path)

    return pdf1, pdf2, nepqa