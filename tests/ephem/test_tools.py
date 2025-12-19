import unittest

from pyastra import const
from pyastra.context import ChartContext
from pyastra.core.datetime import Datetime
from pyastra.ephem import tools
from pyastra.ephem import ephem
from tests.fixtures.common import date, pos, VALUES_TROPICAL, VALUES_SIDEREAL_FAGAN_BRADLEY


class BaseTest(unittest.TestCase):
    """Base for all tests."""

    __test__ = False
    context = None
    expected = None

    def test_is_diurnal(self):
        is_diurnal = tools.is_diurnal(self.context)
        self.assertEqual(is_diurnal, True)

    def test_is_not_diurnal(self):
        date = Datetime('2015/03/13', '23:00', '+00:00')
        context = ChartContext(jd=date.jd, lat=pos.lat, lon=pos.lon)
        is_diurnal = tools.is_diurnal(context)
        self.assertEqual(is_diurnal, False)

    def test_next_station_sun(self):
        expected = tools.find_next_station(const.SUN, self.context.jd)
        self.assertIsNone(expected)

    def test_next_station_moon(self):
        expected = tools.find_next_station(const.MOON, self.context.jd)
        self.assertIsNone(expected)

    def test_next_station_mercury(self):
        station_jd, station_type = tools.find_next_station(const.MERCURY, self.context.jd)
        self.assertAlmostEqual(station_jd, 2457161.708, 2)

    def test_next_station_venus(self):
        station_jd, station_type = tools.find_next_station(const.VENUS, self.context.jd)
        self.assertAlmostEqual(station_jd, 2457229.208, 2)

    def test_next_station_mars(self):
        station_jd, station_type = tools.find_next_station(const.MARS, self.context.jd)
        self.assertAlmostEqual(station_jd, 2457496.208, 2)

    def test_next_station_jupiter(self):
        station_jd, station_type = tools.find_next_station(const.JUPITER, self.context.jd)
        self.assertAlmostEqual(station_jd, 2457121.208, 2)

    def test_next_station_saturn(self):
        station_jd, station_type = tools.find_next_station(const.SATURN, self.context.jd)
        self.assertAlmostEqual(station_jd, 2457096.208, 2)

    def test_pars_fortuna_lon(self):
        pf_lon = tools.pars_fortuna_lon(self.context)
        self.assertAlmostEqual(pf_lon, self.expected[const.PARS_FORTUNA]['lon'], 2)

    def test_syzygy_jd(self):
        sz_jd = tools.syzygy_jd(self.context.jd)
        self.assertAlmostEqual(sz_jd, 2457087.253, 2)

    def test_solar_return_jd_backwards(self):
        """It should take -10 days to find the sun where it was approximately 10 days ago."""
        sun = ephem.get_object(const.SUN, context=self.context)
        sr_jd = tools.solar_return_jd(sun.lon - 10, self.context, forward=False)
        self.assertAlmostEqual(sr_jd, self.context.jd - 10, 1)

    def test_solar_return_jd_forward(self):
        """It should take 10 days to find the sun where it will be approximately in 10 days."""
        sun = ephem.get_object(const.SUN, context=self.context)
        sr_jd = tools.solar_return_jd(sun.lon + 10, self.context, forward=True)
        self.assertAlmostEqual(sr_jd, self.context.jd + 10, 1)


class ToolsTestTropicalZodiac(BaseTest):
    """Tests ephem tools for tropical zodiac."""

    __test__ = True
    context = ChartContext(
        jd=date.jd,
        lon=pos.lon,
        lat=pos.lat
    )
    expected = VALUES_TROPICAL


class ToolsTestSiderealZodiac(BaseTest):
    """Tests ephem tools for sideral zodiac."""

    __test__ = True
    context = ChartContext(
        jd=date.jd,
        lon=pos.lon,
        lat=pos.lat,
        zodiac=const.ZODIAC_SIDEREAL,
        ayanamsa=const.AYANANMSA_FAGAN_BRADLEY
    )
    expected = VALUES_SIDEREAL_FAGAN_BRADLEY
