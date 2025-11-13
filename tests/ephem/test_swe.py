import unittest

from pyastra import const
from pyastra.ephem import swe
from tests.fixtures.common import date, pos, VALUES


class SweTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_sun_position(self):
        lon, lat, lon_speed, lat_speed = swe.swe_object(const.SUN, date.jd)
        self.assertAlmostEqual(lon, VALUES[const.SUN]['lon'], 2)
        self.assertAlmostEqual(lat, VALUES[const.SUN]['lat'], 2)

    def test_moon_position(self):
        lon, lat, lon_speed, lat_speed = swe.swe_object(const.MOON, date.jd)
        self.assertAlmostEqual(lon, VALUES[const.MOON]['lon'], 2)
        self.assertAlmostEqual(lat, VALUES[const.MOON]['lat'], 2)

    def test_house1_position(self):
        cusps, _ = swe.swe_houses(date.jd, pos.lat, pos.lon, const.HOUSES_ALCABITUS)
        self.assertAlmostEqual(cusps[0], VALUES[const.HOUSE1]['lon'], 2)

    def test_house10_position(self):
        cusps, _ = swe.swe_houses(date.jd, pos.lat, pos.lon, const.HOUSES_ALCABITUS)
        self.assertAlmostEqual(cusps[9], VALUES[const.HOUSE10]['lon'], 2)

    def test_asc_position(self):
        cusps, ascmc = swe.swe_houses(date.jd, pos.lat, pos.lon, const.HOUSES_ALCABITUS)
        self.assertAlmostEqual(ascmc[0], VALUES[const.ASC]['lon'], 2)

    def test_mc_position(self):
        cusps, ascmc = swe.swe_houses(date.jd, pos.lat, pos.lon, const.HOUSES_ALCABITUS)
        self.assertAlmostEqual(ascmc[1], VALUES[const.MC]['lon'], 2)

    def test_sirius_position(self):
        mag, lon, lat = swe.swe_fixed_star(const.STAR_SIRIUS, date.jd)
        self.assertAlmostEqual(lon, VALUES[const.STAR_SIRIUS]['lon'], 2)

    def test_regulus_position(self):
        mag, lon, lat = swe.swe_fixed_star(const.STAR_REGULUS, date.jd)
        self.assertAlmostEqual(lon, VALUES[const.STAR_REGULUS]['lon'], 2)
