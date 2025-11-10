"""
This module implements functions which are useful for pyastra.
Basically, it converts internal objects and lists from the ephemeris to pyastra.objects and
pyastra.lists.
    
PyAstra users will want to use this module for accessing the ephemeris.
    
"""

from pyastra import const
from pyastra.datetime import Datetime
from pyastra.geopos import GeoPos
from pyastra.object import Object, FixedStar
from pyastra.lists import GenericList, ObjectList, HouseList, FixedStarList

from . import builder, swe, tools


# === Objects === #

def get_object(obj_id: str, date: Datetime, pos: GeoPos) -> Object:
    """
    Returns an ephemeris object.

    """
    return builder.create_object(obj_id, date.jd, pos.lat, pos.lon)


def get_objects(ids: list, date: Datetime, pos: GeoPos) -> ObjectList:
    """
    Returns a list of objects.

    """
    obj_list = [get_object(ID, date, pos) for ID in ids]
    return ObjectList(obj_list)


# === Houses and angles === #

def get_houses_and_angles(date: Datetime, pos: GeoPos, hsys: str) -> tuple:
    """
    Returns the lists of houses and angles.
    Since houses and angles are computed at the same time, this function should be fast.
    
    """
    return builder.create_houses_and_angles(date.jd, pos.lat, pos.lon, hsys)


def get_houses(date: Datetime, pos: GeoPos, hsys: str) -> HouseList:
    """
    Returns a list of houses.

    """
    houses, _ = get_houses_and_angles(date, pos, hsys)
    return houses


def get_angles(date: Datetime, pos: GeoPos, hsys: str) -> GenericList:
    """
    Returns a list of angles (Asc, MC.)

    """
    _, angles = get_houses_and_angles(date, pos, hsys)
    return angles


# === Fixed stars === #

def get_fixed_star(obj_id: str, date: Datetime) -> FixedStar:
    """
    Returns a fixed star from the ephemeris.

    """
    return builder.create_fixed_star(obj_id, date.jd)


def get_fixed_stars(ids: list, date: Datetime) -> FixedStarList:
    """
    Returns a list of fixed stars.

    """
    star_list = [get_fixed_star(ID, date) for ID in ids]
    return FixedStarList(star_list)


# === Solar returns === #

def next_solar_return(date: Datetime, lon: float) -> Datetime:
    """
    Returns the next date when sun will be at longitude 'lon'.

    """
    jd = tools.solar_return_jd(date.jd, lon, True)
    return Datetime.from_jd(jd, date.utcoffset)


def prev_solar_return(date: Datetime, lon: float) -> Datetime:
    """
    Returns the previous date when sun was at longitude 'lon'.

    """
    jd = tools.solar_return_jd(date.jd, lon, False)
    return Datetime.from_jd(jd, date.utcoffset)


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

def next_station(obj_id: float, date: Datetime) -> Datetime | None:
    """
    Returns the approximate date of the next station.

    """
    jd = tools.next_station_jd(obj_id, date.jd)
    return Datetime.from_jd(jd, date.utcoffset) if jd else None
