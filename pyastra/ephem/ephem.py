"""
This module implements functions which are useful for pyastra.
Basically, it converts internal objects and lists from the ephemeris to pyastra.objects and
pyastra.lists.
    
PyAstra users will want to use this module for accessing the ephemeris.
    
"""

from pyastra import const
from pyastra.context import ChartContext
from pyastra.datetime import Datetime
from pyastra.geopos import GeoPos
from pyastra.object import Object, FixedStar
from pyastra.lists import GenericList, ObjectList, HouseList, FixedStarList

from . import builder, swe, tools


# === Objects === #

def get_object(obj_id: str, context: ChartContext) -> Object:
    """
    Returns an ephemeris object.

    """
    return builder.create_object(obj_id, context)


def get_objects(obj_ids: list, context: ChartContext) -> ObjectList:
    """
    Returns a list of objects.

    """
    return ObjectList([get_object(obj_id, context) for obj_id in obj_ids])


# === Houses and angles === #

def get_houses_and_angles(context: ChartContext) -> tuple:
    """
    Returns the lists of houses and angles.
    Since houses and angles are computed at the same time, this function should be fast.
    
    """
    return builder.create_houses_and_angles(context)


def get_houses(context: ChartContext) -> HouseList:
    """
    Returns a list of houses.

    """
    houses, _ = get_houses_and_angles(context)
    return houses


def get_angles(context: ChartContext) -> GenericList:
    """
    Returns a list of angles (Asc, MC.)

    """
    _, angles = get_houses_and_angles(context)
    return angles


# === Fixed stars === #

def get_fixed_star(obj_id: str, context: ChartContext) -> FixedStar:
    """
    Returns a fixed star from the ephemeris.

    """
    return builder.create_fixed_star(obj_id, context)


def get_fixed_stars(ids: list, context: ChartContext) -> FixedStarList:
    """
    Returns a list of fixed stars.

    """
    star_list = [get_fixed_star(ID, context) for ID in ids]
    return FixedStarList(star_list)


# === Solar returns === #

def next_solar_return(lon: float, context: ChartContext) -> Datetime:
    """
    Returns the next date when sun will be at longitude 'lon'.

    """
    jd = tools.solar_return_jd(lon, context, True)
    return Datetime.from_jd(jd, context.utc_offset)


def prev_solar_return(lon: float, context: ChartContext) -> Datetime:
    """
    Returns the previous date when sun was at longitude 'lon'.

    """
    jd = tools.solar_return_jd(lon, context, False)
    return Datetime.from_jd(jd, context.utc_offset)


# === Sunrise and sunsets === #

def next_sunrise(date: Datetime, pos: GeoPos) -> Datetime:
    """
    Returns the date of the next sunrise relative to 'date'.

    """
    jd = swe.swe_next_transit(const.SUN, date.jd, pos.lat, pos.lon, swe.CALC_RISE)
    return Datetime.from_jd(jd, date.utcoffset)


def next_sunset(date: Datetime, pos: GeoPos) -> Datetime:
    """
    Returns the date of the next sunset relative to 'date'.

    """
    jd = swe.swe_next_transit(const.SUN, date.jd, pos.lat, pos.lon, swe.CALC_SET)
    return Datetime.from_jd(jd, date.utcoffset)


def prev_sunrise(date: Datetime, pos: GeoPos) -> Datetime:
    """
    Returns the date of the previous sunrise relative to 'date'.

    """
    new_date = Datetime.from_jd(date.jd - 1, date.utcoffset)
    return next_sunrise(new_date, pos)


def prev_sunset(date: Datetime, pos: GeoPos) -> Datetime:
    """
    Returns the date of the previous sunset relative to 'date'.

    """
    new_date = Datetime.from_jd(date.jd - 1, date.utcoffset)
    return next_sunset(new_date, pos)


# === Station === #

def find_next_station(obj_id: str, date: Datetime) -> tuple | None:
    """
    Finds the approximate date and type of the next planetary station.
    A station occurs when the planet's longitudinal speed crosses zero, or, in other words, when
    the planet goes from direct to retrograde or from retrograde to direct.

    Returns a tuple containing the datetime and the type of station (const.STATION_TO_DIRECT or
    const.STATION_TO_RETROGRADE), or None if the planet does not become stationary.
    """
    res = tools.find_next_station(obj_id, date.jd)
    if res:
        station_jd, station_type = res
        return Datetime.from_jd(station_jd, date.utcoffset), station_type

    return None
