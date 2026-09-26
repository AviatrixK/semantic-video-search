from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .search.service import search_video
from .schemas.search import SearchRequest, SearchResponse
from .rag.service import generate_answer
from .schemas.ask import AskRequest, AskResponse

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):

    results = search_video(
        request.query,
        top_k=3
    )

    context_parts = []
    sources = []

    for i in range(len(results["documents"][0])):

        distance = results["distances"][0][i]

        if distance > 1.5:
            continue

        text = results["documents"][0][i]

        video_name = results["metadatas"][0][i]["video_name"]
        start = results["metadatas"][0][i]["start"]
        end = results["metadatas"][0][i]["end"]

        context_parts.append(
            f"[{start} - {end} seconds]\n{text}"
        )

        sources.append({
            "video_name": video_name,
            "start": start,
            "end": end
        })

    context = "\n\n".join(context_parts)

    answer = generate_answer(
        request.query,
        context
    )

    return {
        "query": request.query,
        "answer": answer,
        "sources": sources
    }