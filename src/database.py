from typing import List
from sentence_transformers import SentenceTransformer
import chromadb

class Database:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("book")

    def store(self, chunks: List[str]) -> None:
        print("Embedding chunks...")
        embeddings = self.model.encode(chunks).tolist()
        ids = [str(i) for i in range(len(chunks))]
        self.collection.add(
            embeddings=embeddings,
            documents=chunks,
            ids=ids
        )
        print(f"✅ Stored {len(chunks)} chunks in vector database")

    def retrieve(self, query: str, top_k: int = 3) -> List[str]:
        query_embedding = self.model.encode([query]).tolist()
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )
        return results["documents"][0]