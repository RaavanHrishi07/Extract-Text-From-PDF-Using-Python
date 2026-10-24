
from pathlib import Path

import extract_text_from_pdf as pdf_tool


def test_project_directories_are_configured():
    """Check that input and output directories point to the project."""
    assert pdf_tool.INPUT_DIR == pdf_tool.BASE_DIR / "pdf_files"
    assert pdf_tool.OUTPUT_DIR == pdf_tool.BASE_DIR / "extracted_text"


def test_tesseract_path_is_configured():
    """Check that the Tesseract executable path is configured."""
    assert pdf_tool.TESSERACT_PATH.lower().endswith(
        r"tesseract-ocr\tesseract.exe"
    )


def test_poppler_path_is_configured():
    """Check that the Poppler binary directory is configured."""
    assert (Path(pdf_tool.POPPLER_PATH) / "pdftoppm.exe").name == "pdftoppm.exe"


def test_extract_text_from_pdf_creates_output_file(tmp_path, monkeypatch):
    """Check that extracted text is saved with the correct page marker."""

    class FakeImage:
        def close(self):
            pass

    monkeypatch.setattr(
        pdf_tool.pdf2image,
        "convert_from_path",
        lambda *args, **kwargs: [FakeImage()],
    )
    monkeypatch.setattr(
        pdf_tool.pytesseract,
        "image_to_string",
        lambda image: "Hello from a test PDF!",
    )
    monkeypatch.setattr(pdf_tool, "OUTPUT_DIR", tmp_path)

    output_path = pdf_tool.extract_text_from_pdf(
        pdf_tool.BASE_DIR / "sample.pdf"
    )

    assert output_path == tmp_path / "sample.txt"
    assert output_path.read_text(encoding="utf-8") == (
        "--- Page 1 ---\nHello from a test PDF!\n"
    )
