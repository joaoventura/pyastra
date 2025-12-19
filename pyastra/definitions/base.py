"""
Base properties.

"""

from pyastra import const

# The four elements
ELEMENTS = [
    const.FIRE,
    const.EARTH,
    const.AIR,
    const.WATER
]

# The four temperaments
TEMPERAMENTS = [
    const.CHOLERIC,
    const.MELANCHOLIC,
    const.SANGUINE,
    const.PHLEGMATIC
]

# Genders
GENDERS = [
    const.MASCULINE,
    const.FEMININE
]

# Factions
FACTIONS = [
    const.DIURNAL,
    const.NOCTURNAL
]

# Sun seasons
SUN_SEASONS = [
    const.SPRING,
    const.SUMMER,
    const.AUTUMN,
    const.WINTER
]

# Element to Temperament
ELEMENT_TO_TEMPERAMENT = {
    const.FIRE: const.CHOLERIC,
    const.EARTH: const.MELANCHOLIC,
    const.AIR: const.SANGUINE,
    const.WATER: const.PHLEGMATIC
}

# Temperament to Element
TEMPERAMENT_TO_ELEMENT = {
    const.CHOLERIC: const.FIRE,
    const.MELANCHOLIC: const.EARTH,
    const.SANGUINE: const.AIR,
    const.PHLEGMATIC: const.WATER
}

# Qualities of elements
ELEMENT_QUALITIES = {
    const.FIRE: [const.HOT, const.DRY],
    const.EARTH: [const.COLD, const.DRY],
    const.AIR: [const.HOT, const.HUMID],
    const.WATER: [const.COLD, const.HUMID]
}

# Qualities of temperaments
TEMPERATURE_QUALITIES = {
    const.CHOLERIC: [const.HOT, const.DRY],
    const.MELANCHOLIC: [const.COLD, const.DRY],
    const.SANGUINE: [const.HOT, const.HUMID],
    const.PHLEGMATIC: [const.COLD, const.HUMID]
}

# Moon Phase Elements
MOONPHASE_ELEMENTS = {
    const.MOON_FIRST_QUARTER: const.AIR,
    const.MOON_SECOND_QUARTER: const.FIRE,
    const.MOON_THIRD_QUARTER: const.EARTH,
    const.MOON_LAST_QUARTER: const.WATER
}

# Sun Season Elements
SUNSEASON_ELEMENTS = {
    const.SPRING: const.AIR,
    const.SUMMER: const.FIRE,
    const.AUTUMN: const.EARTH,
    const.WINTER: const.WATER
}
