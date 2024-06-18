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
        self.stash['_50'] += deposited_stash['_50']
        self.stash['_100'] += deposited_stash['_100']


@strategies.composite
def banknotes_strategy(draw) -> MoneyStash:
    positive_integer = strategies.integers(min_value=0)
    _5 = draw(positive_integer)
    _10 = draw(positive_integer)
    _20 = draw(positive_integer)
    _50 = draw(positive_integer)
    _100 = draw(positive_integer)
    assume(_5 + _10 + _20 + _50 + _100 > 1)
    banknotes: MoneyStash = {
        '_5': _5,
        '_10': _10,
        '_20': _20,
        '_50': _50,
        '_100': _100,
    }
    return banknotes


class TestATM(unittest.TestCase):
    @given(banknotes=banknotes_strategy())
    def test_depositing_money(
            self,
            banknotes,
    ) -> None:
        atm = ATM()
        atm.deposit(banknotes)
        self.assertEqual(atm.stash['_5'], banknotes['_5'])
        self.assertEqual(atm.stash['_10'], banknotes['_10'])
        self.assertEqual(atm.stash['_20'], banknotes['_20'])
        self.assertEqual(atm.stash['_50'], banknotes['_50'])
        self.assertEqual(atm.stash['_100'], banknotes['_100'])


if __name__ == '__main__':
    unittest.main(exit=False)
