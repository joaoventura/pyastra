import unittest

from pyastra import const
from pyastra.context import ChartContext
from pyastra.ephem import swe
from tests.fixtures.common import date, pos, VALUES_TROPICAL, VALUES_SIDEREAL_FAGAN_BRADLEY


class SweTropicalTests(unittest.TestCase):

    def setUp(self):
        self.context = ChartContext(jd=date.jd, lat=pos.lat, lon=pos.lon)
        self.expected = VALUES_TROPICAL

    def test_sun_position(self):
        lon, lat, lon_speed, lat_speed = swe.swe_object(const.SUN, context=self.context)
        self.assertAlmostEqual(lon, self.expected[const.SUN]['lon'], 2)
        self.assertAlmostEqual(lat, self.expected[const.SUN]['lat'], 2)

    def test_moon_position(self):
        lon, lat, lon_speed, lat_speed = swe.swe_object(const.MOON, context=self.context)
        self.assertAlmostEqual(lon, self.expected[const.MOON]['lon'], 2)
        self.assertAlmostEqual(lat, self.expected[const.MOON]['lat'], 2)

    def test_house1_position(self):
        cusps, _ = swe.swe_houses(context=self.context)
        self.assertAlmostEqual(cusps[0], self.expected[const.HOUSE1]['lon'], 2)

    def test_house10_position(self):
        cusps, _ = swe.swe_houses(context=self.context)
        self.assertAlmostEqual(cusps[9], self.expected[const.HOUSE10]['lon'], 2)

    def test_asc_position(self):
        cusps, ascmc = swe.swe_houses(context=self.context)
        self.assertAlmostEqual(ascmc[0], self.expected[const.ASC]['lon'], 2)

    def test_mc_position(self):
        cusps, ascmc = swe.swe_houses(context=self.context)
        self.assertAlmostEqual(ascmc[1], self.expected[const.MC]['lon'], 2)

    def test_sirius_position(self):
        mag, lon, lat = swe.swe_fixed_star(const.STAR_SIRIUS, context=self.context)
        self.assertAlmostEqual(lon, self.expected[const.STAR_SIRIUS]['lon'], 2)

    def test_regulus_position(self):
        mag, lon, lat = swe.swe_fixed_star(const.STAR_REGULUS, context=self.context)
        self.assertAlmostEqual(lon, self.expected[const.STAR_REGULUS]['lon'], 2)


class SweSiderealTests(unittest.TestCase):

    def setUp(self):
        self.context = ChartContext(
            jd=date.jd,
            lat=pos.lat,
            lon=pos.lon,
            zodiac=const.ZODIAC_SIDEREAL,
            ayanamsa=const.AYANANMSA_FAGAN_BRADLEY
        )
        self.expected = VALUES_SIDEREAL_FAGAN_BRADLEY

    def test_sun_position(self):
        lon, lat, lon_speed, lat_speed = swe.swe_object(const.SUN, context=self.context)
        self.assertAlmostEqual(lon, self.expected[const.SUN]['lon'], 2)
        self.assertAlmostEqual(lat, self.expected[const.SUN]['lat'], 2)

    def test_moon_position(self):
        lon, lat, lon_speed, lat_speed = swe.swe_object(const.MOON, context=self.context)
        self.assertAlmostEqual(lon, self.expected[const.MOON]['lon'], 2)
        self.assertAlmostEqual(lat, self.expected[const.MOON]['lat'], 2)
