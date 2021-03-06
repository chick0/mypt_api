from pydantic import BaseModel

from v3.storage.models import Date


class ProjectRequest(BaseModel):
    title: str
    date: str   # YYYY-MM-DD
    tag: str
    web: str
    github: str
    a: str  # 기획 의도
    b: str  # 특징
    c: str  # 느낀점


class ProjectDetail(BaseModel):
    uuid: str
    title: str
    date: Date
    tags: list[str]
    web: str
    github: str
    a: str  # 기획 의도
    b: str  # 특징
    c: str  # 느낀점


class ProjectDeleteStatus(BaseModel):
    status: bool


class ProjectEditResult(BaseModel):
    result: bool


class ProjectCreated(BaseModel):
    uuid: str
