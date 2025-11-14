import unittest

from pyastra import const
from pyastra.context import ChartContext
from pyastra.ephem import ephem
from tests.fixtures.common import (date, pos, VALUES_TROPICAL, VALUES_SIDEREAL_FAGAN_BRADLEY,
                                   VALUES_SIDEREAL_LAHIRI)


class BaseTest(unittest.TestCase):
    """Base for all ephem tests."""
    context = None
    expected = None

    def _test_object(self, obj_id):
        """Tests an object."""
        obj = ephem.get_object(obj_id, context=self.context)
        self.assertAlmostEqual(obj.lon, self.expected[obj_id]['lon'], 2)
        self.assertAlmostEqual(obj.lonspeed, self.expected[obj_id]['lon_speed'], 2)
        self.assertAlmostEqual(obj.lat, self.expected[obj_id]['lat'], 2)
        self.assertAlmostEqual(obj.latspeed, self.expected[obj_id]['lat_speed'], 2)
        self.assertEqual(obj.sign, self.expected[obj_id]['sign'])

    def _test_house(self, house_id):
        """Tests a house."""
        houses = ephem.get_houses(context=self.context)
        house = houses.get(house_id)
        self.assertAlmostEqual(house.lon, self.expected[house_id]['lon'], 2)
        self.assertAlmostEqual(house.size, self.expected[house_id]['size'], 2)
        self.assertEqual(house.sign, self.expected[house_id]['sign'])

    def _test_angle(self, obj_id):
        """Tests an angle."""
        angles = ephem.get_angles(context=self.context)
        angle = angles.get(obj_id)
        self.assertAlmostEqual(angle.lon, self.expected[obj_id]['lon'], 2)
        self.assertEqual(angle.sign, self.expected[obj_id]['sign'])

    def _test_fixed_star(self, obj_id):
        """Tests a fixed star."""
        obj = ephem.get_fixed_star(obj_id, context=self.context)
        self.assertAlmostEqual(obj.mag, self.expected[obj_id]['mag'], 2)
        self.assertAlmostEqual(obj.lon, self.expected[obj_id]['lon'], 2)
        self.assertAlmostEqual(obj.lat, self.expected[obj_id]['lat'], 2)
        self.assertEqual(obj.sign, self.expected[obj_id]['sign'])


class BaseTestTropicalZodiac(BaseTest):
    __test__ = False
    context = ChartContext(
        jd=date.jd,
        lon=pos.lon,
        lat=pos.lat
    )
    expected = VALUES_TROPICAL


class BaseTestSiderealZodiacFaganBradley(BaseTest):
    __test__ = False
    context = ChartContext(
        jd=date.jd,
        lon=pos.lon,
        lat=pos.lat,
        zodiac=const.ZODIAC_SIDEREAL,
        ayanamsa=const.AYANANMSA_FAGAN_BRADLEY
    )
    expected = VALUES_SIDEREAL_FAGAN_BRADLEY


class BaseTestSiderealZodiacLahiri(BaseTest):
    __test__ = False
    context = ChartContext(
        jd=date.jd,
        lon=pos.lon,
        lat=pos.lat,
        zodiac=const.ZODIAC_SIDEREAL,
        ayanamsa=const.AYANANMSA_LAHIRI
    )
    expected = VALUES_SIDEREAL_LAHIRI


class ObjectTest(BaseTest):
    """Tests objects."""
    __test__ = False

    def test_sun(self):
        self._test_object(const.SUN)

    def test_moon(self):
        self._test_object(const.MOON)

    def test_mercury(self):
        self._test_object(const.MERCURY)

    def test_venus(self):
        self._test_object(const.VENUS)

    def test_mars(self):
        self._test_object(const.MARS)

    def test_jupiter(self):
        self._test_object(const.JUPITER)

    def test_saturn(self):
        self._test_object(const.SATURN)

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
    __test__ = False

    def test_house1(self):
        self._test_house(const.HOUSE1)

    def test_house2(self):
        self._test_house(const.HOUSE2)

    def test_house3(self):
        self._test_house(const.HOUSE3)

    def test_house4(self):
        self._test_house(const.HOUSE4)

    def test_house5(self):
        self._test_house(const.HOUSE5)

    def test_house6(self):
        self._test_house(const.HOUSE7)

    def test_house7(self):
        self._test_house(const.HOUSE7)

    def test_house8(self):
        self._test_house(const.HOUSE8)

    def test_house9(self):
        self._test_house(const.HOUSE9)

    def test_house10(self):
        self._test_house(const.HOUSE10)

    def test_house11(self):
        self._test_house(const.HOUSE11)

    def test_house12(self):
        self._test_house(const.HOUSE12)


class AngleTest(BaseTest):
    """Tests the angles."""
    __test__ = False

    def test_asc(self):
        self._test_angle(const.ASC)

    def test_ic(self):
        self._test_angle(const.IC)

    def test_desc(self):
        self._test_angle(const.DESC)

    def test_mc(self):
        self._test_angle(const.MC)


class FixedStarTest(BaseTest):
    """Tests the fixed stars."""
    __test__ = False

    def test_fixed_star_sirius(self):
        self._test_fixed_star(const.STAR_SIRIUS)

    def test_fixed_star_regulus(self):
        self._test_fixed_star(const.STAR_REGULUS)


