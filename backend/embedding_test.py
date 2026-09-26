import json

from .chunking.service import create_chunks
from .embeddings.service import create_embeddings


with open("data/transcripts/test_video.json", "r", encoding="utf-8") as f:
    data = json.load(f)


chunks = create_chunks(data["segments"])

texts = [chunk["text"] for chunk in chunks]

embeddings = create_embeddings(texts)


print("Number of chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)

print("\nFirst chunk:")
print(texts[0])

print("\nFirst embedding:")
print(embeddings[0])