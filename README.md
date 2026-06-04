# Bridging-literature-and-model
Bridging literature and models: a workflow for harmonizing agricultural datasets for simulation model using AI

# Summary of the Codebase and Data

## Overview

This project is a **scientific data extraction pipeline** that uses **Large Language Models (LLMs)** — specifically fine-tuned OpenAI GPT models — to automatically extract structured crop experiment metadata from scientific PDF papers. The extracted data is mapped to the **ICASA (International Consortium for Agricultural Systems Applications)** standard, making it **FAIR** (Findable, Accessible, Interoperable, Reusable) for use in crop modeling and agronomy research. The project is part of the **FAIRagro** initiative at **ZALF (Leibniz Centre for Agricultural Landscape Research)**.

---

## Dataset

- **55 crop modeling papers** are used in total (see `1.0 paper list.txt`):
  - **45 papers** → used for **training** (fine-tuning the LLM)
  - **10 papers** → used for **evaluation**
- Papers cover a wide range of crops (wheat, maize, soybean, sorghum, barley, etc.) and topics (yield simulation, CO₂ enrichment, irrigation, nitrogen management, soil carbon, etc.)

---

## Folder Structure

| Folder / File | Description |
|---|---|
| `1.0 paper list.txt` | List of 55 publications used in the study |
| `1.1 workflow script/` | Python scripts implementing the full pipeline (Steps 1–3) |
| `2.0 template_icasa_vba_trainingSet_allColumns.xlsm` | Excel template with ICASA variable definitions used for manual extraction and as LLM prompt reference |
| `3.0 Training dataset for fine tuning model/` | JSONL files used to fine-tune the GPT model (one file per ICASA category) |
| `4.0 JSON files manually template/` | Manually extracted JSON files per paper per ICASA category (ground truth) |
| `5.0 combine manual into Tabular/` | Manual extraction results converted to tabular Excel format (one `.xlsx` per paper) |
| `6.0 llm structure output JSON/` | LLM-generated structured JSON outputs per paper per ICASA category |
| `7.0 llm structure output Tbular/` | LLM JSON outputs converted to tabular format (Excel + plots) |
| `Readme.md` | Brief description of each folder |

---

## Pipeline Workflow (Step by Step)

### Step 1 — PDF to Markdown (`step1_correct_pdf_to_markdown.py`)
- Uses the **`marker`** tool (a PDF-to-Markdown converter) to convert scientific PDF papers into Markdown text files.
- Input: folder of PDF papers
- Output: folder of Markdown files

### Step 2 — Markdown Preprocessing (steps 2.1–2.7)
A series of scripts that clean and enrich the Markdown files:

| Script | Purpose |
|---|---|
| `step2.1` | Extract **Methods sections** from Markdown |
| `step2.2` | Extract **tables appearing before** the Methods section |
| `step2.3` | Combine tables-before-methods + methods sections |
| `step2.4` | Extract **author names** from Markdown |
| `step2.5` | Add author info to the combined content |
| `step2.6` | Extract **publication/corresponding date** from Markdown |
| `step2.7` | Add year/date info to the combined content |

Output: enriched Markdown files containing methods text, relevant tables, author names, and publication year — ready for LLM processing.

### Step 3 — LLM Structured Extraction (`step3.1_extract_icasa_group_variables_...py`)
- Reads the enriched Markdown files and the ICASA Excel template.
- Constructs structured prompts for each **ICASA data category**.
- Calls the **fine-tuned OpenAI GPT model** (e.g., `gpt-4.1-mini`) via API.
- Saves the LLM responses as structured **JSON files** per paper per category.

---

## ICASA Data Categories Extracted

The pipeline extracts data across **8 ICASA-standard categories**:

| Category | Description |
|---|---|
| `exp_metadata` | Experiment metadata (location, dates, objectives) |
| `fields` | Soil and field characteristics |
| `genotypes` | Crop cultivar/genotype information |
| `planting` | Sowing/planting details |
| `irrigation` | Irrigation management |
| `fertilization` | Fertilizer application details |
| `harvest` | Harvest data and yield observations |
| `plot_details` | Plot-level experimental design details |

---

## Fine-Tuning Approach

- **Training data** (folder `3.0`): JSONL files where each record contains a paper's extracted Markdown text as input and the manually curated ICASA-structured JSON as the expected output.
- The model is fine-tuned separately for each ICASA category.
- After fine-tuning, the model is applied to all 55 papers to generate automatic extractions (folders `6.0` and `7.0`).
- Results are compared against the manual extractions (folders `4.0` and `5.0`) for evaluation.

---

## Technology Stack

| Component | Tool / Library |
|---|---|
| PDF → Markdown | `marker` (Python CLI tool) |
| LLM API | OpenAI GPT (fine-tuned, e.g., `gpt-4.1-mini`) |
| Data standard | ICASA (International Consortium for Agricultural Systems Applications) |
| Scripting | Python |
| Data storage | JSON, JSONL, Excel (`.xlsx`, `.xlsm`) |
| Initiative | FAIRagro / ZALF |

---

## Key Goal

> Automate the extraction of structured, ICASA-compliant crop experiment data from scientific literature using fine-tuned LLMs, reducing manual curation effort while maintaining data quality for use in crop modeling and agricultural research.
