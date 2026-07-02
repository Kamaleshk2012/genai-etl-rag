from pydantic import BaseModel
from typing import List, Dict, Any

class TransformResponse(BaseModel):
    data: List[Dict[str, Any]]