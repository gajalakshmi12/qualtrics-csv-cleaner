# qualtrics-csv-cleaner
Cleaning survey results from Qualtrics and extract submitted documents

# Qualtrics Assessment Cleaner (macOS)

This tool parses and cleans raw CSV exports from Qualtrics assessment surveys, extracting structured data and downloading any attached documentation. The processed output includes a formatted Excel workbook and associated files grouped by assessment type.

Built with Python, packaged via PyInstaller. This version targets macOS.

---

## Features

- Parses and cleans Qualtrics survey CSVs
- Separates Program and DDC assessments into separate sheets
- Downloads submitted documents from survey responses
- Outputs a clean `assessment_cleaned.xlsx` and organized folders

---

## Usage (macOS)

1. **Download the build:**
   - Go to the Actions tab
   - Download the latest artifact (`macOS-cleaner`) from the most recent workflow run

2. **Extract and run:**
   - Unzip the downloaded file
   - You’ll find a binary named `cleaning_script` (no extension)
   - Right-click the binary → **Open**
   - Use the file picker to select your Qualtrics `.csv` file

3. **Output:**
   - Results are saved in a new `output/` directory:
     - `assessment_cleaned.xlsx`
     - `downloads/program/` — all program assessment files
     - `downloads/ddc/` — all DDC assessment files

---

## macOS Security Notes

First launch will prompt a security warning:

> “cleaning_script” cannot be opened because the developer cannot be verified.

Bypass this by:

- Right-click → **Open**
- Confirm the prompt
- The app will run normally after this first step

---

## Requirements

- macOS 10.15+
- Internet connection for document downloads
- Qualtrics survey CSV with expected column structure

---

## Troubleshooting

- If no output is generated, ensure your CSV includes completed responses and valid document URLs
- File downloads rely on direct URLs (e.g., `File.php?F=` format); ensure these are accessible
- If the app crashes, run it from Terminal to view error output

---

