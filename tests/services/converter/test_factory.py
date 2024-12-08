# tests/services/converter/test_factory.py

import unittest
from src.services.converter.svg_factory import ConverterFactory
from src.methods.svg2pdf2png import PDFToPNGConverter
from src.methods.svg2png_cairo import CairoSVGConverter
from src.methods.svg2png_inkscape import InkscapeSVGConverter
from src.methods.svg2png_reportlab import ReportLabSVGConverter


class TestConverterFactory(unittest.TestCase):
    def test_get_pdf_converter(self):
        converter = ConverterFactory.get_converter("pdf")
        self.assertIsInstance(converter, PDFToPNGConverter)

    def test_get_cairo_converter(self):
        converter = ConverterFactory.get_converter("cairo")
        self.assertIsInstance(converter, CairoSVGConverter)

    def test_get_inkscape_converter(self):
        converter = ConverterFactory.get_converter("inkscape")
        self.assertIsInstance(converter, InkscapeSVGConverter)

    def test_get_reportlab_converter(self):
        converter = ConverterFactory.get_converter("reportlab")
        self.assertIsInstance(converter, ReportLabSVGConverter)

    def test_invalid_method(self):
        with self.assertRaises(ValueError):
            ConverterFactory.get_converter("invalid")
