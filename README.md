
# Extract Text From PDF Using Python

A Python tool that extracts text from PDF documents using Optical Character Recognition (OCR).

## Features

- Extracts text from PDF files using Tesseract OCR.
- Supports multiple PDF files in one run.
- Saves extracted text as UTF-8 `.txt` files.
- Separates extracted content by page.
- Displays processing progress and a summary.
- Handles errors for individual PDF files.

## Technologies Used

- Python 3.11+
- pdf2image
- pytesseract
- Pillow (used by pdf2image)
- Tesseract OCR
- Poppler

## Project Structure

```text
Extract-Text-From-PDF-Using-Python/
├── extract_text_from_pdf.py
├── README.md
├── .gitignore
├── pdf_files/
└── extracted_text/
```

## Requirements

- Python 3.11 or later
- Tesseract OCR
- Poppler for Windows

## Installation

Install the required Python packages:

```powershell
python -m pip install pdf2image Pillow pytesseract
```

Install Tesseract OCR and Poppler separately. Update `TESSERACT_PATH` and `POPPLER_PATH` in the Python script to match their installation locations.

## Usage

1. Place your PDF files inside the `pdf_files` folder.
2. Open PowerShell in the project directory.
3. Run:

```powershell
python .\extract_text_from_pdf.py
```

4. Find the generated `.txt` files inside `extracted_text`.

## Output Example

For an input file named `sample.pdf`, the program creates `sample.txt`.

Extracted text includes page markers such as:

```text
--- Page 1 ---
Text extracted from page one.

--- Page 2 ---
Text extracted from page two.
```

## Limitations

- OCR accuracy depends on PDF quality, image resolution, and document layout.
- Tesseract OCR and Poppler must be installed separately.
- Installation paths may differ between computers.

## Privacy

The `pdf_files/` and `extracted_text/` folders are excluded through `.gitignore` to help prevent personal documents and extracted text from being committed.

## Future Improvements

- Add a graphical user interface.
- Support OCR language selection.
- Add automated tests.
- Improve configuration for different operating systems.


## Author

**Hrishikesh Sharma**

- GitHub: [@RaavanHrishi07](https://github.com/RaavanHrishi07)
- Repository: [Extract-Text-From-PDF-Using-Python](https://github.com/RaavanHrishi07/Extract-Text-From-PDF-Using-Python)
