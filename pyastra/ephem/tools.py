"""
Functions specific for the ephem subpackage.
    
"""

from pyastra import angle
from pyastra import const
from pyastra import utils

from . import swe

# One arc-second error for iterative algorithms
MAX_ERROR = 0.0003


# === Object positions === #

def pf_lon(jd, lat, lon):
    """ Returns the ecliptic longitude of Pars Fortuna. """
    sun = swe.swe_object_lon(const.SUN, jd)
    moon = swe.swe_object_lon(const.MOON, jd)
    asc = swe.swe_houses_lon(jd, lat, lon,
                             const.HOUSES_DEFAULT)[1][0]

    if is_diurnal(jd, lat, lon):
        return angle.norm(asc + moon - sun)
    return angle.norm(asc + sun - moon)


# === Diurnal  === #

def is_diurnal(jd, lat, lon):
    """ Returns if the sun is above the horizon for a given date and location. """
    sun = swe.swe_object(const.SUN, jd)
    mc = swe.swe_houses_lon(jd, lat, lon,
                            const.HOUSES_DEFAULT)[1][1]
    ra, decl = utils.eqCoords(sun['lon'], sun['lat'])
    mc_ra, _ = utils.eqCoords(mc, 0.0)
    return utils.isAboveHorizon(ra, decl, mc_ra, lat)


# === Iterative algorithms === #

def syzygy_jd(jd):
    """ Finds the latest new or full moon and returns the julian date of that event. """
    sun = swe.swe_object_lon(const.SUN, jd)
    moon = swe.swe_object_lon(const.MOON, jd)
    dist = angle.distance(sun, moon)

    # Offset represents the Syzygy type.
    # Zero is conjunction and 180 is opposition.
    offset = 180 if (dist >= 180) else 0
    while abs(dist) > MAX_ERROR:
        jd = jd - dist / 13.1833  # Moon mean daily motion
        sun = swe.swe_object_lon(const.SUN, jd)
        moon = swe.swe_object_lon(const.MOON, jd)
        dist = angle.closestdistance(sun - offset, moon)
    return jd


def solar_return_jd(jd, lon, forward=True):
    """
    Finds the julian date before or after 'jd' when the sun is at longitude 'lon'.
    It searches forward by default.
    
    """
    sun = swe.swe_object_lon(const.SUN, jd)
    if forward:
        dist = angle.distance(sun, lon)
    else:
        dist = -angle.distance(lon, sun)

    while abs(dist) > MAX_ERROR:
        jd = jd + dist / 0.9833  # Sun mean motion
        sun = swe.swe_object_lon(const.SUN, jd)
        dist = angle.closestdistance(sun, lon)
    return jd


# === Other algorithms === #

def next_station_jd(obj_id, jd):
    """ Finds the aproximate julian date of the next station of a planet. """
    speed = swe.swe_object(obj_id, jd)['lonspeed']
    for i in range(2000):
        nextjd = jd + i / 2
        nextspeed = swe.swe_object(obj_id, nextjd)['lonspeed']
        if speed * nextspeed <= 0:
            return nextjd
    return None
