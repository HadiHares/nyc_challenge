import unittest
from avgdrive.nycavg import calcavg_month, roll_avg


class TestNycAvg(unittest.TestCase):

    def test_init(self):
        avgmonth = calcavg_month(year=2020, month=1)
        self.assertEqual(avgmonth, 2.93)

    def test_roll(self):
        roll45 = roll_avg(2020, 1, 3)
        self.assertEqual(round(roll45.mean(), 2), 2.72)


if __name__ == "__main__":
    unittest.main()
