from src.extract import Extractor
from src.chunker import Chunker
from src.database import Database
from src.generate import Generator

class RAGPipeline:
    def __init__(self):
        self.extractor = Extractor()
        self.chunker = Chunker()
        self.database = Database()
        self.generator = Generator()

    def add_document(self, pdf_path: str) -> None:
        """Extract, chunk and store a PDF."""
        text = self.extractor.extract(pdf_path)
        chunks = self.chunker.chunk(text)
        self.database.store(chunks)
        print(f"✅ Document added successfully")

    def process_query(self, query: str) -> str:
        """Retrieve relevant chunks and generate a response."""
        chunks = self.database.retrieve(query)
        print(f"✅ Found {len(chunks)} relevant chunks")
        for i, chunk in enumerate(chunks):
            print(f"🔍 Chunk {i+1}: {chunk}\n")
        response = self.generator.generate(query, chunks)
        return response


if __name__ == "__main__":
    pipeline = RAGPipeline()

    # Add your PDF
    pipeline.add_document("sample_data/source/sl_booklet.pdf")

    # Query loop
    print("\n🚀 RAG Pipeline Ready!\n")
    while True:
        query = input("Your question (or 'quit'): ").strip()
        if query.lower() == "quit":
            break
        response = pipeline.process_query(query)
        print(f"\n✨ Answer: {response}\n")