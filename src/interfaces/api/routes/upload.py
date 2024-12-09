import os
import uuid
from fastapi import APIRouter, UploadFile, HTTPException

UPLOAD_FOLDER = "./static/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

router = APIRouter()

@router.post("/upload-svg/")
async def upload_svg(file: UploadFile):
    """
    Upload an SVG file to the server.
    """
    if not file.filename.endswith(".svg"):
        raise HTTPException(status_code=400, detail="Only SVG files are allowed.")
    
    # Save the file with a unique name
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.svg")
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    return {"file_id": file_id, "file_path": file_path}
