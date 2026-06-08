import os
from src.extract import extract_all
from src.compare import compare_pdfs
from src.nepqa_check import check_nepqa
from src.generate_report import generate_report, save_report

def main():
    print("=" * 50)
    print("SunBridge Nepal Compliance Tool")
    print("=" * 50)

    # File paths
    PDF1_PATH = "data/manufacturer_pdf1.pdf"
    PDF2_PATH = "data/manufacturer_pdf2.pdf"
    NEPQA_PATH = "data/nepqa_2025.pdf"

    # Check all files exist
    for path in [PDF1_PATH, PDF2_PATH, NEPQA_PATH]:
        if not os.path.exists(path):
            print(f"ERROR: File not found -> {path}")
            print("Make sure all PDFs are inside the data/ folder")
            return

    # Step 1 - Extract text from all PDFs
    print("\nStep 1: Extracting text from PDFs...")
    pdf1_text, pdf2_text, nepqa_text = extract_all(PDF1_PATH, PDF2_PATH, NEPQA_PATH)
    print("Extraction complete!")

    # Step 2 - Compare the two manufacturer PDFs
    print("\nStep 2: Comparing the two manufacturer PDFs...")
    comparison = compare_pdfs(pdf1_text, pdf2_text)
    print(f"Common fields found: {comparison['common']}")
    print(f"Only in PDF1: {comparison['pdf1_only']}")
    print(f"Only in PDF2: {comparison['pdf2_only']}")

    # Step 3 - Check against NEPQA requirements
    print("\nStep 3: Checking against NEPQA 2025 requirements...")
    nepqa_results = check_nepqa(pdf1_text, pdf2_text, nepqa_text)
    for item in nepqa_results:
        print(f"  {item['status']} - {item['item']}")

    # Step 4 - Generate report using Claude API
    print("\nStep 4: Generating compliance draft with Claude AI...")
    report = generate_report(pdf1_text, pdf2_text, nepqa_text, comparison, nepqa_results)

    # Step 5 - Save the report
    print("\nStep 5: Saving report...")
    path = save_report(report)

    print("\n" + "=" * 50)
    print("DONE! Your compliance draft is ready.")
    print(f"Find it here: {path}")
    print("=" * 50)

if __name__ == "__main__":
    main()