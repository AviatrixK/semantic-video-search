from pydantic import BaseModel


class AskRequest(BaseModel):
    query: str


class Source(BaseModel):
    video_name: str
    start: float
    end: float


class AskResponse(BaseModel):
    query: str
    answer: str
    sources: list[Source]