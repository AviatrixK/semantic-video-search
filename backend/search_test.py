from .search.service import search_video


query = "What cybersecurity projects did the speaker work on?"

results = search_video(query)

print("Search results:")

for i in range(len(results["documents"][0])):

    print("\nResult:", i + 1)

    print("Text:")
    print(results["documents"][0][i])

    print("Metadata:")
    print(results["metadatas"][0][i])

    print("Distance:")
    print(results["distances"][0][i])