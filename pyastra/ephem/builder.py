"""
Functions for retrieving astronomical and astrological data from an ephemeris.
    
It is as middle layer between the Swiss Ephemeris and user software.
Objects are treated as python dicts and jd/lat/lon as floats.

"""

from pyastra import angle
from pyastra import const
from pyastra.object import Object, House, GenericObject, FixedStar
from pyastra.lists import HouseList, GenericList

from . import swe, tools


# === Objects === #

def create_object(obj_id: str, jd: float, lat: float, lon: float) -> Object:
    """
    Returns an object for a specific date and location.

    """
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

    obj = Object(
        id = obj_id,
        lon = obj_lon,
        lat = obj_lat,
        lonspeed = lon_speed,
        latspeed = lat_speed
    )
    _update_sign_info(obj)
    return obj


# === Houses === #

def create_houses_and_angles(jd: float, lat: float, lon: float, hsys: str) \
        -> tuple[HouseList, GenericList]:
    """
    Returns lists of houses and angles.

    """
    cusps, ascmc = swe.swe_houses(jd, lat, lon, hsys)
    cusps += (cusps[0],)

    houses = [
        House(
            id = const.LIST_HOUSES[i],
            lon = cusps[i],
            size = angle.distance(cusps[i], cusps[i+1])
        ) for i in range(12)
    ]
    for house in houses:
        _update_sign_info(house)

    angles = [
        GenericObject(id=const.ASC, lon=ascmc[0]),
        GenericObject(id=const.MC, lon=ascmc[1]),
        GenericObject(id=const.DESC, lon=angle.norm(ascmc[0] + 180)),
        GenericObject(id=const.IC, lon=angle.norm(ascmc[1] + 180))
    ]
    for a in angles:
        _update_sign_info(a)

    return HouseList(houses), GenericList(angles)


# === Fixed stars === #

def create_fixed_star(obj_id: str, jd: float) -> FixedStar:
    """ Returns a fixed star. """
    mag, lon, lat = swe.swe_fixed_star(obj_id, jd)
    star = FixedStar(
        id = obj_id,
        mag = mag,
        lon = lon,
        lat = lat,
    )
    _update_sign_info(star)
    return star


# === Sign information === #

def _update_sign_info(obj: GenericObject):
    """
    Appends the sign information to a Generic Object.

    """
    obj.sign = const.LIST_SIGNS[int(obj.lon / 30)]
    obj.signlon = obj.lon % 30
