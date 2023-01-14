import json
from typing import Any
from pydantic import BaseModel


class RuntimeValidatedModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    def to_json(self) -> str:
        return self.json()

    def to_dict(self) -> Any:
        return json.loads(self.to_json())
