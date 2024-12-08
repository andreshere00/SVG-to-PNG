from cairosvg import svg2png

class CairoSVGConverter:
    """
    A converter class to process SVG files into PNG format using CairoSVG.
    """

    def convert(self, input_file: str, output_file: str) -> str:
        """
        Converts an SVG string to a PNG file using CairoSVG.

        Args:
            svg_code (str): SVG content as a string.
            output_file (str): Path to the output PNG file.

        Returns:
            str: Path to the output PNG file if successful.
        """
        try:
            with open(input_file, "rb") as svg_file:
                svg2png(file_obj=svg_file, write_to=output_file)
            return output_file
        except Exception as e:
            print(f"Failed to convert SVG to PNG using CairoSVG: {e}")
            return None
