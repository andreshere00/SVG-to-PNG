import os
from typing import Optional

from pdf2image import convert_from_path
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg


class PDFToPNGConverter:
    """Convert an SVG file to PNG by first converting it to a PDF."""

    def convert(self, svg_file: str, output_file: str, dpi: int = 300) -> Optional[str]:
        """
        Convert an SVG file to a high-resolution PNG image by first converting it to a PDF.

        Args:
            svg_file (str): The file path to the input SVG file.
            output_file (str): The desired file path for the output PNG image.
            dpi (int): Dots per inch for the PNG output. Default is 300.

        Returns:
            Optional[str]: The file path to the output PNG image if successful.
        """
        try:
            pdf_file = os.path.splitext(output_file)[0] + ".pdf"

            # Convert SVG to PDF
            drawing = svg2rlg(svg_file)
            renderPDF.drawToFile(drawing, pdf_file)

            # Convert PDF to PNG
            images = convert_from_path(pdf_file, dpi=dpi)
            images[0].save(output_file, "PNG")

            # Clean up intermediate PDF file if needed
            os.remove(pdf_file)

            return output_file
        except Exception as e:
            raise RuntimeError(f"Error during conversion: {e}")
