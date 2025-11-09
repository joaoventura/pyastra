import unittest

from pyastra import const
from pyastra.datetime import Datetime
from pyastra.geopos import GeoPos
from pyastra.ephem import swe


VALUES = {
    const.SUN: {'lon': 352.790, 'lat': 0.000},
    const.MOON: {'lon': 262.381, 'lat': 5.029},
    const.HOUSE1: {'lon': 153.458},
    const.HOUSE10: {'lon': 59.317},
    const.ASC: {'lon': 153.458},
    const.MC: {'lon': 59.317},
}

class SweTests(unittest.TestCase):

    def setUp(self):
        self.date = Datetime('2015/03/13', '17:00', '+00:00')
        self.pos = GeoPos('38n32', '8w54')

    def test_sun_position(self):
        lon, lat, lon_speed, lat_speed = swe.swe_object_raw(const.SUN, self.date.jd)
        self.assertAlmostEqual(lon, VALUES[const.SUN]['lon'], 2)
        self.assertAlmostEqual(lat, VALUES[const.SUN]['lat'], 2)

    def test_moon_position(self):
        lon, lat, lon_speed, lat_speed = swe.swe_object_raw(const.MOON, self.date.jd)
        self.assertAlmostEqual(lon, VALUES[const.MOON]['lon'], 2)
        self.assertAlmostEqual(lat, VALUES[const.MOON]['lat'], 2)

    def test_house1_position(self):
        cusps, _ = swe.swe_houses_raw(self.date.jd, self.pos.lat,
                                      self.pos.lon, const.HOUSES_ALCABITUS)
        self.assertAlmostEqual(cusps[0], VALUES[const.HOUSE1]['lon'], 2)

    def test_house10_position(self):
        cusps, _ = swe.swe_houses_raw(self.date.jd, self.pos.lat,
                                      self.pos.lon, const.HOUSES_ALCABITUS)
        self.assertAlmostEqual(cusps[9], VALUES[const.HOUSE10]['lon'], 2)

    def test_asc_position(self):
        cusps, ascmc = swe.swe_houses_raw(self.date.jd, self.pos.lat,
                                      self.pos.lon, const.HOUSES_ALCABITUS)
        self.assertAlmostEqual(ascmc[0], VALUES[const.ASC]['lon'], 2)

    def test_mc_position(self):
        cusps, ascmc = swe.swe_houses_raw(self.date.jd, self.pos.lat,
                                      self.pos.lon, const.HOUSES_ALCABITUS)
        self.assertAlmostEqual(ascmc[1], VALUES[const.MC]['lon'], 2)
