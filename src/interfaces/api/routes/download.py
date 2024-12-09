import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/download-png/")
def download_file(file_path: str):
    """
    Download a file from the server.
    """
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found.")
    return FileResponse(file_path, media_type="application/octet-stream", filename=os.path.basename(file_path))
