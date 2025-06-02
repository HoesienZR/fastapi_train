from typing import TypeVar,Generic,Optional,List,Optional,Any
from pydantic import BaseModel,Field
from pydantic.generics import GenericModel

M = TypeVar("M")

class PaginatedResponse(GenericModel, Generic[M]):
    count : int = Field(description="number of items returned ")
    items : List[M] = Field(description="list of items returned ")