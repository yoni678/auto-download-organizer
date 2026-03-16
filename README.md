# Auto Download Organizer

This project contains Python scripts that automate downloading and organizing files:

- **PDF Downloader**: Automatically navigates to sample PDF pages and downloads PDFs into a `pdf/` folder.
- **Excel Downloader**: Automatically navigates to sample XLS/XLSX pages and downloads spreadsheets into a `spreadsheets/` folder.
- **Automatic Organization**: All files are moved into folders based on file type (`pdf/`, `spreadsheets/`, `documents/`, `images/`).

## Features

- Uses **Playwright** for browser automation and page interaction.
- Uses **Python** for file handling and organization.
- Works as a **portfolio-ready automation project** demonstrating a full download-to-organization pipeline.
- Easily expandable to support more file types.

## How to Use

1. Clone the repository
2. Install dependencies: `pip install playwright requests`
3. Run the scripts separately: `download_pdf.py` and `download_xlsx.py`
4. Check your Downloads folder for organized files

---
