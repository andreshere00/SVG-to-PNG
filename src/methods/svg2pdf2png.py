# app/converters/pdf_to_png_converter.py
import os
from typing import Optional

from pdf2image import convert_from_path
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

from src.methods.base_converter import BaseConverter


class PDFToPNGConverter(BaseConverter):
    """Convert an SVG file to PNG by first converting it to a PDF."""

    def convert(self, svg_file: str, output_file: str) -> Optional[str]:
        """
        Convert an SVG file to a PNG image by first converting it to a PDF.

        Args:
            svg_file (str): The file path to the input SVG file.
            output_file (str): The desired file path for the output PNG image.

        Returns:
            Optional[str]: The file path to the output PNG image if the conversion
            is successful; otherwise, returns None.

        Raises:
            Exception: If an error occurs during the conversion process, an
            exception is caught, an error message is printed, and None is returned.
        """
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
