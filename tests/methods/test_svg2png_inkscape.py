import unittest
from src.methods.svg2png_inkscape import InkscapeSVGConverter
import os
import shutil

class TestInkscapeSVGConverter(unittest.TestCase):
    def test_inkscape_cli_missing(self):
        # Temporarily remove Inkscape from PATH for testing
        original_path = shutil.which("inkscape")
        if original_path:
            os.environ["PATH"] = os.environ["PATH"].replace(os.path.dirname(original_path), "")

        with self.assertRaises(RuntimeError):
            InkscapeSVGConverter()

        # Restore original PATH
        if original_path:
            os.environ["PATH"] += f":{os.path.dirname(original_path)}"

    def test_convert(self):
        converter = InkscapeSVGConverter()
        input_file = "./tests/assets/sample.svg"
        output_file = "./tests/assets/sample.png"

        # Ensure input file exists
        self.assertTrue(os.path.exists(input_file))

        # Test the conversion
        result = converter.convert(input_file, output_file)
        self.assertTrue(result.endswith(".png"))
        self.assertTrue(os.path.exists(output_file))

        # Cleanup
        if os.path.exists(output_file):
            os.remove(output_file)