# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, \
    division, print_function

import unittest
import geohash


class TestEncode(unittest.TestCase):

    def test_cycle(self):
        for code in ["000000000000", "zzzzzzzzzzzz", "bgr96qxvpd46", ]:
            self.assertEqual(code, geohash.encode(*geohash.decode(code)))

if __name__ == '__main__':
    unittest.main()
