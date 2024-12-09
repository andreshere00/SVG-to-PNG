from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse
from src.services.processor.svg_processor import SVGProcessor
import os
import uuid

app = FastAPI()

UPLOAD_FOLDER = "./static/input/"
OUTPUT_FOLDER = "./static/output/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.post("/upload-svg/")
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

@app.post("/convert-svg/")
async def convert_svg(file_id: str = Form(...), output_format: str = Form("png")):
    """
    Convert an uploaded SVG file to a PNG.
    """
    svg_file = os.path.join(UPLOAD_FOLDER, f"{file_id}.svg")
    if not os.path.exists(svg_file):
        raise HTTPException(status_code=404, detail="SVG file not found.")

    output_file = os.path.join(OUTPUT_FOLDER, f"{file_id}.{output_format}")
    
    # Process the SVG file
    processor = SVGProcessor()
    output_path = processor.process(svg_file, output_file)
    if not output_path:
        raise HTTPException(status_code=500, detail="Conversion failed.")
    
    return {"output_file": output_file}

@app.get("/download-png/")
def download_file(file_path: str):
    """
    Download a file from the server.
    """
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found.")
    return FileResponse(file_path, media_type="application/octet-stream", filename=os.path.basename(file_path))
