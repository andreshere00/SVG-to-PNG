from cairosvg import svg2png


class CairoSVGConverter:
    """A converter class to process SVG files into PNG format using CairoSVG."""

    def convert(self, input_file: str, output_file: str, dpi: int = 300) -> str:
        """
        Convert an SVG file to a high-resolution PNG file using CairoSVG.

        Args:
            input_file (str): Path to the SVG input file.
            output_file (str): Path to the output PNG file.
            dpi (int): Dots per inch for the output PNG. Higher values result in higher resolution. Default is 300.

        Returns:
            str: Path to the output PNG file if successful.
        """
        try:
            with open(input_file, "rb") as svg_file:
                svg2png(file_obj=svg_file, write_to=output_file, dpi=dpi)
            return output_file
        except Exception as e:
            raise RuntimeError(f"Failed to convert SVG to PNG using CairoSVG: {e}")
