import os
import shutil
import subprocess


class InkscapeSVGConverter:
    """A converter class to process SVG files into PNG format using the Inkscape CLI."""

    def __init__(self):
        """Ensure the Inkscape CLI is available."""
        if not shutil.which("inkscape"):
            raise RuntimeError(
                "Inkscape CLI not found. Ensure Inkscape is installed and added to the PATH."
            )

    def convert(self, input_file: str, output_file: str, dpi: int = 300) -> str:
        """
        Convert an SVG file to a PNG file using the Inkscape CLI.

        Args:
            input_file (str): Path to the input SVG file.
            output_file (str): Path to the output PNG file.
            dpi (int): Dots per inch for the PNG output. Default is 300.

        Returns:
            str: Path to the output PNG file if successful.
        """
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input SVG file not found: {input_file}")

        try:
            subprocess.run(
                [
                    "inkscape",
                    input_file,
                    "--export-type=png",
                    f"--export-dpi={dpi}",
                    "--export-filename=" + output_file,
                ],
                check=True,
            )
            return output_file
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to convert SVG using Inkscape: {e}")
