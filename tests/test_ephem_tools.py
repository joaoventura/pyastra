import unittest

from pyastra import const
from pyastra.datetime import Datetime
from pyastra.geopos import GeoPos
from pyastra.ephem import tools
from pyastra.ephem import ephem

VALUES = {
    const.SUN: {'lon': 352.790, 'lat': 0.000, 'sign': const.PISCES},
    const.MOON: {'lon': 262.381, 'lat': 5.029, 'sign': const.SAGITTARIUS},
    const.MERCURY: {'lon': 330.815, 'lat': -2.016, 'sign': const.PISCES},
    const.VENUS: {'lon': 25.503, 'lat': -0.101, 'sign': const.ARIES},
    const.NORTH_NODE: {'lon': 191.141, 'lat': 0.000, 'sign': const.LIBRA},
    const.SOUTH_NODE: {'lon': 11.141, 'lat': 0.000, 'sign': const.ARIES},
    const.PARS_FORTUNA: {'lon': 63.049, 'lat': 0.000, 'sign': const.GEMINI},
    const.SYZYGY: {'lon': 164.839, 'lat': -2.235, 'sign': const.VIRGO},

    const.HOUSE1: {'lon': 153.458, 'sign': const.VIRGO},
    const.HOUSE4: {'lon': 239.317, 'sign': const.SCORPIO},
    const.HOUSE7: {'lon': 333.458, 'sign': const.PISCES},
    const.HOUSE10: {'lon': 59.317, 'sign': const.TAURUS},

    const.ASC: {'lon': 153.458, 'sign': const.VIRGO},
    const.IC: {'lon': 239.317, 'sign': const.SCORPIO},
    const.DESC: {'lon': 333.458, 'sign': const.PISCES},
    const.MC: {'lon': 59.317, 'sign': const.TAURUS},
}


class BaseTest(unittest.TestCase):
    """Base for all tests."""

    def setUp(self):
        self.date = Datetime('2015/03/13', '17:00', '+00:00')
        self.pos = GeoPos('38n32', '8w54')


class ToolsTest(BaseTest):
    """Tests ephem tools."""

    def test_is_diurnal(self):
        is_diurnal = tools.is_diurnal(self.date.jd, self.pos.lat, self.pos.lon)
        self.assertEqual(is_diurnal, True)

    def test_is_not_diurnal(self):
        date = Datetime('2015/03/13', '23:00', '+00:00')
        is_diurnal = tools.is_diurnal(date.jd, self.pos.lat, self.pos.lon)
        self.assertEqual(is_diurnal, False)

    def test_next_station_mercury(self):
        ns = tools.next_station_jd(const.MERCURY, self.date.jd)
        self.assertAlmostEqual(ns, 2457161.708, 2)

    def test_next_station_venus(self):
        ns = tools.next_station_jd(const.VENUS, self.date.jd)
        self.assertAlmostEqual(ns, 2457229.208, 2)

    def test_next_station_mars(self):
        ns = tools.next_station_jd(const.MARS, self.date.jd)
        self.assertAlmostEqual(ns, 2457496.208, 2)

    def test_next_station_jupiter(self):
        ns = tools.next_station_jd(const.JUPITER, self.date.jd)
        self.assertAlmostEqual(ns, 2457121.208, 2)

    def test_next_station_saturn(self):
        ns = tools.next_station_jd(const.SATURN, self.date.jd)
        self.assertAlmostEqual(ns, 2457096.208, 2)

    def test_pars_fortuna_lon(self):
        pf_lon = tools.pf_lon(self.date.jd, self.pos.lat, self.pos.lon)
        self.assertAlmostEqual(pf_lon, 63.049, 2)

    def test_syzygy_jd(self):
        sz_jd = tools.syzygy_jd(self.date.jd)
        self.assertAlmostEqual(sz_jd, 2457087.253, 2)

    def test_solar_return_jd_backwards(self):
        sun = ephem.get_object(const.SUN, self.date, self.pos)
        sr_jd = tools.solar_return_jd(self.date.jd, sun.lon, forward=False)
        self.assertAlmostEqual(sr_jd, 2457095.208, 2)

    def test_solar_return_jd_forward(self):
        sun = ephem.get_object(const.SUN, self.date, self.pos)
        sr_jd = tools.solar_return_jd(self.date.jd, sun.lon, forward=True)
        self.assertAlmostEqual(sr_jd, 2457095.208, 2)
