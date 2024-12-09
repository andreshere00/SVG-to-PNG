import os
import unittest

from src.utils.validator import SVGValidator


class TestSVGValidator(unittest.TestCase):

    def test_validate_valid_svg(self):
        valid_svg = """<?xml version="1.0"?>
        <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
            <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
        </svg>"""
        with open("valid_test.svg", "w") as f:
            f.write(valid_svg)

        self.assertTrue(SVGValidator.validate_svg("valid_test.svg"))
        os.remove("valid_test.svg")

    def test_validate_invalid_svg(self):
        invalid_svg = """<not_svg></not_svg>"""
        with open("invalid_test.svg", "w") as f:
            f.write(invalid_svg)

        self.assertFalse(SVGValidator.validate_svg("invalid_test.svg"))
        os.remove("invalid_test.svg")

    def test_ensure_directory_exists(self):
        path = "temp_dir/test_file.png"
        SVGValidator.ensure_directory_exists(path)
        self.assertTrue(os.path.exists("temp_dir"))
        os.rmdir("temp_dir")  # Clean up
