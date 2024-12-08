import unittest
from src.methods.svg2pdf2png import PDFToPNGConverter

class TestPDFToPNGConverter(unittest.TestCase):

    def test_convert(self):
        converter = PDFToPNGConverter()
        svg_file = "tests/assets/sample.svg"
        output_file = "tests/assets/output.png"
        result = converter.convert(svg_file, output_file)
        self.assertTrue(result.endswith(".png"))
