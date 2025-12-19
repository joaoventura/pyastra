"""
This module provides a rich sign object.

"""

from pyastra import const
from pyastra.definitions import props
from pyastra.dignities import essential

class Sign(str):
    """
    Represents a Zodiac Sign.
    Inherits from 'str' for backward compatibility and extends it with astrological context.
    """

    def __new__(cls, name):
        if name not in const.LIST_SIGNS:
            raise ValueError(f"'{name}' is not a valid Zodiac Sign.")
        return super().__new__(cls, name)

    @property
    def name(self) -> str:
        """ Returns the Sign name. """
        return str(self)

    @property
    def modality(self) -> str:
        """ Returns the modality (Cardinal, Fixed, Mutable). """
        return props.sign.mode[self]

    @property
    def season(self) -> str:
        """ Returns the sun season (Spring, Summer, Autumn, Winter). """
        return props.sign.sunseason[self]

    @property
    def gender(self) -> str:
        """ Returns the gender (Masculine, Feminine). """
        return props.sign.gender[self]

    @property
    def faction(self) -> str:
        """ Returns the faction (Diurnal, Nocturnal). """
        return props.sign.faction[self]

    @property
    def element(self) -> str:
        """ Returns the element (Fire, Earth, Air, Water). """
        return props.sign.element[self]

    @property
    def temperament(self) -> str:
        """ Returns the temperament (Choleric, Melancholic, Sanguine, Phlegmatic). """
        return props.sign.temperament[self]

    @property
    def fertility(self) -> str:
        """ Returns the fertility ([Moderately] Fertile, Sterile). """
        return props.sign.fertility[self]

    @property
    def number(self) -> int:
        """ Returns the number (Zodiac number). """
        return props.sign.number[self]

    @property
    def is_figure_bestial(self):
        """ Returns whether the sign has a figure of a 'beast'. """
        return self in props.sign.figureBestial

    @property
    def is_figure_human(self):
        """ Returns whether the sign has a figure of a 'human'. """
        return self in props.sign.figureHuman

    @property
    def is_figure_wild(self):
        """ Returns whether the sign has a figure of a 'wild' animal. """
        return self in props.sign.figureWild

    @property
    def ruler(self) -> str:
        """ Returns the sign ruler ID. """
        return essential.ruler(self)

    def __repr__(self):
        return f"<Sign: {self} ({self.element}, {self.modality})>"
