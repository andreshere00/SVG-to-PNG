from fastapi import APIRouter, UploadFile, HTTPException
import os
import uuid

router = APIRouter()

UPLOAD_FOLDER = "./static/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload-svg/")
async def upload_svg(file: UploadFile):
    """Upload an SVG file to the server."""
    if not file.filename.endswith(".svg"):
        raise HTTPException(status_code=400, detail="Only SVG files are allowed.")

    # Save the uploaded file
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.svg")
    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {"file_id": file_id, "file_path": file_path}
