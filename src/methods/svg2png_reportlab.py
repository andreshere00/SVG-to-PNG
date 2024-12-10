import os

from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg


class ReportLabSVGConverter:
    """Process SVG files into PNG format using ReportLab and svglib."""

    def convert(self, input_file: str, output_file: str, scale: float = 2.0) -> str:
        """
        Convert an SVG file to a PNG file using ReportLab.

        Args:
            input_file (str): Path to the input SVG file.
            output_file (str): Path to the output PNG file.
            scale (float): Scaling factor for the output PNG resolution. Default is 2.0.

        Returns:
            str: Path to the output PNG file if successful.
        """
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input SVG file not found: {input_file}")

        try:
            # Read the SVG file and convert to a drawing object
            drawing = svg2rlg(input_file)

            # Apply scaling
            drawing.width *= scale
            drawing.height *= scale
            drawing.scale(scale, scale)

            # Export as PNG
            renderPM.drawToFile(drawing, output_file, fmt="PNG")
            return output_file
        except Exception as e:
            raise RuntimeError(f"Failed to convert SVG using ReportLab: {e}")
