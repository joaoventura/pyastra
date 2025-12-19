"""
Functions for retrieving astronomical and astrological data from an ephemeris.
    
It is the middle layer between the Swiss Ephemeris and user software.

"""

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

from ..core import angle
from pyastra import const
from pyastra.context import ChartContext
from pyastra.core.object import Object, House, GenericObject, FixedStar
from pyastra.core.lists import HouseList, GenericList
from . import swe, tools

if TYPE_CHECKING:
    from pyastra.core.chart import Chart


def create_object(obj_id: str, context: ChartContext, chart: Chart = None) -> Object:
    """Returns an object for a specific date and location."""
    if obj_id == const.SOUTH_NODE:
        obj_lon, _, _, _ = swe.swe_object(const.NORTH_NODE, context=context)
        return Object(id=obj_id, lon=angle.norm(obj_lon + 180))

    if obj_id == const.PARS_FORTUNA:
        obj_lon = tools.pars_fortuna_lon(context=context)
        return Object(id=obj_id, lon=obj_lon)

    if obj_id == const.SYZYGY:
        syzygy_jd = tools.syzygy_jd(context.jd)
        syzygy_context = dataclasses.replace(context, jd=syzygy_jd)
        obj_lon, obj_lat, lon_speed, lat_speed = swe.swe_object(const.MOON, context=syzygy_context)

    else:
        obj_lon, obj_lat, lon_speed, lat_speed = swe.swe_object(obj_id, context=context)

    return Object(
        id = obj_id,
        lon = obj_lon,
        lat = obj_lat,
        lon_speed = lon_speed,
        lat_speed = lat_speed,
        chart = chart
    )


def create_houses_and_angles(context: ChartContext, chart: Chart = None) -> tuple:
    """Returns a tuple with lists of houses and angles."""
    cusps, ascmc = swe.swe_houses(context=context)

    # Append the first cusp to the end to simplify size calculation in the loop
    cusps += (cusps[0],)
    houses = [
        House(
            id = const.LIST_HOUSES[i],
            lon = cusps[i],
            size = angle.distance(cusps[i], cusps[i + 1]),
            chart = chart
        ) for i in range(12)
    ]

    angles = [
        GenericObject(id=const.ASC, lon=ascmc[0], chart=chart),
        GenericObject(id=const.MC, lon=ascmc[1], chart=chart),
        GenericObject(id=const.DESC, lon=angle.norm(ascmc[0] + 180), chart=chart),
        GenericObject(id=const.IC, lon=angle.norm(ascmc[1] + 180), chart=chart)
    ]

    return HouseList(houses), GenericList(angles)


def create_fixed_star(obj_id: str, context: ChartContext, chart: Chart = None) -> FixedStar:
    """Returns a fixed star."""
    mag, lon, lat = swe.swe_fixed_star(obj_id, context)
    return FixedStar(
        id = obj_id,
        mag = mag,
        lon = lon,
        lat = lat,
        chart = chart
    )
