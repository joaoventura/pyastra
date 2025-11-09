import unittest

from pyastra import const
from pyastra.datetime import Datetime
from pyastra.geopos import GeoPos
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
    """Base for all ephem tests."""

    def setUp(self):
        self.date = Datetime('2015/03/13', '17:00', '+00:00')
        self.pos = GeoPos('38n32', '8w54')

    def _test_object(self, obj_id):
        """Tests an object."""
        obj = ephem.get_object(obj_id, self.date, self.pos)
        self.assertAlmostEqual(obj.lon, VALUES[obj_id]['lon'], 2)
        self.assertAlmostEqual(obj.lat, VALUES[obj_id]['lat'], 2)
        self.assertEqual(obj.sign, VALUES[obj_id]['sign'])

    def _test_house(self, house_id):
        """Tests a house."""
        houses, angles = ephem.get_houses(self.date, self.pos, const.HOUSES_ALCABITUS)
        house = houses.get(house_id)
        self.assertAlmostEqual(house.lon, VALUES[house_id]['lon'], 2)
        self.assertEqual(house.sign, VALUES[house_id]['sign'])

    def _test_angle(self, obj_id):
        """Tests an angle."""
        houses, angles = ephem.get_houses(self.date, self.pos, const.HOUSES_ALCABITUS)
        angle = angles.get(obj_id)
        self.assertAlmostEqual(angle.lon, VALUES[obj_id]['lon'], 2)
        self.assertEqual(angle.sign, VALUES[obj_id]['sign'])


class ObjectTest(BaseTest):
    """Tests object."""

    def test_sun(self):
        self._test_object(const.SUN)

    def test_moon(self):
        self._test_object(const.MOON)

    def test_mercury(self):
        self._test_object(const.MERCURY)

    def test_venus(self):
        self._test_object(const.VENUS)

    def test_north_node(self):
        self._test_object(const.NORTH_NODE)

    def test_south_node(self):
        self._test_object(const.SOUTH_NODE)

    def test_pars_fortuna(self):
        self._test_object(const.PARS_FORTUNA)

    def test_syzygy(self):
        self._test_object(const.SYZYGY)


class HouseTest(BaseTest):
    """Tests houses."""

    def test_house1(self):
        self._test_house(const.HOUSE1)

    def test_house4(self):
        self._test_house(const.HOUSE4)

    def test_house7(self):
        self._test_house(const.HOUSE7)

    def test_house10(self):
        self._test_house(const.HOUSE10)


class AngleTest(BaseTest):
    """Tests the angles."""

    def test_asc(self):
        self._test_angle(const.ASC)

    def test_ic(self):
        self._test_angle(const.IC)

    def test_desc(self):
        self._test_angle(const.DESC)

    def test_mc(self):
        self._test_angle(const.MC)