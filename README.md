# ☀️ SunBridge Nepal Compliance Tool

An AI-powered compliance assistant that helps SunBridge Trading prepare 
Nepal import documentation for grid-tied solar inverters imported from China.

---

## 🧩 Problem It Solves

When importing solar inverters from China into Nepal, importers need to 
submit compliance documents in Nepal's format (NEPQA 2025). 
Manufacturer PDFs arrive in Chinese export format — different structure, 
different terminology.

This tool reads both manufacturer PDFs, compares them, checks against 
Nepal's NEPQA 2025 import requirements, and automatically generates a 
structured compliance draft using Gemini AI.

---

## ⚙️ How It Works

1. **Extract** — Reads text from both manufacturer PDFs and NEPQA 2025 guideline
2. **Compare** — Finds matching fields and mismatches between the two PDFs
3. **Check** — Validates against Nepal NEPQA 2025 import requirements
4. **Generate** — Uses Gemini AI to produce a structured compliance draft
5. **Save** — Exports the draft as a markdown file ready to share

---

## 🗂️ Project Structure