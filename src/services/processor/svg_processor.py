from src.config.logs.logger import LoggerManager
from src.services.converter.svg_factory import ConverterFactory
from src.utils.tracer import Tracer


class SVGProcessor:
    """Main class to process SVG files and convert them to PNG using a specified method."""

    def __init__(self, conversion_method: str = "cairo"):
        """
        Initialize the processor and set up the conversion method.

        Args:
            conversion_method (str): The conversion method to use.
        """

        self.logger = LoggerManager().logger
        self.method = conversion_method
        self.converter = ConverterFactory.get_converter(self.method)
        self.tracer = Tracer(logger=self.logger)

    def process(self, input_file: str, output_file: str) -> str:
        """
        Process an SVG file and convert it to a PNG file.

        Args:
            input_file (str): Path to the input SVG file.
            output_file (str): Path to the output PNG file.

        Returns:
            str: Path to the output PNG file if successful.
        """

        @self.tracer.compute_execution_time
        def _process():
            try:
                result = self.converter.convert(input_file, output_file)
                self.logger.info(
                    f"Converted {input_file} to {output_file} using method '{self.method}'"
                )
                return result
            except Exception as e:
                self.logger.error(f"Failed to process SVG file '{input_file}': {e}")
                raise RuntimeError(
                    f"Failed to process SVG file '{input_file}' with method '{self.method}': {e}"
                )

        return _process()
