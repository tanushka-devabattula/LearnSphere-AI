"""
pdf_utils.py

Utility functions for handling PDF files in AI Learning Buddy.
"""

from PyPDF2 import PdfReader


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF.

    Parameters:
        uploaded_file: Streamlit UploadedFile object

    Returns:
        str: Extracted text
    """
    try:
        reader = PdfReader(uploaded_file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text.strip()

    except Exception as e:
        raise Exception(f"Failed to read PDF: {e}")


def clean_pdf_text(text):
    """
    Cleans extracted PDF text by removing unnecessary spaces
    and blank lines.
    """

    if not text:
        return ""

    lines = text.splitlines()

    cleaned = [
        line.strip()
        for line in lines
        if line.strip()
    ]

    return "\n".join(cleaned)


def get_pdf_word_count(text):
    """
    Returns total number of words.
    """

    if not text:
        return 0

    return len(text.split())


def get_pdf_character_count(text):
    """
    Returns total number of characters.
    """

    if not text:
        return 0

    return len(text)


def get_pdf_page_count(uploaded_file):
    """
    Returns number of pages in PDF.
    """

    try:
        reader = PdfReader(uploaded_file)
        return len(reader.pages)

    except Exception:
        return 0


def get_pdf_statistics(uploaded_file):
    """
    Returns useful PDF statistics.

    Returns:
        {
            "pages": int,
            "words": int,
            "characters": int
        }
    """

    text = extract_text_from_pdf(uploaded_file)
    cleaned_text = clean_pdf_text(text)

    return {
        "pages": get_pdf_page_count(uploaded_file),
        "words": get_pdf_word_count(cleaned_text),
        "characters": get_pdf_character_count(cleaned_text),
    }
