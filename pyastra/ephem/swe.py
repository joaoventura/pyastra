"""
Implements a simple interface with the C Swiss Ephemeris using the pyswisseph library.

"""

# pylint: disable=c-extension-no-member

import swisseph
from pyastra import angle
from pyastra import const

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


# ==== Internal functions ==== #

def set_path(path):
    """ Sets the path for the swe files. """
    swisseph.set_ephe_path(path)


# === Object functions === #

def swe_object(obj, jd):
    """ Returns an object from the Ephemeris. """
    swe_obj = SWE_OBJECTS[obj]
    swe_list, _ = swisseph.calc_ut(jd, swe_obj)
    return {
        'id': obj,
        'lon': swe_list[0],
        'lat': swe_list[1],
        'lonspeed': swe_list[3],
        'latspeed': swe_list[4]
    }


def swe_object_lon(obj, jd):
    """ Returns the longitude of an object. """
    swe_obj = SWE_OBJECTS[obj]
    swe_list, _ = swisseph.calc_ut(jd, swe_obj)
    return swe_list[0]


def swe_next_transit(obj, jd, lat, lon, flag):
    """ Returns the julian date of the next transit of
    an object. The flag should be 'RISE' or 'SET'. 
    
    """
    swe_obj = SWE_OBJECTS[obj]
    flag = swisseph.CALC_RISE if flag == 'RISE' else swisseph.CALC_SET
    trans = swisseph.rise_trans(jd, swe_obj, flag, (lon, lat, 0))
    return trans[1][0]


# === Houses and angles === #

def swe_houses(jd, lat, lon, hsys):
    """ Returns lists of houses and angles. """
    hsys = SWE_HOUSESYS[hsys]
    hlist, ascmc = swisseph.houses(jd, lat, lon, hsys)
    # Add first house to the end of 'hlist' so that we can compute house sizes with an iterator
    hlist += (hlist[0],)
    houses = [
        {
            'id': const.LIST_HOUSES[i],
            'lon': hlist[i],
            'size': angle.distance(hlist[i], hlist[i + 1])
        } for i in range(12)
    ]
    angles = [
        {'id': const.ASC, 'lon': ascmc[0]},
        {'id': const.MC, 'lon': ascmc[1]},
        {'id': const.DESC, 'lon': angle.norm(ascmc[0] + 180)},
        {'id': const.IC, 'lon': angle.norm(ascmc[1] + 180)}
    ]
    return houses, angles


def swe_houses_lon(jd, lat, lon, hsys):
    """ Returns lists with house and angle longitudes. """
    hsys = SWE_HOUSESYS[hsys]
    hlist, ascmc = swisseph.houses(jd, lat, lon, hsys)
    angles = [
        ascmc[0],
        ascmc[1],
        angle.norm(ascmc[0] + 180),
        angle.norm(ascmc[1] + 180)
    ]
    return hlist, angles


# === Fixed stars === #

# Beware: the swisseph.fixstar_mag function is really slow because it parses the fixstars.cat file
# every time.

def swe_fixed_star(star, jd):
    """ Returns a fixed star from the Ephemeris. """
    swe_list, _, _ = swisseph.fixstar2_ut(star, jd)
    mag = swisseph.fixstar2_mag(star)
    return {
        'id': star,
        'mag': mag,
        'lon': swe_list[0],
        'lat': swe_list[1]
    }


# === Eclipses === #

def solar_eclipse_global(jd, backwards):
    """ Returns the jd details of previous or next global solar eclipse. """
    swe_list = swisseph.sol_eclipse_when_glob(jd, backwards=backwards)
    return {
        'maximum': swe_list[1][0],
        'begin': swe_list[1][2],
        'end': swe_list[1][3],
        'totality_begin': swe_list[1][4],
        'totality_end': swe_list[1][5],
        'center_line_begin': swe_list[1][6],
        'center_line_end': swe_list[1][7],
    }


def lunar_eclipse_global(jd, backwards):
    """ Returns the jd details of previous or next global lunar eclipse. """
    swe_list = swisseph.lun_eclipse_when(jd, backwards=backwards)
    return {
        'maximum': swe_list[1][0],
        'partial_begin': swe_list[1][2],
        'partial_end': swe_list[1][3],
        'totality_begin': swe_list[1][4],
        'totality_end': swe_list[1][5],
        'penumbral_begin': swe_list[1][6],
        'penumbral_end': swe_list[1][7],
    }
