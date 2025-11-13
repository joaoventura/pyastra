import unittest

from pyastra import const
from pyastra.context import ChartContext
from pyastra.ephem import ephem
from tests.fixtures.common import date, pos, VALUES_TROPICAL, VALUES_SIDEREAL_FAGAN_BRADLEY


class BaseTest(unittest.TestCase):
    """Base for all ephem tests."""

    def setUp(self):
        self.context = None
        self.expected = None

    def _test_object(self, obj_id):
        """Tests an object."""
        obj = ephem.get_object(obj_id, context=self.context)
        self.assertAlmostEqual(obj.lon, self.expected[obj_id]['lon'], 2)
        self.assertAlmostEqual(obj.lat, self.expected[obj_id]['lat'], 2)
        self.assertEqual(obj.sign, self.expected[obj_id]['sign'])

    def _test_house(self, house_id):
        """Tests a house."""
        houses = ephem.get_houses(context=self.context)
        house = houses.get(house_id)
        self.assertAlmostEqual(house.lon, self.expected[house_id]['lon'], 2)
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
        self.assertAlmostEqual(obj.lon, self.expected[obj_id]['lon'], 2)
        self.assertAlmostEqual(obj.lat, self.expected[obj_id]['lat'], 2)
        self.assertEqual(obj.sign, self.expected[obj_id]['sign'])


class BaseTropicalTests(BaseTest):
    """Base for all ephem tests using the Tropical zodiac."""

    def setUp(self):
        self.context = ChartContext(
            jd = date.jd,
            lon = pos.lon,
            lat = pos.lat
        )
        self.expected = VALUES_TROPICAL


class ObjectTropicalTests(BaseTropicalTests):
    """Tests objects using the tropical zodiac."""

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


class HouseTropicalTests(BaseTropicalTests):
    """Tests houses."""

    def test_house1(self):
        self._test_house(const.HOUSE1)

    def test_house4(self):
        self._test_house(const.HOUSE4)

    def test_house7(self):
        self._test_house(const.HOUSE7)

    def test_house10(self):
        self._test_house(const.HOUSE10)


class AngleTropicalTests(BaseTropicalTests):
    """Tests the angles."""

    def test_asc(self):
        self._test_angle(const.ASC)

    def test_ic(self):
        self._test_angle(const.IC)

    def test_desc(self):
        self._test_angle(const.DESC)

    def test_mc(self):
        self._test_angle(const.MC)


class FixedStarTropicalTests(BaseTropicalTests):
    """Tests the fixed stars."""

    def test_fixed_star_sirius(self):
        self._test_fixed_star(const.STAR_SIRIUS)

    def test_fixed_star_regulus(self):
        self._test_fixed_star(const.STAR_REGULUS)


class SolarReturnTropicalTests(BaseTropicalTests):
    """Tests solar returns."""

    def test_next_solar_return(self):
        sr_date = ephem.next_solar_return(date, VALUES_TROPICAL[const.SUN]['lon'] + 1)
        self.assertAlmostEqual(sr_date.jd, 2457096.210, 2)

    def test_prev_solar_return(self):
        sr_date = ephem.prev_solar_return(date, VALUES_TROPICAL[const.SUN]['lon'] - 1)
        self.assertAlmostEqual(sr_date.jd, 2457094.206, 2)


class SunRiseAndSetTropicalTests(BaseTropicalTests):
    """Tests sun rises and sets."""

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


class StationTropicalTests(BaseTropicalTests):
    """Tests when planets are stationary."""

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


class BaseSiderealTests(BaseTest):
    """Base for all ephem tests using the Sidereal zodiac."""

    def setUp(self):
        self.context = ChartContext(
            jd = date.jd,
            lon = pos.lon,
            lat = pos.lat,
            zodiac = const.ZODIAC_SIDEREAL,
            ayanamsa = const.AYANANMSA_FAGAN_BRADLEY
        )
        self.expected = VALUES_SIDEREAL_FAGAN_BRADLEY


class ObjectSiderealTests(BaseSiderealTests):
    """Tests objects using the sidereal zodiac."""

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


class HouseSiderealTests(BaseSiderealTests):
    """Tests houses using the sidereal zodiac."""

    def test_house1(self):
        self._test_house(const.HOUSE1)

    def test_house4(self):
        self._test_house(const.HOUSE4)

    def test_house7(self):
        self._test_house(const.HOUSE7)

    def test_house10(self):
        self._test_house(const.HOUSE10)


class AngleSiderealTests(BaseSiderealTests):
    """Tests the angles using the sidereal zodiac."""

    def test_asc(self):
        self._test_angle(const.ASC)

    def test_ic(self):
        self._test_angle(const.IC)

    def test_desc(self):
        self._test_angle(const.DESC)

    def test_mc(self):
        self._test_angle(const.MC)


class FixedStarSiderealTests(BaseSiderealTests):
    """Tests the fixed stars using the sidereal zodiac."""

    def test_fixed_star_sirius(self):
        self._test_fixed_star(const.STAR_SIRIUS)

    def test_fixed_star_regulus(self):
        self._test_fixed_star(const.STAR_REGULUS)


class SolarReturnSiderealTests(BaseSiderealTests):
    """Tests solar returns using the sidereal zodiac."""

    def test_next_solar_return(self):
        sr_date = ephem.next_solar_return(date, VALUES_TROPICAL[const.SUN]['lon'] + 1)
        self.assertAlmostEqual(sr_date.jd, 2457096.210, 2)

    def test_prev_solar_return(self):
        sr_date = ephem.prev_solar_return(date, VALUES_TROPICAL[const.SUN]['lon'] - 1)
        self.assertAlmostEqual(sr_date.jd, 2457094.206, 2)


class SunRiseAndSetSiderealTests(BaseSiderealTests):
    """Tests sun rises and sets using the sidereal zodiac."""

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


class StationSiderealTests(BaseSiderealTests):
    """Tests when planets are stationary using the sidereal zodiac."""

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
