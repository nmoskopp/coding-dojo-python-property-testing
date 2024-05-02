#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# © 2024 Nils Dagsson Moskopp <nils.moskopp@grandcentrix.net>

from copy import deepcopy
from hypothesis import assume, given, strategies
from logging import warning
from mypy.api import run as mypy_api_run
from typing import TypedDict

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


class MoneyStash(TypedDict):
    _5: int
    _10: int
    _20: int
    _50: int
    _100: int


class ATM:
    def __init__(self, stash: MoneyStash):
        self.stash = stash

    def withdraw_all(self) -> MoneyStash:
        result = deepcopy(self.stash)
        self.stash = {
            '_5': 0,
            '_10': 0,
            '_20': 0,
            '_50': 0,
            '_100': 0,
        }
        return result


@given(
    _5=strategies.integers(),
    _10=strategies.integers(),
    _20=strategies.integers(),
    _50=strategies.integers(),
    _100=strategies.integers(),
)
def test_withdrawing_all_money(
        _5: int,
        _10: int,
        _20: int,
        _50: int,
        _100: int,
) -> None:
    assume(_5 >= 0)
    assume(_10 >= 0)
    assume(_20 >= 0)
    assume(_50 >= 0)
    assume(_100 >= 0)
    banknotes: MoneyStash = {
        '_5': _5,
        '_10': _10,
        '_20': _20,
        '_50': _50,
        '_100': _100,
    }

    atm = ATM(banknotes)
    money = atm.withdraw_all()
    assert money['_5'] == _5
    assert money['_10'] == _10
    assert money['_20'] == _20
    assert money['_50'] == _50
    assert money['_100'] == _100


if __name__ == '__main__':
    unittest.main(exit=False)
