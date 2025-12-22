"""
Aspect properties

"""

from pyastra import const

ASPECT_NAMES = {
    # Major Aspects
    const.NO_ASPECT: 'None',
    const.CONJUNCTION: 'Conjunction',
    const.SEXTILE: 'Sextile',
    const.SQUARE: 'Square',
    const.TRINE: 'Trine',
    const.OPPOSITION: 'Opposition',

    # Minor Aspects
    const.SEMISEXTILE: 'Semisextile',
    const.SEMIQUINTILE: 'Semiquintile',
    const.SEMISQUARE: 'Semisquare',
    const.QUINTILE: 'Quintile',
    const.SESQUIQUINTILE: 'Sesquiquintile',
    const.SESQUISQUARE: 'Sesquisquare',
    const.BIQUINTILE: 'Biquintile',
    const.QUINCUNX: 'Quincunx'
}
