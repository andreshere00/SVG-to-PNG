import unittest
import os
from src.methods.svg2png_reportlab import ReportLabSVGConverter


class TestReportLabSVGConverter(unittest.TestCase):
    def test_convert(self):
        converter = ReportLabSVGConverter()
        input_file = "tests/assets/sample.svg"
        output_file = "tests/assets/sample_reportlab.png"

        # Ensure input file exists
        self.assertTrue(os.path.exists(input_file))

        # Test conversion
        result = converter.convert(input_file, output_file)
        self.assertTrue(result.endswith(".png"))
        self.assertTrue(os.path.exists(output_file))

        # Clean up
        os.remove(output_file)