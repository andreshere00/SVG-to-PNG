from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import os


class ReportLabSVGConverter:
    """
    A converter class to process SVG files into PNG format using ReportLab and svglib.
    """

    def convert(self, input_file: str, output_file: str) -> str:
        """
        Converts an SVG file to a PNG file using ReportLab.

        Args:
            input_file (str): Path to the input SVG file.
            output_file (str): Path to the output PNG file.

        Returns:
            str: Path to the output PNG file if successful.

        Raises:
            RuntimeError: If the conversion fails.
        """
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input SVG file not found: {input_file}")

        try:
            # Read the SVG file and convert to a drawing object
            drawing = svg2rlg(input_file)

            # Export as PNG
            renderPM.drawToFile(drawing, output_file, fmt="PNG")
            return output_file
        except Exception as e:
            raise RuntimeError(f"Failed to convert SVG using ReportLab: {e}")