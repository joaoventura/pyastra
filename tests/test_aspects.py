import unittest
from pyastra import const
from pyastra import aspects
from pyastra.chart import Chart
from tests.fixtures.common import date, pos, ASPECTS


class ChartTests(unittest.TestCase):

    def setUp(self):
        self.chart = Chart(date, pos)
        self.sun = self.chart.get(const.SUN)
        self.moon = self.chart.get(const.MOON)
        self.mercury = self.chart.get(const.MERCURY)
        self.venus = self.chart.get(const.VENUS)
        self.mars = self.chart.get(const.MARS)
        self.jupiter = self.chart.get(const.JUPITER)
        self.saturn = self.chart.get(const.SATURN)
        self.north_node = self.chart.get(const.NORTH_NODE)
        self.south_node = self.chart.get(const.SOUTH_NODE)
        self.syzygy = self.chart.get(const.SYZYGY)
        self.pars_fortuna = self.chart.get(const.PARS_FORTUNA)

    def _test_aspect(self, obj1, obj2):
        asp = aspects.get_aspect(obj1, obj2, const.MAJOR_ASPECTS)
        expected = ASPECTS[obj1.id][obj2.id]
        self.assertEqual(asp.type, expected['type'])
        self.assertEqual(asp.active.id, expected['active_id'])
        self.assertEqual(asp.movement(), expected['movement'])
        self.assertEqual(asp.mutual_aspect(), expected['mutual_aspect'])
        self.assertEqual(asp.mutual_movement(), expected['mutual_movement'])


