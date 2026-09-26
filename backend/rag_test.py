from .search.service import search_video
from .rag.service import generate_answer


query = "Where did the speaker do internship?"

results = search_video(query, top_k=3)

context_parts = []

for i in range(len(results["documents"][0])):

    text = results["documents"][0][i]

    start = results["metadatas"][0][i]["start"]
    end = results["metadatas"][0][i]["end"]

    context_parts.append(
        f"[{start} - {end} seconds]\n{text}"
    )


context = "\n\n".join(context_parts)

answer = generate_answer(
    query,
    context
)

print("\nQuestion:")
print(query)

print("\nRetrieved context:")
print(context)

print("\nAnswer:")
print(answer)