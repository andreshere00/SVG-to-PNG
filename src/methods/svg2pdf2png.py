# app/converters/pdf_to_png_converter.py
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from pdf2image import convert_from_path
from src.methods.base_converter import BaseConverter
from typing import Optional
import os

class PDFToPNGConverter(BaseConverter):
    """
    Converts an SVG file to PNG by first converting it to a PDF.
    """

    def convert(self, svg_file: str, output_file: str) -> Optional[str]:
        try:
            pdf_file = os.path.splitext(output_file)[0] + ".pdf"

            # Convert SVG to PDF
            drawing = svg2rlg(svg_file)
            renderPDF.drawToFile(drawing, pdf_file)

            # Convert PDF to PNG
            images = convert_from_path(pdf_file)
            images[0].save(output_file, "PNG")

            # Clean up intermediate PDF file if needed
            os.remove(pdf_file)

            return output_file
        except Exception as e:
            print(f"Error during conversion: {e}")
            return None
