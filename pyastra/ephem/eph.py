"""
Functions for retrieving astronomical and astrological data from an ephemeris.
    
It is as middle layer between the Swiss Ephemeris and user software.
Objects are treated as python dicts and jd/lat/lon as floats.

"""

from pyastra import angle
from pyastra import const

from . import swe
from . import tools


# === Objects === #

def get_object(obj_id, jd, lat, lon):
    """ Returns an object for a specific date and location. """
    if obj_id == const.SOUTH_NODE:
        obj = swe.swe_object(const.NORTH_NODE, jd)
        obj.update({
            'id': const.SOUTH_NODE,
            'lon': angle.norm(obj['lon'] + 180)
        })
    elif obj_id == const.PARS_FORTUNA:
        pflon = tools.pf_lon(jd, lat, lon)
        obj = {
            'id': obj_id,
            'lon': pflon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }
    elif obj_id == const.SYZYGY:
        szjd = tools.syzygy_jd(jd)
        obj = swe.swe_object(const.MOON, szjd)
        obj['id'] = const.SYZYGY
    else:
        obj = swe.swe_object(obj_id, jd)

    _sign_info(obj)
    return obj


# === Houses === #

def get_houses(jd, lat, lon, hsys):
    """ Returns lists of houses and angles. """
    houses, angles = swe.swe_houses(jd, lat, lon, hsys)
    for h in houses:
        _sign_info(h)
    for a in angles:
        _sign_info(a)
    return houses, angles


# === Fixed stars === #

def get_fixed_star(obj_id, jd):
    """ Returns a fixed star. """
    star = swe.swe_fixed_star(obj_id, jd)
    _sign_info(star)
    return star


# === Solar returns === #

def next_solar_return(jd, lon):
    """ Return the JD of the next solar return. """
    return tools.solar_return_jd(jd, lon, True)


def prev_solar_return(jd, lon):
    """ Returns the JD of the previous solar return. """
    return tools.solar_return_jd(jd, lon, False)


# === Sunrise and sunsets === #

def next_sunrise(jd, lat, lon):
    """ Returns the JD of the next sunrise. """
    return swe.swe_next_transit(const.SUN, jd, lat, lon, 'RISE')


def next_sunset(jd, lat, lon):
    """ Returns the JD of the next sunset. """
    return swe.swe_next_transit(const.SUN, jd, lat, lon, 'SET')


def last_sunrise(jd, lat, lon):
    """ Returns the JD of the last sunrise. """
    return next_sunrise(jd - 1.0, lat, lon)


def last_sunset(jd, lat, lon):
    """ Returns the JD of the last sunset. """
    return next_sunset(jd - 1.0, lat, lon)


# === Stations === #

def next_station(obj_id, jd):
    """ Returns the approximate jd of the next station. """
    return tools.next_station_jd(obj_id, jd)


# === Other functions === #

def _sign_info(obj):
    """ Appends the sign id and longitude to an object. """
    lon = obj['lon']
    obj.update({
        'sign': const.LIST_SIGNS[int(lon / 30)],
        'signlon': lon % 30
    })
