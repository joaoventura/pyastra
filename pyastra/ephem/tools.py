"""
Functions specific for the ephem subpackage.
    
"""

from pyastra import angle
from pyastra import const
from pyastra import utils

from . import swe

# One arc-second error for iterative algorithms
MAX_ERROR = 0.0003


def is_diurnal(jd: float, lat: float, lon: float) -> bool:
    """
    Returns if the sun is above the horizon for a given date and location.
    It computes the result using the sun's and MC's Right Ascension and Declination values.

    """
    sun_lon, sun_lat, _, _ = swe.swe_object(const.SUN, jd)
    _, angles = swe.swe_houses(jd, lat, lon, const.HOUSES_DEFAULT)
    mc_lon = angles[1]
    sun_ra, sun_decl = utils.eq_coords(sun_lon, sun_lat)
    mc_ra, _ = utils.eq_coords(mc_lon, 0.0)
    return utils.is_above_horizon(sun_ra, sun_decl, mc_ra, lat)


def pars_fortuna_lon(jd: float, lat: float, lon: float) -> float:
    """
    Returns the ecliptic longitude of Pars Fortuna.
    It computes the longitude using the respective diurnal and nocturnal formulas.

    """
    sun_lon, _, _, _ = swe.swe_object(const.SUN, jd)
    moon_lon, _, _, _ = swe.swe_object(const.MOON, jd)
    asc_lon = swe.swe_houses(jd, lat, lon, const.HOUSES_DEFAULT)[1][0]

    if is_diurnal(jd, lat, lon):
        return angle.norm(asc_lon + moon_lon - sun_lon)
    return angle.norm(asc_lon + sun_lon - moon_lon)


# === Iterative algorithms === #

def syzygy_jd(jd: float) -> float:
    """
    Finds the previous new moon or full moon and returns the julian date of that event.
    The syzygy is the location of the pre-natal moon (new moon or full moon).

    """
    sun_lon, _, _, _ = swe.swe_object(const.SUN, jd)
    moon_lon, _, _, _ = swe.swe_object(const.MOON, jd)
    dist = angle.distance(sun_lon, moon_lon)

    # Offset represents the Syzygy type, where zero is conjunction and 180 is opposition.
    offset = 180 if (dist >= 180) else 0
    while abs(dist) > MAX_ERROR:
        jd = jd - dist / 13.1833  # Moon mean daily motion
        sun_lon, _, _, _ = swe.swe_object(const.SUN, jd)
        moon_lon, _, _, _ = swe.swe_object(const.MOON, jd)
        dist = angle.closest_distance(sun_lon - offset, moon_lon)
    return jd


def solar_return_jd(jd: float, lon: float, forward:str=True) -> float:
    """
    Finds the julian date before or after 'jd' when the sun is at longitude given by 'lon'.
    It searches forward by default.
    
    """
    sun_lon, _, _, _ = swe.swe_object(const.SUN, jd)
    if forward:
        dist = angle.distance(sun_lon, lon)
    else:
        dist = -angle.distance(lon, sun_lon)

    while abs(dist) > MAX_ERROR:
        jd = jd + dist / 0.9833  # Sun mean daily motion
        sun_lon, _, _, _ = swe.swe_object(const.SUN, jd)
        dist = angle.closest_distance(sun_lon, lon)
    return jd


def find_next_station(obj_id: str, jd: float) -> tuple | None:
    """
    Finds the approximate julian date and type of the next planetary station.
    A station occurs when the planet's longitudinal speed crosses zero.

    Returns a tuple containing the julian date and the type of station (direct to retrograde or
    vice versa).

    """
    _, _, initial_speed, _ = swe.swe_object(obj_id, jd)
    for i in range(2000):
        next_jd = jd + i / 2
        _, _, next_lon_speed, _ = swe.swe_object(obj_id, next_jd)
        if initial_speed * next_lon_speed <= 0:
            if initial_speed > 0:
                station_type = const.STATION_TO_RETROGRADE
            else:
                station_type = const.STATION_TO_DIRECT

            return next_jd, station_type
    return None
