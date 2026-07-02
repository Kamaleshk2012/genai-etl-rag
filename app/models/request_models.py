from pydantic import BaseModel
from typing import List

class FileUploadRequest(BaseModel):
    filenames: List[str]