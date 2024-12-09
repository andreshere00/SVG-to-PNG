import os
from xml.etree import ElementTree


class SVGValidator:
    """Class to handle SVG validation and output directory management."""

    @staticmethod
    def validate_svg(file_path: str) -> bool:
        """
        Validate if the provided file is a valid SVG.

        Args:
            file_path (str): Path to the SVG file.

        Returns:
            bool: True if the SVG file is valid, False otherwise.
        """
        try:
            tree = ElementTree.parse(file_path)
            root = tree.getroot()
            return root.tag == "{http://www.w3.org/2000/svg}svg"
        except Exception as e:
            print(f"Invalid SVG file: {e}")
            return False

    @staticmethod
    def ensure_directory_exists(path: str) -> None:
        """
        Ensure the directory for the output file exists.

        Args:
            path (str): Path to the output file.
        """
        os.makedirs(os.path.dirname(path), exist_ok=True)

    @staticmethod
    def prepare(input_file: str, output_file: str) -> bool:
        """
        Perform all validation and preparation steps.

        Args:
            input_file (str): Path to the input SVG file.
            output_file (str): Path to the output PNG file.

        Returns:
            bool: True if the preparation is successful, False otherwise.
        """
        if not SVGValidator.validate_svg(input_file):
            print("Invalid input SVG file. Please provide a valid SVG file.")
            return False

        SVGValidator.ensure_directory_exists(output_file)
        return True
