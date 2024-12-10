import os

from fastapi import APIRouter, Form, HTTPException

from src.services.processor.svg_processor import SVGProcessor

UPLOAD_FOLDER = "./static/uploads/"
OUTPUT_FOLDER = "./static/output/"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

router = APIRouter()


@router.post("/convert-svg/")
async def convert_svg(
    file_id: str = Form(...),
    output_format: str = Form("png"),
    conversion_method: str = Form("cairo"),  # Add conversion_method parameter
):
    """Convert an uploaded SVG file to a PNG or another format using the specified method."""
    svg_file = os.path.join(UPLOAD_FOLDER, f"{file_id}.svg")
    if not os.path.exists(svg_file):
        raise HTTPException(status_code=404, detail="SVG file not found.")

    output_file = os.path.join(OUTPUT_FOLDER, f"{file_id}.{output_format}")

    # Process the SVG file with the specified method
    try:
        processor = SVGProcessor(conversion_method=conversion_method)
        output_path = processor.process(svg_file, output_file)
        if not output_path:
            raise HTTPException(status_code=500, detail="Conversion failed.")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"output_file": output_file}
