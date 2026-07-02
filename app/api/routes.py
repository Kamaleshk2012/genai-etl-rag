from fastapi import APIRouter, UploadFile, File
from typing import Annotated

from app.services.ingestion_service import load_files
from app.services.transformation_service import join_data, transform_data
from app.utils.file_writer import save_output

router = APIRouter()

@router.get("/check-route")
def check_route():
    return {"message": "NEW ROUTE FILE LOADED ✅"}

@router.post("/transform")
async def transform(
    device: Annotated[UploadFile, File(...)],
    location: Annotated[UploadFile, File(...)]
):
    files = [device, location]

    data = load_files(files)

    device_df = data.get(device.filename)
    location_df = data.get(location.filename)

    if device_df is None or location_df is None:
        return {"error": "File loading failed"}

    merged = join_data(device_df, location_df)
    result = transform_data(merged)

    filename = save_output(result)

    return {
        "message": "Transformation complete",
        "file": filename,
        "data": result
    }


