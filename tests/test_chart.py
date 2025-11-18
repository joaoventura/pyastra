import unittest
from dataclasses import asdict

from pyastra import const
from pyastra.chart import Chart

from tests.fixtures.common import date, pos


class ChartTests(unittest.TestCase):

    def setUp(self):
        self.chart_tropical = Chart(date, pos)
        self.chart_sidereal = Chart(date, pos, zodiac=const.ZODIAC_SIDEREAL,
                                    ayanamsa=const.AYANANMSA_FAGAN_BRADLEY)


class SolarReturnTest(ChartTests):

    def test_solar_return_tropical_sun_lon(self):
        """Sun must return to same longitude."""
        sr_chart = self.chart_tropical.solar_return(2025)
        self.assertAlmostEqual(self.chart_tropical.get(const.SUN).lon,
                               sr_chart.get(const.SUN).lon, 2)

    def test_solar_return_sidereal_sun_lon(self):
        """Sun must return to same longitude."""
        sr_chart = self.chart_sidereal.solar_return(2025)
        self.assertAlmostEqual(self.chart_sidereal.get(const.SUN).lon,
                               sr_chart.get(const.SUN).lon, 2)

    def test_solar_return_tropical_context(self):
        """Solar return charts must maintain similar contexts, except jd."""
        sr_chart = self.chart_tropical.solar_return(2025)
        context = asdict(self.chart_tropical.context)
        context_sr = asdict(sr_chart.context)
        del context['jd']
        del context_sr['jd']
        self.assertDictEqual(context, context_sr)

    def test_solar_return_sidereal_context(self):
        """Solar return charts must maintain similar contexts, except jd."""
        sr_chart = self.chart_sidereal.solar_return(2025)
        context = asdict(self.chart_sidereal.context)
        context_sr = asdict(sr_chart.context)
        del context['jd']
        del context_sr['jd']
        self.assertDictEqual(context, context_sr)

    def test_solar_return_tropical_2025(self):
        """Solar return charts dates must match."""
        sr_chart = self.chart_tropical.solar_return(2025)
        self.assertAlmostEqual(sr_chart.date.jd, 2460747.632236115, 2)

    def test_solar_return_sidereal_2025(self):
        """Solar return charts dates must match."""
        sr_chart = self.chart_sidereal.solar_return(2025)
        self.assertAlmostEqual(sr_chart.date.jd, 2460747.7716551097, 2)

    def test_solar_return_tropical_objects(self):
        """Solar return charts dates must calculate the same objects."""
        sr_chart = self.chart_tropical.solar_return(2025)
        ids = [obj.id for obj in self.chart_tropical.objects]
        ids_sr = [obj.id for obj in sr_chart.objects]
        self.assertListEqual(ids, ids_sr)

    def test_solar_return_sidereal_objects(self):
        """Solar return charts dates must calculate the same objects."""
        sr_chart = self.chart_sidereal.solar_return(2025)
        ids = [obj.id for obj in self.chart_sidereal.objects]
        ids_sr = [obj.id for obj in sr_chart.objects]
        self.assertListEqual(ids, ids_sr)

    def test_solar_return_tropical_objects_complete(self):
        """Solar return charts dates must calculate the same objects."""
        chart = Chart(date, pos, ids=const.LIST_OBJECTS)
        sr_chart = chart.solar_return(2025)
        ids = [obj.id for obj in chart.objects]
        ids_sr = [obj.id for obj in sr_chart.objects]
        self.assertListEqual(ids, ids_sr)
