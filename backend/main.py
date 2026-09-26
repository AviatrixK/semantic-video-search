from fastapi import FastAPI

from .search.service import search_video
from .schemas.search import SearchRequest, SearchResponse

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Semantic Video Search API is running"
    }


@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):

    results = search_video(
        request.query,
        top_k=3
    )

    response = []

    for i in range(len(results["documents"][0])):

        response.append({
            "text": results["documents"][0][i],
            "video_name": results["metadatas"][0][i]["video_name"],
            "start": results["metadatas"][0][i]["start"],
            "end": results["metadatas"][0][i]["end"],
            "distance": results["distances"][0][i]
        })

    return {
        "query": request.query,
        "results": response
    }