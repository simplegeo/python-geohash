import unittest
import geohash

class TestEncode(unittest.TestCase):
    def test_example(self):
        self.assertEqual('bgr96qxvpd46', geohash.encode(63.537551615736049, -135.59328029278211))
	
if __name__=='__main__':
    unittest.main()
