from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str


class SearchResult(BaseModel):
    text: str
    video_name: str
    start: float
    end: float
    distance: float


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]