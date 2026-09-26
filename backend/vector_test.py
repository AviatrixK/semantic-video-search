import json

from .chunking.service import create_chunks
from .embeddings.service import create_embeddings
from .vector_store.service import add_chunks


with open("data/transcripts/test_video.json", "r", encoding="utf-8") as f:
    data = json.load(f)


chunks = create_chunks(data["segments"])

texts = [chunk["text"] for chunk in chunks]

embeddings = create_embeddings(texts)


add_chunks(
    chunks,
    embeddings,
    data["video_name"]
)


print("Chunks successfully stored in ChromaDB")