# NASA Space Biology Knowledge Engine - Scraping Tools

## About

This repository was created for the **NASA Space Apps Challenge 2025** to address the "Build a Space Biology Knowledge Engine" challenge. The project automates the bulk download of NASA space biology research papers as PDFs from a CSV dataset.

## What It Does

The tool reads space biology publication metadata from a CSV file (with PMC IDs) and automatically:
- Scrapes NASA's Life Sciences Data Archive and related databases
- Downloads full-text PDFs of research papers
- Organizes the downloaded papers for further analysis

## Technologies Used

- **Python** - Core programming language
- **Selenium** - Web automation framework
- **Microsoft Edge WebDriver (macOS M1)** - Browser automation driver
- **Pandas** - Data manipulation and CSV processing
- **BeautifulSoup4** - HTML parsing

## Repository Contents

- `100_pdfs_nasa.py` - Main scraping script
- `SB_publication_PMC.csv` - Input dataset with publication metadata and PMC IDs
- `msedgedriver` - Edge WebDriver executable for macOS M1

## Usage

```bash
pip install selenium pandas requests beautifulsoup4
python 100_pdfs_nasa.py
```

---

Built for NASA Space Apps Challenge 2025
