import unittest
import biab_eq as be


class TestBiabEq(unittest.TestCase):
    def setUp(self):
        self.exp_vol = 7.24
        self.exp_temp = 160.09

        self.grain_wt = 12.375
        self.postboil_vol = 5
        self.target_mash_temp = 152

        self.exp_preboil_grav = 1.034

    def test_vol(self):
        vol = be.strike_water_vol(self.grain_wt,
                                  postboil_vol=self.postboil_vol)
        self.assertAlmostEqual(self.exp_vol, vol, places=2)

    def test_temp(self):
        temp = be.strike_water_temp(init_grain_temp=70,
                                    strike_water_vol=self.exp_vol,
                                    grain_wt=self.grain_wt,
                                    target_mash_temp=self.target_mash_temp)
        self.assertAlmostEqual(self.exp_temp, temp, places=2)

    def test_grav(self):
        grav = be.preboil_grav(target_og=1.040)
        self.assertAlmostEqual(self.exp_preboil_grav, grav, places=3)
