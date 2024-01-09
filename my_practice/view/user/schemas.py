from datetime import datetime
from enum import Enum
from typing import Annotated, Optional, List
from annotated_types import MinLen, MaxLen

from pydantic import BaseModel

class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"
    master = "master"
    legend = "legend"
    goat = "GOAT"    

class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType

class User(BaseModel):
    id: int
    role: str
    name: Annotated[str, MinLen(3), MaxLen(25)]
    degree: Optional[List[Degree]] = []




