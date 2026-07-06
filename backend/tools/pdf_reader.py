import fitz  # PyMuPDF


class PDFReader:
    @staticmethod
    def extract_text(pdf_path: str) -> str:
        """
        Extract all text from a PDF resume.
        """

        text = ""

        try:
            document = fitz.open(pdf_path)

            for page in document:
                text += page.get_text()

            document.close()

            return text

        except Exception as e:
            return f"Error reading PDF: {e}"


pdf_reader = PDFReader()