import os
import shutil
import subprocess


class InkscapeSVGConverter:
    """A converter class to process SVG files into PNG format using the Inkscape CLI."""

    def __init__(self):
        """
        Initialize the converter and ensures the Inkscape CLI is available.

        Raises:
            RuntimeError: If the Inkscape CLI is not found in the system PATH.
        """
        if not shutil.which("inkscape"):
            raise RuntimeError(
                "Inkscape CLI not found. Ensure Inkscape is installed and added to the PATH."
            )

    def convert(self, input_file: str, output_file: str) -> str:
        """
        Convert an SVG file to a PNG file using the Inkscape CLI.

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
            subprocess.run(
                [
                    "inkscape",
                    input_file,
                    "--export-type=png",
                    "--export-filename=" + output_file,
                ],
                check=True,
            )
            return output_file
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to convert SVG using Inkscape: {e}")
