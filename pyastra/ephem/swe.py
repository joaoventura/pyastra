"""
Implements a simple interface with the C Swiss Ephemeris using the pyswisseph library.

"""

# pylint: disable=c-extension-no-member

import threading
from contextlib import contextmanager

import swisseph
from pyastra import const
from pyastra.context import ChartContext

# Map objects
SWE_OBJECTS = {
    const.SUN: 0,
    const.MOON: 1,
    const.MERCURY: 2,
    const.VENUS: 3,
    const.MARS: 4,
    const.JUPITER: 5,
    const.SATURN: 6,
    const.URANUS: 7,
    const.NEPTUNE: 8,
    const.PLUTO: 9,
    const.CHIRON: 15,
    const.NORTH_NODE: 10
}

# Map house systems
SWE_HOUSESYS = {
    const.HOUSES_PLACIDUS: b'P',
    const.HOUSES_KOCH: b'K',
    const.HOUSES_PORPHYRIUS: b'O',
    const.HOUSES_REGIOMONTANUS: b'R',
    const.HOUSES_CAMPANUS: b'C',
    const.HOUSES_EQUAL: b'A',
    const.HOUSES_EQUAL_2: b'E',
    const.HOUSES_VEHLOW_EQUAL: b'V',
    const.HOUSES_WHOLE_SIGN: b'W',
    const.HOUSES_MERIDIAN: b'X',
    const.HOUSES_AZIMUTHAL: b'H',
    const.HOUSES_POLICH_PAGE: b'T',
    const.HOUSES_ALCABITUS: b'B',
    const.HOUSES_MORINUS: b'M'
}

# Map ayanamsas
SWE_AYANAMSAS = {
    const.AYANANMSA_FAGAN_BRADLEY: swisseph.SIDM_FAGAN_BRADLEY,
    const.AYANANMSA_LAHIRI: swisseph.SIDM_LAHIRI,
    const.AYANANMSA_DELUCE: swisseph.SIDM_DELUCE,
    const.AYANANMSA_RAMAN: swisseph.SIDM_RAMAN,
    const.AYANANMSA_KRISHNAMURTI: swisseph.SIDM_KRISHNAMURTI,
    const.AYANANMSA_SASSANIAN: swisseph.SIDM_SASSANIAN,
    const.AYANANMSA_ALDEBARAN_15TAU: swisseph.SIDM_ALDEBARAN_15TAU,
    const.AYANANMSA_GALCENTER_0SAG: swisseph.SIDM_GALCENT_0SAG
}

# Flags
CALC_RISE = swisseph.CALC_RISE
CALC_SET = swisseph.CALC_SET

# Thread lock
SWE_LOCK = threading.Lock()


@contextmanager
def swe_context(context: ChartContext):
    """
    Context manager to safely set and reset swisseph's global state.
    It acquires a lock, sets the topographic and sidereal modes based on the chart context,
    yields control, and then reliably cleans up.
    """
    SWE_LOCK.acquire()
    try:
        # Get the speed and use the Swiss Ephemeris
        flags = swisseph.FLG_SPEED | swisseph.FLG_SWIEPH

        # Consider topocentric positions
        if context.amsl > 0.0:
            swisseph.set_topo(context.lat, context.lon, context.amsl)
            flags |= swisseph.FLG_TOPOCTR

        # Use tropical or sidereal zodiac
        if context.zodiac == const.ZODIAC_SIDEREAL:
            eph_mode = SWE_AYANAMSAS[context.ayanamsa]
            swisseph.set_sid_mode(eph_mode)
            flags |= swisseph.FLG_SIDEREAL
        else:
            swisseph.set_sid_mode(0)

        # Yield flags to caller
        yield flags

    finally:
        # Restore zodiac mode
        swisseph.set_sid_mode(0)
        SWE_LOCK.release()


def set_path(path: str):
    """ Sets the path for the swe files. """
    swisseph.set_ephe_path(path)


def swe_object(obj_id: str, context: ChartContext) -> tuple:
    """
    Get raw positional data of an object from the ephemeris.

    Returns: tuple with (lon, lat, lon_speed, lat_speed).
    """
    with swe_context(context) as flags:
        swe_obj = SWE_OBJECTS[obj_id]
        swe_list, _ = swisseph.calc_ut(context.jd, swe_obj, flags)

    return swe_list[0], swe_list[1], swe_list[3], swe_list[4]


def swe_object_fast(obj_id: str, jd: float) -> tuple:
    """
    Get raw positional data of an object from the ephemeris, ignoring any context such as
    zodiac type, ayanamsa, etc.

    Returns: tuple with (lon, lat, lon_speed, lat_speed).
    """
    swe_obj = SWE_OBJECTS[obj_id]
    swe_list, _ = swisseph.calc_ut(jd, swe_obj, swisseph.FLG_SPEED)
    return swe_list[0], swe_list[1], swe_list[3], swe_list[4]


def swe_houses(context: ChartContext) -> tuple:
    """
    Get the list of houses cusps and angles from the ephemeris.

    From pyswisseph, the cusps are returned as a tuple of house cusps. The ascmc and additional
    points are returned as (asc, mc, armc, vertex, equasc, coasc1, coasc2, polasc),
    as defined in swehouse.c.
    Returns: tuple with (1) the house cusps and (2) the angles as (asc, mc).
    """
    with swe_context(context) as flags:
        hsys = SWE_HOUSESYS[context.hsys]
        cusps, ascmc = swisseph.houses_ex(context.jd, context.lat, context.lon, hsys, flags)
        angles = (ascmc[0], ascmc[1])

    return cusps, angles


def swe_fixed_star(obj_id: str, context: ChartContext) -> tuple:
    """
    Get a fixed star from the ephemeris.

    Caution: the swisseph.fixstar2_mag function is slow because it parses 'fixstars.cat' every time.
    Returns: tuple with (mag, lon, lat).
    """
    with swe_context(context) as flags:
        swe_list, _, _ = swisseph.fixstar2_ut(obj_id, context.jd, flags)
        mag = swisseph.fixstar2_mag(obj_id)

    return mag[0], swe_list[0], swe_list[1]


def swe_next_transit(obj_id: str, jd: float, lat: float, lon: float, flag: int) -> float:
    """
    Get the julian date of the next transit of an object.

    Transit can be CALC_RISE, CALC_SET, or CALC_MTRANSIT (for meridian)
    Returns a float with the julian date.
    """
    swe_obj = SWE_OBJECTS[obj_id]
    trans = swisseph.rise_trans(jd, swe_obj, flag, (lon, lat, 0))
    return trans[1][0]
