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
    obj_lon, obj_lat, lon_speed, lat_speed = 0, 0, 0, 0

    if obj_id == const.SOUTH_NODE:
        obj_lon, obj_lat, lon_speed, lat_speed = swe.swe_object(const.NORTH_NODE, jd)
        obj_lon = angle.norm(obj_lon + 180)

    elif obj_id == const.PARS_FORTUNA:
        obj_lon = tools.pars_fortuna_lon(jd, lat, lon)

    elif obj_id == const.SYZYGY:
        syzygy_jd = tools.syzygy_jd(jd)
        obj_lon, obj_lat, lon_speed, lat_speed = swe.swe_object(const.MOON, syzygy_jd)

    else:
        obj_lon, obj_lat, lon_speed, lat_speed = swe.swe_object(obj_id, jd)

    obj = {
        'id': obj_id,
        'lon': obj_lon,
        'lat': obj_lat,
        'lonspeed': lon_speed,
        'latspeed': lat_speed
    }

    _sign_info(obj)
    return obj


# === Houses === #

def get_houses(jd, lat, lon, hsys):
    """ Returns lists of houses and angles. """
    cusps, ascmc = swe.swe_houses(jd, lat, lon, hsys)
    cusps += (cusps[0],)
    houses = [
        {
            'id': const.LIST_HOUSES[i],
            'lon': cusps[i],
            'size': angle.distance(cusps[i], cusps[i + 1])
        } for i in range(12)
    ]
    angles = [
        {'id': const.ASC, 'lon': ascmc[0]},
        {'id': const.MC, 'lon': ascmc[1]},
        {'id': const.DESC, 'lon': angle.norm(ascmc[0] + 180)},
        {'id': const.IC, 'lon': angle.norm(ascmc[1] + 180)}
    ]
    for h in houses:
        _sign_info(h)
    for a in angles:
        _sign_info(a)

    return houses, angles


# === Fixed stars === #

def get_fixed_star(obj_id, jd):
    """ Returns a fixed star. """
    mag, lon, lat = swe.swe_fixed_star(obj_id, jd)
    star = {
        'id': obj_id,
        'mag': mag,
        'lon': lon,
        'lat': lat
    }
    _sign_info(star)
    return star


# === Other functions === #

def _sign_info(obj):
    """ Appends the sign id and longitude to an object. """
    lon = obj['lon']
    obj.update({
        'sign': const.LIST_SIGNS[int(lon / 30)],
        'signlon': lon % 30
    })
