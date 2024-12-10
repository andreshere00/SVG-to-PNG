import os

from src.config.logs.logger import LoggerManager
from src.services.converter.svg_factory import ConverterFactory
from src.utils.config_loader import ConfigLoader
from src.utils.tracer import Tracer


class SVGProcessor:
    """Main class to process SVG files and convert them to PNG using a specified method."""

    def __init__(self, converter=None):
        """Initialize the processor and set up the conversion method."""

        # Initialize configuration and logger
        config_loader = ConfigLoader()
        self.config = config_loader.load()
        logger_manager = LoggerManager()
        self.logger = logger_manager.logger

        # Get method and trace folder from the configuration
        self.method = self.config.get("svg_conversion", {}).get("methods", "cairo")
        self.trace_folder = self.config.get("logging", {}).get("output_folder", "./logs")
        os.makedirs(self.trace_folder, exist_ok=True)

        self.converter = converter or ConverterFactory.get_converter(self.method)

    @Tracer.compute_execution_time
    def process(self, input_file: str, output_file: str) -> str:
        """
        Process an SVG file and convert it to a PNG file.

        Args:
            input_file (str): Path to the input SVG file.
            output_file (str): Path to the output PNG file.

        Returns:
            str: Path to the output PNG file if successful.
        """

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
