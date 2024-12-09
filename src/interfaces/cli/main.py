import argparse
import os
import sys

from dotenv import load_dotenv

from src.config.logs.logger import LoggerManager
from src.services.processor.svg_processor import SVGProcessor
from src.utils.config_loader import ConfigLoader
from src.utils.validator import SVGValidator

load_dotenv()
pythonpath = os.getenv("PYTHONPATH")
if pythonpath:
    sys.path.append(pythonpath)


def main():
    """Execute the e2e feature for transforming an SVG image to PNG format using CLI."""
    # Initialize logger
    logger_manager = LoggerManager()
    logger = logger_manager.logger

    # Load configuration
    config_loader = ConfigLoader()
    config = config_loader.load()
    method = config.get("svg_conversion", {}).get("default", "pdf")

    logger.info(f"Initializing application with default method: {method}")

    # Parse CLI arguments
    parser = argparse.ArgumentParser(description="Convert SVG to PNG.")
    parser.add_argument("--input", required=True, help="Path to the input SVG file.")
    parser.add_argument("--output", required=True, help="Path to the output PNG file.")
    args = parser.parse_args()

    # Perform all validations and preparations
    if not SVGValidator.prepare(args.input, args.output):
        logger.error("Validation failed. Exiting application.")
        return

    # Process the SVG file
    logger.info(f"Processing input file: {args.input} with output target: {args.output}")
    processor = SVGProcessor()

    try:
        output_path = processor.process(args.input, args.output)
        if output_path:
            logger.info(f"Conversion successful. Output saved at: {output_path}")
            print(f"PNG saved at: {output_path}")
        else:
            logger.error("Conversion failed during processing.")
            print("Conversion failed.")
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        print("An error occurred during processing. Check the logs for details.")


if __name__ == "__main__":
    main()
