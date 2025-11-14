"""
This module implements a class to represent an astrology Chart. It provides methods to handle
the chart, as well as three relevant properties:
- objects: a list with the chart's objects
- houses: a list with the chart's houses
- angles: a list with the chart's angles

Since houses 1 and 10 may not match the Asc and MC in some house systems, the Chart class includes
the list of angles. The angles should be used when you want to deal with angle's longitudes.

There are also methods to access fixed stars.
    
"""
import copy
import dataclasses

from . import angle
from . import const
from . import utils

from .context import ChartContext
from .ephem import ephem
from .datetime import Datetime


# ------------------ #
#    Chart Class     #
# ------------------ #

class Chart:
    """ This class represents an astrology chart. """

    def __init__(self, date, pos, **kwargs):
        """ Creates an astrology chart for a given date and location.
        
        Optional arguments are:
        - hsys: house system
        - IDs: list of objects to include
        
        """
        # Handle optional arguments
        hsys = kwargs.get('hsys', const.HOUSES_DEFAULT)
        ids = kwargs.get('IDs', const.LIST_OBJECTS_TRADITIONAL)

        self.date = date
        self.pos = pos
        self.hsys = hsys
        self.context = ChartContext(
            jd = self.date.jd,
            lat = self.pos.lat,
            lon = self.pos.lon,
            **kwargs
        )

        self.objects = ephem.get_objects(ids, context=self.context, chart=self)
        self.houses, self.angles = ephem.get_houses_and_angles(context=self.context, chart=self)

    def copy(self):
        """ Returns a deep copy of this chart. """
        chart = Chart.__new__(Chart)
        chart.date = self.date
        chart.pos = self.pos
        chart.hsys = self.hsys
        chart.objects = self.objects.copy()
        chart.houses = self.houses.copy()
        chart.angles = self.angles.copy()
        chart.context = copy.copy(self.context)
        return chart

    def __str__(self):
        return f"<Chart {self.date} {self.pos} [{self.context.hsys}] [{self.context.zodiac}]>"

    def __repr__(self):
        return self.__str__()

    # === Properties === #

    def get_object(self, obj_id):
        """ Returns an object from the chart. """
        return self.objects.get(obj_id)

    def get_house(self, obj_id):
        """ Returns an house from the chart. """
        return self.houses.get(obj_id)

    def get_angle(self, obj_id):
        """ Returns an angle from the chart. """
        return self.angles.get(obj_id)

    def get(self, obj_id):
        """ Returns an object, house or angle from the chart. """
        if obj_id.startswith('House'):
            return self.get_house(obj_id)
        if obj_id in const.LIST_ANGLES:
            return self.get_angle(obj_id)
        return self.get_object(obj_id)

    # === Fixed stars === #

    # The computation of fixed stars is inefficient, so the access must be made directly to the
    # ephemeris only when needed.

    def get_fixed_star(self, obj_id):
        """ Returns a fixed star from the ephemeris. """
        return ephem.get_fixed_star(obj_id, context=self.context, chart=self)

    def get_fixed_stars(self):
        """ Returns a list with all fixed stars. """
        ids = const.LIST_FIXED_STARS
        return ephem.get_fixed_stars(ids, context=self.context, chart=self)

    # === Houses and angles === #

    def is_house1_asc(self):
        """ Returns true if House1 is the same as the Asc. """
        house1 = self.get_house(const.HOUSE1)
        asc = self.get_angle(const.ASC)
        dist = angle.closest_distance(house1.lon, asc.lon)
        return abs(dist) < 0.0003  # 1 arc-second

    def is_house10_mc(self):
        """ Returns true if House10 is the same as the MC. """
        house10 = self.get_house(const.HOUSE10)
        mc = self.get_angle(const.MC)
        dist = angle.closest_distance(house10.lon, mc.lon)
        return abs(dist) < 0.0003  # 1 arc-second

    # === Other properties === #

    def is_diurnal(self):
        """ Returns true if this chart is diurnal. """
        sun = self.get_object(const.SUN)
        mc = self.get_angle(const.MC)

        # Get ecliptical positions and check if the sun is above the horizon.
        lat = self.pos.lat
        sun_ra, sun_decl = utils.eq_coords(sun.lon, sun.lat)
        mc_ra, _ = utils.eq_coords(mc.lon, 0)
        return utils.is_above_horizon(sun_ra, sun_decl, mc_ra, lat)

    def get_moon_phase(self):
        """ Returns the phase of the moon. """
        sun = self.get_object(const.SUN)
        moon = self.get_object(const.MOON)
        dist = angle.distance(sun.lon, moon.lon)
        if dist < 90:
            return const.MOON_FIRST_QUARTER
        if dist < 180:
            return const.MOON_SECOND_QUARTER
        if dist < 270:
            return const.MOON_THIRD_QUARTER
        return const.MOON_LAST_QUARTER

    # === Solar returns === #

    def solar_return(self, year):
        """ Returns this chart's solar return for a given year. """
        sun = self.get_object(const.SUN)
        date = Datetime(f'{year}/01/01', '00:00', self.date.utcoffset)
        context = dataclasses.replace(self.context, jd=date.jd)
        sr_date = ephem.next_solar_return(sun.lon, context=context)
        return Chart(sr_date, self.pos, hsys=self.hsys)
