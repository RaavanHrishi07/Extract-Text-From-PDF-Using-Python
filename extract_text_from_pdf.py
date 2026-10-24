
from pathlib import Path

import pdf2image
import pytesseract


# Project paths
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "pdf_files"
OUTPUT_DIR = BASE_DIR / "extracted_text"

# External tools
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"D:\Release-26.09.0-0\poppler-26.09.0\Library\bin"

# Configure Tesseract
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def extract_text_from_pdf(pdf_path: Path) -> Path:
    """Extract text from a PDF using OCR and save it as a text file."""

    print(f"\nExtracting text from: {pdf_path.name}")

    output_path = OUTPUT_DIR / f"{pdf_path.stem}.txt"
    extracted_text = []

    images = pdf2image.convert_from_path(
        str(pdf_path),
        poppler_path=POPPLER_PATH,
    )

    try:
        for page_number, image in enumerate(images, start=1):
            try:
                print(f"Processing page {page_number}/{len(images)}...")

                text = pytesseract.image_to_string(image)
                extracted_text.append(
                    f"--- Page {page_number} ---\n{text.strip()}"
                )
            finally:
                image.close()
    finally:
        # Release image resources even if OCR fails.
        images.clear()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_path.write_text(
        "\n\n".join(extracted_text) + "\n",
        encoding="utf-8",
    )

    print(f"Successfully saved text to: {output_path}")

    return output_path


def main():
    """Validate dependencies and process all PDFs in the input folder."""

    print("=" * 55)
    print("       PDF TEXT EXTRACTION TOOL")
    print("=" * 55)

    # Validate Tesseract installation.
    if not Path(TESSERACT_PATH).is_file():
        print(f"ERROR: Tesseract not found at:\n{TESSERACT_PATH}")
        return

    # Validate Poppler installation.
    if not (Path(POPPLER_PATH) / "pdftoppm.exe").is_file():
        print(f"ERROR: Poppler not found at:\n{POPPLER_PATH}")
        return

    # Create required folders.
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Find PDF files (case-insensitive extension).
    pdf_files = sorted(
        path
        for path in INPUT_DIR.iterdir()
        if path.is_file() and path.suffix.lower() == ".pdf"
    )

    if not pdf_files:
        print(f"\nNo PDF files found in:\n{INPUT_DIR}")
        print("Place one or more PDF files in the pdf_files folder.")
        return

    print(f"\nFound {len(pdf_files)} PDF file(s).")

    successful = 0
    failed = 0

    for pdf_path in pdf_files:
        try:
            extract_text_from_pdf(pdf_path)
            successful += 1
        except Exception as error:
            failed += 1
            print(f"ERROR processing {pdf_path.name}: {error}")

    print("\n" + "=" * 55)
    print("                 EXTRACTION SUMMARY")
    print("=" * 55)
    print(f"Total PDFs : {len(pdf_files)}")
    print(f"Successful : {successful}")
    print(f"Failed     : {failed}")
    print(f"Output     : {OUTPUT_DIR}")
    print("=" * 55)


if __name__ == "__main__":
    main()
