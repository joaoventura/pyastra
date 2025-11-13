import unittest

from pyastra import const
from pyastra.context import ChartContext
from pyastra.datetime import Datetime
from pyastra.ephem import tools
from pyastra.ephem import ephem
from tests.fixtures.common import date, pos, VALUES_TROPICAL


class BaseTest(unittest.TestCase):
    """Base for all tests."""

    def setUp(self):
        self.date = date
        self.pos = pos
        self.context = ChartContext(
            jd=self.date.jd,
            lon=self.pos.lon,
            lat=self.pos.lat
        )


class ToolsTest(BaseTest):
    """Tests ephem tools."""

    def test_is_diurnal(self):
        is_diurnal = tools.is_diurnal(self.context)
        self.assertEqual(is_diurnal, True)

    def test_is_not_diurnal(self):
        date = Datetime('2015/03/13', '23:00', '+00:00')
        context = ChartContext(jd=date.jd, lat=pos.lat, lon=pos.lon)
        is_diurnal = tools.is_diurnal(context)
        self.assertEqual(is_diurnal, False)

    def test_next_station_sun(self):
        expected = tools.find_next_station(const.SUN, self.date.jd)
        self.assertIsNone(expected)

    def test_next_station_moon(self):
        expected = tools.find_next_station(const.MOON, self.date.jd)
        self.assertIsNone(expected)

    def test_next_station_mercury(self):
        station_jd, station_type = tools.find_next_station(const.MERCURY, self.date.jd)
        self.assertAlmostEqual(station_jd, 2457161.708, 2)

    def test_next_station_venus(self):
        station_jd, station_type = tools.find_next_station(const.VENUS, self.date.jd)
        self.assertAlmostEqual(station_jd, 2457229.208, 2)

    def test_next_station_mars(self):
        station_jd, station_type = tools.find_next_station(const.MARS, self.date.jd)
        self.assertAlmostEqual(station_jd, 2457496.208, 2)

    def test_next_station_jupiter(self):
        station_jd, station_type = tools.find_next_station(const.JUPITER, self.date.jd)
        self.assertAlmostEqual(station_jd, 2457121.208, 2)

    def test_next_station_saturn(self):
        station_jd, station_type = tools.find_next_station(const.SATURN, self.date.jd)
        self.assertAlmostEqual(station_jd, 2457096.208, 2)

    def test_pars_fortuna_lon(self):
        pf_lon = tools.pars_fortuna_lon(self.context)
        self.assertAlmostEqual(pf_lon, 63.049, 2)

    def test_syzygy_jd(self):
        sz_jd = tools.syzygy_jd(self.date.jd)
        self.assertAlmostEqual(sz_jd, 2457087.253, 2)

    def test_solar_return_jd_backwards(self):
        sun = ephem.get_object(const.SUN, context=self.context)
        sr_jd = tools.solar_return_jd(self.date.jd, sun.lon, forward=False)
        self.assertAlmostEqual(sr_jd, 2457095.208, 2)

    def test_solar_return_jd_forward(self):
        sun = ephem.get_object(const.SUN, context=self.context)
        sr_jd = tools.solar_return_jd(self.date.jd, sun.lon, forward=True)
        self.assertAlmostEqual(sr_jd, 2457095.208, 2)
