#!/usr/bin/env python

"""
code that tests the Card and Deck class defined in cards.py

can be run with py.test
"""

import pytest  # used for the exception testing
import unittest

from cards import Card, Deck


class MyFuncTestCase(unittest.TestCase):

    def test_Card_num_suits(self):
        self.assertEqual(Card.num_suits(), 4)

    def test_Card_num_ranks(self):
        self.assertEqual(Card.num_ranks(), 13)

    def test_Card__init__(self):
        c1 = Card(0, 0)
        self.assertIsNotNone(c1)
        self.assertEqual(c1.rank, 0)
        self.assertEqual(c1.suit, 0)

        # intentionally reverse args
        c2 = Card(rank=0, suit=0)
        self.assertIsNotNone(c2)
        self.assertEqual(c2.rank, 0)
        self.assertEqual(c2.suit, 0)

        with self.assertRaises(IndexError):
            Card(rank=0, suit=4)
            Card(rank=13, suit=0)
            Card(rank=2, suit=-1)
            Card(rank=-1, suit=3)
            Card(rank=100, suit=100)

        with self.assertRaises(IndexError):
            Card(None, None)
            Card({0, 1}, {2, 3})
            Card([0, 1], [2, 3])
            Card((0, 1), (2, 3))
            Card(1.0, 2.0)
            Card("1.0", "2.0")

    def test_Card_check(self):
        c1 = Card(0, 0)
        self.assertEqual(c1, Card.check(c1))

        with self.assertRaises(ValueError):
            Card.check(None)
            Card.check(0)
            Card.check({0, 1})
            Card.check([0, 1])
            Card.check((0, 1))
            Card.check(1.0)
            Card.check("1.0")

    def test_Card__getitem__(self):
        c1 = Card(11, 1)
        self.assertEqual(c1.rank, 11)
        self.assertEqual(c1[0], 11)
        self.assertEqual(c1.suit, 1)
        self.assertEqual(c1[1], 1)

    def test_Card__setitem__(self):
        c1 = Card(2, 2)
        c1[0] = 1
        c1[1] = 3

        # key out of bound assigns suit.
        # item is not checked to be in bounds

    def test_Card__repr__(self):
        pass

    def test_Card__str__(self):
        pass

    def test_Card_value(self):
        pass

    def test_Deck__init__(self):
        d1 = Deck()
        self.assertEqual(len(d1.deck), 0)

    def test_Deck_init_FrenchDeck(self):
        pass

    def test_Deck_init_EuchreDeck(self):
        pass

    def test_Deck_init_PinochleDeck(self):
        pass

    def test_Deck___getitem__(self):
        pass

    def test_Deck___setitem__(self):
        pass

    def test_Deck___repr__(self):
        pass

    def test_Deck___str__(self):
        pass

    def test_Deck_remove_card(self):
        pass

    def test_Deck_append_card(self):
        pass

    def test_Deck_index_card(self):
        pass

    def test_Deck_deal_next_card(self):
        pass

    def test_Deck_shuffle(self):
        pass

if __name__ == "__main__":
    unittest.main()
