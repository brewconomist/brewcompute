import unittest
import biab_eq as be


class TestBiabEq(unittest.TestCase):
    def setUp(self):
        self.exp_vol = 7.24
        self.exp_temp = 180

        self.grain_wt = 12.375
        self.batch_vol = 5

    def test_vol(self):
        vol = be.strike_water_vol(self.grain_wt, batch_vol=self.batch_vol)
        self.assertEqual(self.exp_vol, vol)

    def test_temp(self):
        temp = be.strike_water_temp(init_grain_temp=70,
                                    strike_water_vol=self.exp_vol,
                                    grain_wt=self.grain_wt)
        self.assertEqual(self.exp_temp, temp)
