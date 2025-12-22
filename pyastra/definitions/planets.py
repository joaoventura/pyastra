"""
Planet properties

"""

from pyastra import const

MEAN_MOTION = {
    const.NO_PLANET: 0,
    const.SUN: 0.9833,
    const.MOON: 13.1833,
    const.MERCURY: 0.9833,
    const.VENUS: 0.9833,
    const.MARS: 0.5166,
    const.JUPITER: 0.0833,
    const.SATURN: 0.0333,
    const.URANUS: 0.001,
    const.NEPTUNE: 0.0001,
    const.PLUTO: 0.00001,
    const.CHIRON: 0.00001,
    const.NORTH_NODE: 13.1833,
    const.SOUTH_NODE: 13.1833,
    const.SYZYGY: 0.0
}

# Object orbs
ORB = {
    const.NO_PLANET: 0,
    const.SUN: 15,
    const.MOON: 12,
    const.MERCURY: 7,
    const.VENUS: 7,
    const.MARS: 8,
    const.JUPITER: 9,
    const.SATURN: 9,
    const.URANUS: 5,
    const.NEPTUNE: 5,
    const.PLUTO: 5,
    const.CHIRON: 5,
    const.NORTH_NODE: 12,
    const.SOUTH_NODE: 12,
    const.SYZYGY: 0,
    const.PARS_FORTUNA: 0
}

# Planet elements
ELEMENT = {
    const.SATURN: const.EARTH,
    const.JUPITER: const.AIR,
    const.MARS: const.FIRE,
    const.SUN: const.FIRE,
    const.VENUS: const.AIR,
    const.MERCURY: const.EARTH,
    const.MOON: const.WATER
}

# Planet temperaments
TEMPERAMENT = {
    const.SATURN: const.MELANCHOLIC,
    const.JUPITER: const.SANGUINE,
    const.MARS: const.CHOLERIC,
    const.SUN: const.CHOLERIC,
    const.VENUS: const.SANGUINE,
    const.MERCURY: const.MELANCHOLIC,
    const.MOON: const.PHLEGMATIC
}

# Planet genders
GENDER = {
    const.SATURN: const.MASCULINE,
    const.JUPITER: const.MASCULINE,
    const.MARS: const.MASCULINE,
    const.SUN: const.MASCULINE,
    const.VENUS: const.FEMININE,
    const.MERCURY: const.NEUTRAL,
    const.MOON: const.FEMININE
}

# Planet factions
FACTION = {
    const.SATURN: const.DIURNAL,
    const.JUPITER: const.DIURNAL,
    const.MARS: const.NOCTURNAL,
    const.SUN: const.DIURNAL,
    const.VENUS: const.NOCTURNAL,
    const.MERCURY: const.NEUTRAL,
    const.MOON: const.NOCTURNAL
}

# Sign joy of planets
SIGN_OF_JOY = {
    const.SATURN: const.AQUARIUS,
    const.JUPITER: const.SAGITTARIUS,
    const.MARS: const.SCORPIO,
    const.SUN: const.LEO,
    const.VENUS: const.TAURUS,
    const.MERCURY: const.VIRGO,
    const.MOON: const.CANCER
}

# House joy of planets
HOUSE_OF_JOY = {
    const.SATURN: const.HOUSE12,
    const.JUPITER: const.HOUSE11,
    const.MARS: const.HOUSE6,
    const.SUN: const.HOUSE9,
    const.VENUS: const.HOUSE5,
    const.MERCURY: const.HOUSE1,
    const.MOON: const.HOUSE3
}
