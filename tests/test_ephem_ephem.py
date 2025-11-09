import unittest

from pyastra import const
from pyastra.ephem import ephem
from tests.fixtures.common import date, pos, VALUES


class BaseTest(unittest.TestCase):
    """Base for all ephem tests."""

    def setUp(self):
        self.date = date
        self.pos = pos

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