class AspectTest(ChartTests):

    def test_sun_aspects_moon(self):
        self._test_aspect(self.sun, self.moon)

    def test_sun_aspects_mercury(self):
        self._test_aspect(self.sun, self.mercury)

    def test_sun_aspects_venus(self):
        self._test_aspect(self.sun, self.venus)

    def test_sun_aspects_mars(self):
        self._test_aspect(self.sun, self.mars)

    def test_sun_aspects_jupiter(self):
        self._test_aspect(self.sun, self.jupiter)

    def test_sun_aspects_saturn(self):
        self._test_aspect(self.sun, self.saturn)

    def test_sun_aspects_north_node(self):
        self._test_aspect(self.sun, self.north_node)

    def test_sun_aspects_south_node(self):
        self._test_aspect(self.sun, self.south_node)

    def test_sun_aspects_syzygy(self):
        self._test_aspect(self.sun, self.syzygy)

    def test_sun_aspects_pars_fortuna(self):
        self._test_aspect(self.sun, self.pars_fortuna)

    def test_moon_aspects_sun(self):
        self._test_aspect(self.moon, self.sun)

    def test_moon_aspects_mercury(self):
        self._test_aspect(self.moon, self.mercury)

    def test_moon_aspects_venus(self):
        self._test_aspect(self.moon, self.venus)

    def test_moon_aspects_mars(self):
        self._test_aspect(self.moon, self.mars)

    def test_moon_aspects_jupiter(self):
        self._test_aspect(self.moon, self.jupiter)

    def test_moon_aspects_saturn(self):
        self._test_aspect(self.moon, self.saturn)

    def test_moon_aspects_north_node(self):
        self._test_aspect(self.moon, self.north_node)

    def test_moon_aspects_south_node(self):
        self._test_aspect(self.moon, self.south_node)

    def test_moon_aspects_syzygy(self):
        self._test_aspect(self.moon, self.syzygy)

    def test_moon_aspects_pars_fortuna(self):
        self._test_aspect(self.moon, self.pars_fortuna)

    def test_mercury_aspects_sun(self):
        self._test_aspect(self.mercury, self.sun)

    def test_mercury_aspects_moon(self):
        self._test_aspect(self.mercury, self.moon)

    def test_mercury_aspects_venus(self):
        self._test_aspect(self.mercury, self.venus)

    def test_mercury_aspects_mars(self):
        self._test_aspect(self.mercury, self.mars)

    def test_mercury_aspects_jupiter(self):
        self._test_aspect(self.mercury, self.jupiter)

    def test_mercury_aspects_saturn(self):
        self._test_aspect(self.mercury, self.saturn)

    def test_mercury_aspects_north_node(self):
        self._test_aspect(self.mercury, self.north_node)

    def test_mercury_aspects_south_node(self):
        self._test_aspect(self.mercury, self.south_node)

    def test_mercury_aspects_syzygy(self):
        self._test_aspect(self.mercury, self.syzygy)

    def test_mercury_aspects_pars_fortuna(self):
        self._test_aspect(self.mercury, self.pars_fortuna)

    def test_venus_aspects_sun(self):
        self._test_aspect(self.venus, self.sun)

    def test_venus_aspects_moon(self):
        self._test_aspect(self.venus, self.moon)

    def test_venus_aspects_mercury(self):
        self._test_aspect(self.venus, self.mercury)

    def test_venus_aspects_mars(self):
        self._test_aspect(self.venus, self.mars)

    def test_venus_aspects_jupiter(self):
        self._test_aspect(self.venus, self.jupiter)

    def test_venus_aspects_saturn(self):
        self._test_aspect(self.venus, self.saturn)

    def test_venus_aspects_north_node(self):
        self._test_aspect(self.venus, self.north_node)

    def test_venus_aspects_south_node(self):
        self._test_aspect(self.venus, self.south_node)

    def test_venus_aspects_syzygy(self):
        self._test_aspect(self.venus, self.syzygy)

    def test_venus_aspects_pars_fortuna(self):
        self._test_aspect(self.venus, self.pars_fortuna)

    def test_mars_aspects_sun(self):
        self._test_aspect(self.mars, self.sun)

    def test_mars_aspects_moon(self):
        self._test_aspect(self.mars, self.moon)

    def test_mars_aspects_mercury(self):
        self._test_aspect(self.mars, self.mercury)

    def test_mars_aspects_venus(self):
        self._test_aspect(self.mars, self.venus)

    def test_mars_aspects_jupiter(self):
        self._test_aspect(self.mars, self.jupiter)

    def test_mars_aspects_saturn(self):
        self._test_aspect(self.mars, self.saturn)

    def test_mars_aspects_north_node(self):
        self._test_aspect(self.mars, self.north_node)

    def test_mars_aspects_south_node(self):
        self._test_aspect(self.mars, self.south_node)

    def test_mars_aspects_syzygy(self):
        self._test_aspect(self.mars, self.syzygy)

    def test_mars_aspects_pars_fortuna(self):
        self._test_aspect(self.mars, self.pars_fortuna)

    def test_jupiter_aspects_sun(self):
        self._test_aspect(self.jupiter, self.sun)

    def test_jupiter_aspects_moon(self):
        self._test_aspect(self.jupiter, self.moon)

    def test_jupiter_aspects_mercury(self):
        self._test_aspect(self.jupiter, self.mercury)

    def test_jupiter_aspects_venus(self):
        self._test_aspect(self.jupiter, self.venus)

    def test_jupiter_aspects_mars(self):
        self._test_aspect(self.jupiter, self.mars)

    def test_jupiter_aspects_saturn(self):
        self._test_aspect(self.jupiter, self.saturn)

    def test_jupiter_aspects_north_node(self):
        self._test_aspect(self.jupiter, self.north_node)

    def test_jupiter_aspects_south_node(self):
        self._test_aspect(self.jupiter, self.south_node)

    def test_jupiter_aspects_syzygy(self):
        self._test_aspect(self.jupiter, self.syzygy)

    def test_jupiter_aspects_pars_fortuna(self):
        self._test_aspect(self.jupiter, self.pars_fortuna)

    def test_saturn_aspects_sun(self):
        self._test_aspect(self.saturn, self.sun)

    def test_saturn_aspects_moon(self):
        self._test_aspect(self.saturn, self.moon)

    def test_saturn_aspects_mercury(self):
        self._test_aspect(self.saturn, self.mercury)

    def test_saturn_aspects_venus(self):
        self._test_aspect(self.saturn, self.venus)

    def test_saturn_aspects_mars(self):
        self._test_aspect(self.saturn, self.mars)

    def test_saturn_aspects_jupiter(self):
        self._test_aspect(self.saturn, self.jupiter)

    def test_saturn_aspects_north_node(self):
        self._test_aspect(self.saturn, self.north_node)

    def test_saturn_aspects_south_node(self):
        self._test_aspect(self.saturn, self.south_node)

    def test_saturn_aspects_syzygy(self):
        self._test_aspect(self.saturn, self.syzygy)

    def test_saturn_aspects_pars_fortuna(self):
        self._test_aspect(self.saturn, self.pars_fortuna)
