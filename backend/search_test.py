from .search.service import search_video


query = "What cybersecurity projects did the speaker work on?"

results = search_video(query, top_k=3)

print("Search results:")

for i in range(len(results["documents"][0])):

    distance = results["distances"][0][i]

    if distance > 1.5:
        continue

    print("\nResult:", i + 1)
    print("Distance:", distance)
    print("Text:")
    print(results["documents"][0][i])