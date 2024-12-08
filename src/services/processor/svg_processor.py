import os
from src.services.converter.svg_factory import ConverterFactory
from src.utils.config_loader import load_config
from src.utils.tracer import compute_execution_time
from src.config.logs.logger import logger

class SVGProcessor:
    """
    Main class to process SVG files and convert them to PNG using a specified method.
    """

    def __init__(self, converter=None):
        """
        Initialize the processor and set up the conversion method.
        """
        config = load_config()
        self.method = config.get("default_method", "pdf")
        self.trace_folder = config.get("trace_folder", "./logs")
        os.makedirs(self.trace_folder, exist_ok=True)
        self.converter = converter or ConverterFactory.get_converter(self.method)

    @compute_execution_time()
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
            return self.converter.convert(input_file, output_file)
        except Exception as e:
            logger.error(f"Failed to process SVG file: {e}")
            return None
