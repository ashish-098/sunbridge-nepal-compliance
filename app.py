import streamlit as st
import os
from src.extract import extract_all
from src.compare import compare_pdfs
from src.nepqa_check import check_nepqa
from src.generate_report import generate_report, save_report

st.set_page_config(
    page_title="SunBridge Nepal Compliance Tool",
    page_icon="☀️",
    layout="wide"
)

st.title("☀️ SunBridge Trading")
st.subheader("Nepal Import Compliance Tool — Grid-tied Solar Inverters")
st.markdown("---")

st.sidebar.header("📁 Upload Documents")

pdf1 = st.sidebar.file_uploader("Manufacturer PDF 1", type="pdf")
pdf2 = st.sidebar.file_uploader("Manufacturer PDF 2", type="pdf")
nepqa = st.sidebar.file_uploader("NEPQA 2025 Guideline", type="pdf")

if st.sidebar.button("🚀 Generate Compliance Draft", type="primary"):
    if not pdf1 or not pdf2 or not nepqa:
        st.error("Please upload all 3 PDF files first!")
    else:
        # Save uploaded files temporarily
        os.makedirs("temp", exist_ok=True)
        
        with open("temp/pdf1.pdf", "wb") as f:
            f.write(pdf1.read())
        with open("temp/pdf2.pdf", "wb") as f:
            f.write(pdf2.read())
        with open("temp/nepqa.pdf", "wb") as f:
            f.write(nepqa.read())

        with st.spinner("Step 1: Extracting text from PDFs..."):
            pdf1_text, pdf2_text, nepqa_text = extract_all(
                "temp/pdf1.pdf", "temp/pdf2.pdf", "temp/nepqa.pdf"
            )
        st.success("✅ Text extracted!")

        with st.spinner("Step 2: Comparing manufacturer PDFs..."):
            comparison = compare_pdfs(pdf1_text, pdf2_text)

        st.success("✅ Comparison done!")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Common Fields", len(comparison['common']))
        with col2:
            st.metric("Only in PDF 1", len(comparison['pdf1_only']))
        with col3:
            st.metric("Only in PDF 2", len(comparison['pdf2_only']))

        with st.spinner("Step 3: Checking NEPQA 2025 requirements..."):
            nepqa_results = check_nepqa(pdf1_text, pdf2_text, nepqa_text)

        st.success("✅ NEPQA check done!")

        st.subheader("📋 NEPQA 2025 Checklist")
        for item in nepqa_results:
            st.write(f"{item['status']} — {item['item']}")

        with st.spinner("Step 4: Generating compliance draft with Gemini AI... (this may take 30-60 seconds)"):
            report = generate_report(pdf1_text, pdf2_text, nepqa_text, comparison, nepqa_results)
            path = save_report(report)

        st.success("✅ Compliance draft generated!")
        st.markdown("---")
        st.subheader("📄 Compliance Draft")
        st.markdown(report)

        st.download_button(
            label="⬇️ Download Report",
            data=report,
            file_name="sunbridge_nepal_compliance_draft.md",
            mime="text/markdown"
        )

else:
    st.info("👈 Upload your 3 PDF files in the sidebar and click Generate!")
    
    st.markdown("### How it works")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("**📥 Step 1**\nUpload 2 manufacturer PDFs and NEPQA guideline")
    with col2:
        st.markdown("**🔍 Step 2**\nTool extracts and compares both documents")
    with col3:
        st.markdown("**✅ Step 3**\nChecks against Nepal import requirements")
    with col4:
        st.markdown("**📄 Step 4**\nAI generates compliance draft automatically")