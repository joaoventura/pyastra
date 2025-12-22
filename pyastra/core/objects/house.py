"""
This module implements the House class.

"""

from pyastra import const, definitions
from pyastra.core import angle
from pyastra.core.objects.generic import GenericObject
from pyastra.dignities import essential


class House(GenericObject):
    """ This class represents a generic house cusp. """

    # The traditional house offset
    _OFFSET = -5.0

    def __init__(self, *args, **kwargs):
        self.size = 30.0
        super().__init__(*args, **kwargs)
        self.type = const.OBJ_HOUSE

    def __str__(self):
        string = super().__str__()[:-1]
        return f'{string} {self.size}>'

    # === Properties === #

    def num(self):
        """ Returns the number of this house [1..12]. """
        return int(self.id[5:])

    @property
    def condition(self):
        """ Returns the condition of this house (Angular, Succedent, Cadent). """
        return definitions.houses.CONDITION[self.id]

    @property
    def is_benefic(self) -> bool:
        """ True if considered a benefic house (1, 5, 11). """
        return self.id in [const.HOUSE1, const.HOUSE5, const.HOUSE11]

    @property
    def is_malefic(self) -> bool:
        """ True if considered a difficult/malefic house (6, 8, 12). """
        return self.id in [const.HOUSE6, const.HOUSE8, const.HOUSE12]

    @property
    def gender(self):
        """ Returns the gender of this house. """
        return definitions.houses.GENDER[self.id]

    @property
    def meaning(self):
        """ Returns the meaning of this house. """
        return definitions.houses.MEANING[self.id]

    @property
    def ruler(self):
        """ Returns the house ruler. """
        return essential.ruler(self.sign)

    @property
    def almutem(self):
        """ Returns the almutem of this house. """
        return essential.almutem(self.sign, self.signlon)

    # === Functions === #

    def is_above_horizon(self):
        """ Returns true if this house is above horizon. """
        return self.id in definitions.houses.ABOVE_HORIZON

    def in_house(self, lon):
        """ Returns if a longitude belongs to this house. """
        dist = angle.distance(self.lon + House._OFFSET, lon)
        return dist < self.size

    def has_object(self, obj):
        """ Returns true if an object is in this house. """
        return self.in_house(obj.lon)
