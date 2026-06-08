import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def generate_report(pdf1_text, pdf2_text, nepqa_text, comparison, nepqa_check):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are a compliance assistant helping SunBridge Trading, a Nepal importer.

They are importing grid-tied solar inverters from China into Nepal.
You have been given two manufacturer PDFs from China and the NEPQA 2025 Nepal import guideline.

Your job is to produce a clear, honest compliance draft that SunBridge can share with their Nepal import agent.

---

MANUFACTURER PDF 1 (China export document):
{pdf1_text[:3000]}

---

MANUFACTURER PDF 2 (China export document - possibly a different variant):
{pdf2_text[:3000]}

---

NEPAL IMPORT GUIDELINE (NEPQA 2025) - use as reference only:
{nepqa_text[:2000]}

---

COMPARISON FINDINGS:
- Fields found in both PDFs: {comparison['common']}
- Fields only in PDF 1: {comparison['pdf1_only']}
- Fields only in PDF 2: {comparison['pdf2_only']}

---

NEPQA CHECKLIST:
{nepqa_check}

---

Now produce a structured compliance draft with these sections:

1. PRODUCT OVERVIEW
   - Model name, type, intended use
   - Any variant differences between the two PDFs

2. MANUFACTURER INFORMATION
   - Company name, country, contact if available

3. TECHNICAL SPECIFICATIONS
   - Power, voltage, current, frequency, efficiency, weight, dimensions
   - Note any mismatches between the two PDFs honestly

4. TEST AND CERTIFICATION INFORMATION
   - Any test reports, certifications, lab names mentioned
   - Note if anything is missing or unclear

5. LABELING INFORMATION
   - What labeling details are present
   - What seems to be missing for Nepal import

6. MISMATCHES AND GAPS
   - Be honest about anything that does not match between the two PDFs
   - List anything that is unclear or missing

7. APPROACH NOTE
   - A short paragraph explaining how you analyzed these documents

Be honest. If something is missing, say so clearly. This is a working draft, not a final filing.
"""

    print("Calling Gemini API to generate report...")
    response = model.generate_content(prompt)
    return response.text


def save_report(report_text):
    os.makedirs("output", exist_ok=True)
    path = "output/sunbridge_nepal_compliance_draft.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(report_text)
    print(f"Report saved to {path}")
    return path