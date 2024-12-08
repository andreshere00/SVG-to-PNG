from src.methods.svg2pdf2png import PDFToPNGConverter
from src.methods.svg2png_cairo import CairoSVGConverter
from src.methods.svg2png_inkscape import InkscapeSVGConverter
from src.methods.svg2png_reportlab import ReportLabSVGConverter


class ConverterFactory:
    """
    Factory class to provide the appropriate converter based on the method.
    """

    @staticmethod
    def get_converter(method: str):
        """
        Returns the appropriate converter instance based on the method.

        Args:
            method (str): The method for conversion ("pdf", "cairo", "inkscape", "reportlab").

        Returns:
            An instance of the corresponding converter.

        Raises:
            ValueError: If the method is unsupported.
        """
        if method == "pdf":
            return PDFToPNGConverter()
        elif method == "cairo":
            return CairoSVGConverter()
        elif method == "inkscape":
            return InkscapeSVGConverter()
        elif method == "reportlab":
            return ReportLabSVGConverter()
        else:
            raise ValueError(f"Unsupported conversion method: {method}")