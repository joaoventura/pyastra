"""
This module provides a rich sign object.

"""

from pyastra import const
from pyastra import definitions
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
        return definitions.signs.MODALITY[self]

    @property
    def season(self) -> str:
        """ Returns the sun season (Spring, Summer, Autumn, Winter). """
        return definitions.signs.SUN_SEASON[self]

    @property
    def gender(self) -> str:
        """ Returns the gender (Masculine, Feminine). """
        return definitions.signs.GENDER[self]

    @property
    def faction(self) -> str:
        """ Returns the faction (Diurnal, Nocturnal). """
        return definitions.signs.FACTION[self]

    @property
    def element(self) -> str:
        """ Returns the element (Fire, Earth, Air, Water). """
        return definitions.signs.ELEMENT[self]

    @property
    def temperament(self) -> str:
        """ Returns the temperament (Choleric, Melancholic, Sanguine, Phlegmatic). """
        return definitions.signs.TEMPERAMENT[self]

    @property
    def fertility(self) -> str:
        """ Returns the fertility ([Moderately] Fertile, Sterile). """
        return definitions.signs.FERTILITY[self]

    @property
    def number(self) -> int:
        """ Returns the number (Zodiac number). """
        return definitions.signs.SIGN_NUMBER[self]

    @property
    def is_figure_bestial(self):
        """ Returns whether the sign has a figure of a 'beast'. """
        return self in definitions.signs.FIGURE_BESTIAL

    @property
    def is_figure_human(self):
        """ Returns whether the sign has a figure of a 'human'. """
        return self in definitions.signs.FIGURE_HUMAN

    @property
    def is_figure_wild(self):
        """ Returns whether the sign has a figure of a 'wild' animal. """
        return self in definitions.signs.FIGURE_WILD

    @property
    def ruler(self) -> str:
        """ Returns the sign ruler ID. """
        return essential.ruler(self)

    def __repr__(self):
        return f"<Sign: {self} ({self.element}, {self.modality})>"
