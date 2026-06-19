from typing import List

class Chunker:
    def chunk(self, text: str, chunk_size: int = 200) -> List[str]:
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append(chunk)
        print(f"Created {len(chunks)} chunks of {chunk_size} words each")
        return chunks