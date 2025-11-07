"""
This module implements functions which are useful for pyastra.
Basically, it converts internal objects and lists from the ephemeris to pyastra.objects and
pyastra.lists.
    
PyAstra users will want to use this module for accessing the ephemeris.
    
"""

from pyastra.datetime import Datetime
from pyastra.object import GenericObject, Object, House, FixedStar
from pyastra.lists import GenericList, ObjectList, HouseList, FixedStarList

from . import eph
from . import swe


# === Objects === #

def get_object(obj_id, date, pos):
    """ Returns an ephemeris object. """
    obj = eph.get_object(obj_id, date.jd, pos.lat, pos.lon)
    return Object.from_dict(obj)


def get_object_list(ids, date, pos):
    """ Returns a list of objects. """
    obj_list = [get_object(ID, date, pos) for ID in ids]
    return ObjectList(obj_list)


# === Houses and angles === #

def get_houses(date, pos, hsys):
    """
    Returns the lists of houses and angles.
    Since houses and angles are computed at the same time, this function should be fast.
    
    """
    houses, angles = eph.get_houses(date.jd, pos.lat, pos.lon, hsys)
    house_list = [House.from_dict(house) for house in houses]
    angle_list = [GenericObject.from_dict(angle) for angle in angles]
    return HouseList(house_list), GenericList(angle_list)


def get_house_list(date, pos, hsys):
    """ Returns a list of houses. """
    houses, _ = get_houses(date, pos, hsys)
    return houses


def get_angle_list(date, pos, hsys):
    """ Returns a list of angles (Asc, MC..) """
    _, angles = get_houses(date, pos, hsys)
    return angles


# === Fixed stars === #

def get_fixed_star(obj_id, date):
    """ Returns a fixed star from the ephemeris. """
    star = eph.get_fixed_star(obj_id, date.jd)
    return FixedStar.from_dict(star)


def get_fixed_star_list(ids, date):
    """ Returns a list of fixed stars. """
    star_list = [get_fixed_star(ID, date) for ID in ids]
    return FixedStarList(star_list)


# === Solar returns === #

def next_solar_return(date, lon):
    """ Returns the next date when sun is at longitude 'lon'. """
    jd = eph.next_solar_return(date.jd, lon)
    return Datetime.from_jd(jd, date.utcoffset)


def prev_solar_return(date, lon):
    """ Returns the previous date when sun is at longitude 'lon'. """
    jd = eph.prev_solar_return(date.jd, lon)
    return Datetime.from_jd(jd, date.utcoffset)


# === Sunrise and sunsets === #

def next_sunrise(date, pos):
    """ Returns the date of the next sunrise. """
    jd = eph.next_sunrise(date.jd, pos.lat, pos.lon)
    return Datetime.from_jd(jd, date.utcoffset)


def next_sunset(date, pos):
    """ Returns the date of the next sunset. """
    jd = eph.next_sunset(date.jd, pos.lat, pos.lon)
    return Datetime.from_jd(jd, date.utcoffset)


def last_sunrise(date, pos):
    """ Returns the date of the last sunrise. """
    jd = eph.last_sunrise(date.jd, pos.lat, pos.lon)
    return Datetime.from_jd(jd, date.utcoffset)


def last_sunset(date, pos):
    """ Returns the date of the last sunset. """
    jd = eph.last_sunset(date.jd, pos.lat, pos.lon)
    return Datetime.from_jd(jd, date.utcoffset)


# === Station === #

def next_station(obj_id, date):
    """ Returns the approximate date of the next station. """
    jd = eph.next_station(obj_id, date.jd)
    return Datetime.from_jd(jd, date.utcoffset)


# === Eclipses === #

def prev_solar_eclipse(date):
    """ Returns the Datetime of the maximum phase of the previous global solar eclipse. """
    eclipse = swe.solar_eclipse_global(date.jd, backwards=True)
    return Datetime.from_jd(eclipse['maximum'], date.utcoffset)


def next_solar_eclipse(date):
    """ Returns the Datetime of the maximum phase of the next global solar eclipse. """
    eclipse = swe.solar_eclipse_global(date.jd, backwards=False)
    return Datetime.from_jd(eclipse['maximum'], date.utcoffset)


def prev_lunar_eclipse(date):
    """ Returns the Datetime of the maximum phase of the previous global lunar eclipse. """
    eclipse = swe.lunar_eclipse_global(date.jd, backwards=True)
    return Datetime.from_jd(eclipse['maximum'], date.utcoffset)


def next_lunar_eclipse(date):
    """ Returns the Datetime of the maximum phase of the next global lunar eclipse. """
    eclipse = swe.lunar_eclipse_global(date.jd, backwards=False)
    return Datetime.from_jd(eclipse['maximum'], date.utcoffset)
