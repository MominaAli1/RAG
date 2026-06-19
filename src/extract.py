import PyPDF2

class Extractor:
    def extract(self, path: str) -> str:
        text = ""
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
        print(f" Extracted text from {len(reader.pages)} pages")
        return text.strip()