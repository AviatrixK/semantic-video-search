import json

from .chunking.service import create_chunks


with open("data/transcripts/test_video.json", "r", encoding="utf-8") as f:
    data = json.load(f)

chunks = create_chunks(data["segments"])

print(f"Created {len(chunks)} chunks")

for i, chunk in enumerate(chunks):
    print("\nChunk:", i + 1)
    print("Start:", chunk["start"])
    print("End:", chunk["end"])
    print("Text:", chunk["text"])