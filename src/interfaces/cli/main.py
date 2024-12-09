import os
import sys
import argparse
from dotenv import load_dotenv

from src.services.processor.svg_processor import SVGProcessor
from src.utils.validator import SVGValidator
from src.config.logs.logger import logger
from src.utils.config_loader import load_config

load_dotenv()
pythonpath = os.getenv("PYTHONPATH")
if pythonpath:
    sys.path.append(pythonpath)

def main():
    """
    Main function to execute the e2e feature for transforming a SVG image to PNG format using CLI.
    It does not take arguments since they are passed by Console. 
    """
    parser = argparse.ArgumentParser(description="Convert SVG to PNG.")
    parser.add_argument("--input", required=True, help="Path to the input SVG file.")
    parser.add_argument("--output", required=True, help="Path to the output PNG file.")
    args = parser.parse_args()

    # Load configuration
    config = load_config()
    method = config.get("default_method", "pdf")

    logger.info(f"Initializing application with default method: {method}")

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
