#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# © 2024 Nils Dagsson Moskopp <nils.moskopp@grandcentrix.net>

from hypothesis import assume, given, strategies
from typing import TypedDict

import unittest


class MoneyStash(TypedDict):
    _5: int
    _10: int
    _20: int
    _50: int
    _100: int


class ATM:
    def __init__(self) -> None:
        self.stash: MoneyStash = {
            '_5': 0,
            '_10': 0,
            '_20': 0,
            '_50': 0,
            '_100': 0,
        }

    def deposit(self, deposited_stash: MoneyStash) -> None:
        self.stash['_5'] += deposited_stash['_5']
        self.stash['_10'] += deposited_stash['_10']
        self.stash['_20'] += deposited_stash['_20']
        self.stash['_50'] += deposited_stash['_5']
        self.stash['_100'] += deposited_stash['_100']


class TestATM(unittest.TestCase):
    @given(
        _5=strategies.integers(min_value=0),
        _10=strategies.integers(min_value=0),
        _20=strategies.integers(min_value=0),
        _50=strategies.integers(min_value=0),
        _100=strategies.integers(min_value=0),
    )
    def test_depositing_money(
            self,
            _5: int,
            _10: int,
            _20: int,
            _50: int,
            _100: int,
    ) -> None:
        # Assume we have a positive amount of each banknote
        assume(_5 > 0)
        assume(_10 > 0)
        assume(_20 > 0)
        assume(_50 > 0)
        assume(_100 > 0)
        banknotes: MoneyStash = {
            '_5': _5,
            '_10': _10,
            '_20': _20,
            '_50': _50,
            '_100': _100,
        }

        atm = ATM()
        atm.deposit(banknotes)
        self.assertEqual(atm.stash['_5'], _5)
        self.assertEqual(atm.stash['_10'], _10)
        self.assertEqual(atm.stash['_20'], _20)
        self.assertEqual(atm.stash['_50'], _50)
        self.assertEqual(atm.stash['_100'], _100)


if __name__ == '__main__':
    unittest.main(exit=False)
