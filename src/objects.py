from dataclasses import dataclass
from typing import List


@dataclass(slots=True)
class Task:
    name: str
    description: str
    task_req: str | None = None


@dataclass
class LabTasks:
    number: int
    tasks: List[Task]


@dataclass
class AllLabTasks:
    labs: List[LabTasks]



@dataclass(slots=True)
class SolvedTask:
    name: str
    code: str
