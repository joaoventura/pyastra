"""
Functions for retrieving astronomical and astrological data from an ephemeris.
    
It is the middle layer between the Swiss Ephemeris and user software.

"""

from pyastra import angle
from pyastra import const
from pyastra.object import Object, House, GenericObject, FixedStar
from pyastra.lists import HouseList, GenericList

from . import swe, tools


def create_object(obj_id: str, jd: float, lat: float, lon: float) -> Object:
    """
    Returns an object for a specific date and location.

    """
    if obj_id == const.SOUTH_NODE:
        obj_lon, _, _, _ = swe.swe_object(const.NORTH_NODE, jd)
        return Object(id=obj_id, lon=angle.norm(obj_lon + 180))

    if obj_id == const.PARS_FORTUNA:
        obj_lon = tools.pars_fortuna_lon(jd, lat, lon)
        return Object(id=obj_id, lon=obj_lon)

    if obj_id == const.SYZYGY:
        syzygy_jd = tools.syzygy_jd(jd)
        obj_lon, obj_lat, lon_speed, lat_speed = swe.swe_object(const.MOON, syzygy_jd)

    else:
        obj_lon, obj_lat, lon_speed, lat_speed = swe.swe_object(obj_id, jd)

    return Object(
        id = obj_id,
        lon = obj_lon,
        lat = obj_lat,
        lonspeed = lon_speed,
        latspeed = lat_speed
    )


def create_houses_and_angles(jd: float, lat: float, lon: float, hsys: str) -> tuple:
    """
    Returns tuple with the lists of houses and angles.

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

    angles = [
        GenericObject(id=const.ASC, lon=ascmc[0]),
        GenericObject(id=const.MC, lon=ascmc[1]),
        GenericObject(id=const.DESC, lon=angle.norm(ascmc[0] + 180)),
        GenericObject(id=const.IC, lon=angle.norm(ascmc[1] + 180))
    ]

    return HouseList(houses), GenericList(angles)


def create_fixed_star(obj_id: str, jd: float) -> FixedStar:
    """
    Returns a fixed star.

    """
    mag, lon, lat = swe.swe_fixed_star(obj_id, jd)
    return FixedStar(
        id = obj_id,
        mag = mag,
        lon = lon,
        lat = lat,
    )
