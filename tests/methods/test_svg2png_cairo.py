import unittest

from src.methods.svg2png_cairo import CairoSVGConverter


class TestCairoSVGConverter(unittest.TestCase):
    def test_convert(self):
        converter = CairoSVGConverter()
        input_file = "tests/assets/sample.svg"
        output_file = "tests/assets/sample.png"
        result = converter.convert(input_file, output_file)
        self.assertTrue(result.endswith(".png"))
