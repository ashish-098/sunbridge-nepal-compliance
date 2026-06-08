def check_nepqa(pdf1_text, pdf2_text, nepqa_text):
    # Items Nepal import review typically needs
    required_items = [
        "model number",
        "manufacturer name",
        "rated power",
        "voltage",
        "efficiency",
        "certification",
        "test report",
        "label",
        "warranty"
    ]

    results = []

    for item in required_items:
        in_pdf1 = item.lower() in pdf1_text.lower()
        in_pdf2 = item.lower() in pdf2_text.lower()
        in_nepqa = item.lower() in nepqa_text.lower()

        status = "✅ Found" if (in_pdf1 or in_pdf2) else "❌ Missing"

        results.append({
            "item": item,
            "status": status,
            "in_pdf1": in_pdf1,
            "in_pdf2": in_pdf2,
            "nepal_requires": in_nepqa
        })

    return results