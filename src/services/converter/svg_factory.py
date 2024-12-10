from src.methods.svg2pdf2png import PDFToPNGConverter
from src.methods.svg2png_cairo import CairoSVGConverter
from src.methods.svg2png_inkscape import InkscapeSVGConverter
from src.methods.svg2png_reportlab import ReportLabSVGConverter


class ConverterFactory:
    """Factory class to create converter instances based on the specified method."""

    @staticmethod
    def get_supported_methods():
        """
        Get the list of supported conversion methods.

        Returns:
            list: List of supported conversion method names.
        """
        return {
            "cairo": CairoSVGConverter,
            "reportlab": ReportLabSVGConverter,
            "inkscape": InkscapeSVGConverter,
            "pdf": PDFToPNGConverter,
        }.keys()

    @staticmethod
    def get_converter(conversion_method: str):
        """
        Get the appropriate converter based on the conversion method.

        Args:
            conversion_method (str): The conversion method to use.

        Returns:
            BaseConverter: An instance of the appropriate converter class.

        Raises:
            ValueError: If the specified conversion method is not supported.
        """
        supported_methods = {
            "cairo": CairoSVGConverter,
            "reportlab": ReportLabSVGConverter,
            "inkscape": InkscapeSVGConverter,
            "pdf": PDFToPNGConverter,
        }

        if conversion_method not in supported_methods:
            raise ValueError(
                f"Unsupported conversion method: {conversion_method}. "
                f"Supported methods: {list(supported_methods.keys())}"
            )

        return supported_methods[conversion_method]()
