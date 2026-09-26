import chromadb


client = chromadb.PersistentClient(
    path="data/chroma"
)


collection = client.get_or_create_collection(
    name="video_chunks"
)


def add_chunks(chunks, embeddings, video_name):
    ids = []
    documents = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        ids.append(f"{video_name}_{i}")

        documents.append(chunk["text"])

        metadatas.append({
            "video_name": video_name,
            "start": chunk["start"],
            "end": chunk["end"]
        })

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )   