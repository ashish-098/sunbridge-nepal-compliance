def compare_pdfs(pdf1_text, pdf2_text):
    findings = {
        "pdf1_only": [],
        "pdf2_only": [],
        "mismatches": [],
        "common": []
    }

    # Key technical terms to look for
    keywords = [
        "model", "power", "voltage", "current", "frequency",
        "efficiency", "weight", "dimension", "certification",
        "warranty", "protection", "temperature", "humidity"
    ]

    for keyword in keywords:
        in_pdf1 = keyword.lower() in pdf1_text.lower()
        in_pdf2 = keyword.lower() in pdf2_text.lower()

        if in_pdf1 and in_pdf2:
            findings["common"].append(keyword)
        elif in_pdf1:
            findings["pdf1_only"].append(keyword)
        elif in_pdf2:
            findings["pdf2_only"].append(keyword)

    return findings