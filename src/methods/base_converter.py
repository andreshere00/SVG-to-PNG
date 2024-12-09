from abc import ABC, abstractmethod
from typing import Optional


class BaseConverter(ABC):
    """Abstract base class for all SVG-to-PNG converters."""

    @abstractmethod
    def convert(self, svg_file: str, output_file: str) -> Optional[str]:
        """
        Convert an SVG file to a PNG file.

        Args:
            svg_file (str): Path to the input SVG file.
            output_file (str): Path to the output PNG file.

        Returns:
            Optional[str]: Path to the converted PNG file or None if failed.
        """
