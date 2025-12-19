"""
Zodiac properties.

"""

from pyastra import const
from . import base


_signs = const.LIST_SIGNS

# Modality
MODALITY = dict(zip(_signs, [const.CARDINAL, const.FIXED, const.MUTABLE] * 4))

# Sun Season
_seasons = [[season] * 3 for season in base.SUN_SEASONS]
_seasons = sum(_seasons, [])
SUN_SEASON = dict(zip(_signs, _seasons))

# Simple properties
GENDER = dict(zip(_signs, base.GENDERS * 6))
FACTION = dict(zip(_signs, base.FACTIONS * 6))
ELEMENT = dict(zip(_signs, base.ELEMENTS * 3))
TEMPERAMENT = dict(zip(_signs, base.TEMPERAMENTS * 3))

# Fertilities
FERTILITY = {
    const.ARIES: const.SIGN_MODERATELY_STERILE,
    const.TAURUS: const.SIGN_MODERATELY_FERTILE,
    const.GEMINI: const.SIGN_STERILE,
    const.CANCER: const.SIGN_FERTILE,
    const.LEO: const.SIGN_STERILE,
    const.VIRGO: const.SIGN_STERILE,
    const.LIBRA: const.SIGN_MODERATELY_FERTILE,
    const.SCORPIO: const.SIGN_FERTILE,
    const.SAGITTARIUS: const.SIGN_MODERATELY_FERTILE,
    const.CAPRICORN: const.SIGN_MODERATELY_STERILE,
    const.AQUARIUS: const.SIGN_MODERATELY_STERILE,
    const.PISCES: const.SIGN_FERTILE
}

# Sign numbers
SIGN_NUMBER = dict((sign, i + 1) for (i, sign) in enumerate(_signs))

# Sign figure properties
FIGURE_BESTIAL = [
    const.ARIES,
    const.TAURUS,
    const.LEO,
    const.SAGITTARIUS,
    const.CAPRICORN
]

FIGURE_HUMAN = [
    const.GEMINI,
    const.VIRGO,
    const.LIBRA,
    const.AQUARIUS
]

FIGURE_WILD = [
    const.LEO
]
