#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# © 2024 Nils Dagsson Moskopp <nils.moskopp@grandcentrix.net>

from logging import warning
from mypy.api import run as mypy_api_run

import pycodestyle
import unittest


class TestTyping(unittest.TestCase):
    def test_static_typing(self) -> None:
        """Test that typing is correct according to mypy."""
        normal_report, error_report, exit_status = mypy_api_run(
            [
                '--ignore-missing-imports',
                '--strict',
                __file__,
            ]
        )
        self.assertEqual(
            exit_status,
            0,
            normal_report
        )


class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self) -> None:
        """Test that code is formatted according to PEP8."""
        style = pycodestyle.StyleGuide()
        result = style.check_files([__file__])
        self.assertEqual(
            result.total_errors,
            0,
        )


if __name__ == '__main__':
    unittest.main(exit=False)
