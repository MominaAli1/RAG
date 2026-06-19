from typing import List
from groq import Groq

class Generator:
    def __init__(self):
        self.client = Groq()

    def generate(self, query: str, chunks: List[str]) -> str:
        context = "\n\n".join(chunks)
        
        prompt = f"""Answer the question using only the context below.

Context:
{context}

Question: {query}

Answer:"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content