class SolarReturnTest(BaseTest):
    """Tests solar returns."""
    __test__ = False

    def test_next_solar_return(self):
        sr_date = ephem.next_solar_return(self.expected[const.SUN]['lon'] + 1, self.context)
        self.assertAlmostEqual(sr_date.jd, 2457096.210, 2)

    def test_prev_solar_return(self):
        sr_date = ephem.prev_solar_return(self.expected[const.SUN]['lon'] - 1, self.context)
        self.assertAlmostEqual(sr_date.jd, 2457094.206, 2)


class SunRiseAndSetTest(BaseTest):
    """Tests sun rises and sets."""
    __test__ = False

    def test_next_sunrise(self):
        expected = ephem.next_sunrise(date, pos)
        self.assertAlmostEqual(expected.jd, 2457095.783, 2)

    def test_next_sunset(self):
        expected = ephem.next_sunset(date, pos)
        self.assertAlmostEqual(expected.jd, 2457095.278, 2)

    def test_prev_sunrise(self):
        expected = ephem.prev_sunrise(date, pos)
        self.assertAlmostEqual(expected.jd, 2457094.784, 2)

    def test_prev_sunset(self):
        expected = ephem.prev_sunset(date, pos)
        self.assertAlmostEqual(expected.jd, 2457094.277, 2)


class StationTest(BaseTest):
    """Tests when planets are stationary."""
    __test__ = False

    def test_sun_stationary(self):
        expected = ephem.find_next_station(const.SUN, date)
        self.assertIsNone(expected)

    def test_moon_stationary(self):
        expected = ephem.find_next_station(const.MOON, date)
        self.assertIsNone(expected)

    def test_mercury_stationary(self):
        station_date, station_type = ephem.find_next_station(const.MERCURY, date)
        self.assertAlmostEqual(station_date.jd, 2457161.708, 2)
        self.assertEqual(station_type, const.STATION_TO_RETROGRADE)

    def test_venus_stationary(self):
        station_date, station_type = ephem.find_next_station(const.VENUS, date)
        self.assertAlmostEqual(station_date.jd, 2457229.208, 2)
        self.assertEqual(station_type, const.STATION_TO_RETROGRADE)

    def test_mars_stationary(self):
        station_date, station_type = ephem.find_next_station(const.MARS, date)
        self.assertAlmostEqual(station_date.jd, 2457496.208, 2)
        self.assertEqual(station_type, const.STATION_TO_RETROGRADE)

    def test_jupiter_stationary(self):
        station_date, station_type = ephem.find_next_station(const.JUPITER, date)
        self.assertAlmostEqual(station_date.jd, 2457121.208, 2)
        self.assertEqual(station_type, const.STATION_TO_DIRECT)

    def test_saturn_stationary(self):
        station_date, station_type = ephem.find_next_station(const.SATURN, date)
        self.assertAlmostEqual(station_date.jd, 2457096.208, 2)
        self.assertEqual(station_type, const.STATION_TO_RETROGRADE)


class ObjectTestTropicalZodiac(ObjectTest, BaseTestTropicalZodiac):
    __test__ = True


class ObjectTestSiderealZodiacFaganBradley(ObjectTest, BaseTestSiderealZodiacFaganBradley):
    __test__ = True


class ObjectTestSiderealZodiacLahiri(ObjectTest, BaseTestSiderealZodiacLahiri):
    __test__ = True


class HouseTestTropicalZodiac(HouseTest, BaseTestTropicalZodiac):
    __test__ = True


class HouseTestSiderealZodiacFaganBradley(HouseTest, BaseTestSiderealZodiacFaganBradley):
    __test__ = True


class HouseTestSiderealZodiacLahiri(HouseTest, BaseTestSiderealZodiacLahiri):
    __test__ = True


class AngleTestTropicalZodiac(AngleTest, BaseTestTropicalZodiac):
    __test__ = True


class AngleTestSiderealZodiacFaganBradley(AngleTest, BaseTestSiderealZodiacFaganBradley):
    __test__ = True


class AngleTestSiderealZodiacLahiri(AngleTest, BaseTestSiderealZodiacLahiri):
    __test__ = True


class FixedStarTestTropicalZodiac(FixedStarTest, BaseTestTropicalZodiac):
    __test__ = True


class FixedStarTestSiderealZodiacFaganBradley(FixedStarTest, BaseTestSiderealZodiacFaganBradley):
    __test__ = True


class FixedStarTestSiderealZodiacLahiri(FixedStarTest, BaseTestSiderealZodiacLahiri):
    __test__ = True


class SolarReturnTestTropicalZodiac(SolarReturnTest, BaseTestTropicalZodiac):
    __test__ = True


class SolarReturnTestSiderealZodiacFaganBradley(SolarReturnTest, BaseTestSiderealZodiacFaganBradley):
    __test__ = True


class SolarReturnTestSiderealZodiacLahiri(SolarReturnTest, BaseTestSiderealZodiacLahiri):
    __test__ = True


class SunRiseAndSetTropicalTests(SunRiseAndSetTest, BaseTestTropicalZodiac):
    __test__ = True


class SunRiseAndSetSiderealTestsFaganBradley(SunRiseAndSetTest, BaseTestSiderealZodiacFaganBradley):
    __test__ = True


class SunRiseAndSetSiderealTestsLahiri(SunRiseAndSetTest, BaseTestSiderealZodiacLahiri):
    __test__ = True


class StationTropicalTests(StationTest, BaseTestTropicalZodiac):
    __test__ = True


class StationSiderealTestsFaganBradley(StationTest, BaseTestSiderealZodiacFaganBradley):
    __test__ = True


class StationSiderealTestsLahiri(StationTest, BaseTestSiderealZodiacLahiri):
    __test__ = True