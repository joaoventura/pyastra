"""
Defines the ChartContext, a data class that holds all the necessary input parameters for
astrological calculations.

This object serves as a single, immutable source of truth for the context of a chart,
including date, time, position, and calculation settings.

"""

from dataclasses import dataclass
from pyastra import const

@dataclass(frozen=True)
class ChartContext:
    """
    An immutable data class representing the complete context for a single astrological chart
    calculation.

    """

    jd: float
    lat: float
    lon: float
    utc_offset: float = 0.0
    hsys: str = const.HOUSES_DEFAULT
    zodiac: str = const.ZODIAC_TROPICAL
    ayanamsa: str = const.AYANANMSA_FAGAN_BRADLEY
    alt: float = 0.0   # Altitude above mean sea level
