from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="data/chroma"
)

collection = client.get_collection(
    name="video_chunks"
)


def search_video(query, top_k=1):

    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results