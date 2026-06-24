# NurseGPT Python Scripts

## Overview
This repository contains Python scripts developed during the evaluation of **NurseGPT**, an AI-powered documentation tool being piloted at Brenda Strafford Foundation (BSF) Cambridge Manor, a long-term care facility in Calgary, Alberta.

These scripts support data cleaning, preprocessing, and analysis of baseline observational and clinical data collected during the study.

---

## Scripts

### 1. DataPreprocessing_TotalTime_Outliers_Filtered_Only_KN.ipynb
**Purpose:** Cleans and preprocesses baseline observational charting data for statistical analysis in SPSS.

**Key steps:**
- Loads raw Excel data from the benchmarking sheet
- Strips whitespace and forward fills identifier columns
- Filters to KN-collected observations only
- Converts date columns to string format for SPSS compatibility
- Removes outliers in total charting time using a defined threshold
- Exports cleaned CSV for SPSS analysis

**Libraries:** `pandas`, `numpy`, `seaborn`, `matplotlib`

---

### 2. Patient_Pattern_Date_Extracted.ipynb
**Purpose:** Extracts Created Date and Effective Date from PDF progress notes using regex pattern matching for nurses charting's pattern analysis (spread across shifts versus lump at the end of shift)

**Key steps:**
- Opens PDF progress notes using `pymupdf`
- Applies regex patterns to extract date and timestamp fields
- Structures extracted data into a pandas DataFrame
- Flags rows with null values for review

**Libraries:** `pandas`, `pymupdf`, `re`

---

### 3. NurseGPT_WER_Evaluation_Script.ipynb
**Purpose:** Evaluate NurseGPT transcription accuracy in sandbox environment before full deployment in Care Neighborhood by computing Word Error Rate between BSF progress notes (reference) and NurseGPT transcripts (hypothesis) across Green, Yellow, and Red test case tiers.

**Key steps:**
- Load and preprocesses reference and hypothesis diagnoses
- Applies text normalization (contractions, number-to-word conversion, whitespace removal, time formatting, etc.)
- Merge NurseGPT transcripts with BSF progress notes by Page Number ID
- Compute WER metrics using the `jiwer` library
- Outputs a scored DataFrame with error counts per test case and export to CSV files for analysis
- For more information on workflow, please visit the following link: [NurseGPT WER Benchmark Workflow Diagram](https://app.mural.co/t/khuongnguyen8881/m/khuongnguyen8881/1774901102904/4617abf48d2d21e090bcb665a137f0a896ec5b0c)

**Libraries:** `pandas`, `jiwer`, `re`

---

## Notes
- Raw data files are excluded from this repository to protect patient privacy
- All scripts use placeholder file paths (update `INSERT_FILE_PATH` before running)
- This work is part of a mixed-methods evaluation study (Acute Care Alberta Evaluation Team, 2025–2026)

---

## Author
KN1235 — Research Evaluation Intern, Acute Care Alberta
