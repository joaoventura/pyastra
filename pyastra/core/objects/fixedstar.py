"""
This module implements the Fixed Star class.

"""

from pyastra import const
from pyastra.core import angle
from pyastra.core.objects.generic import GenericObject
from pyastra.core.objects.house import House


class FixedStar(GenericObject):
    """ This class represents a generic fixed star. """

    def __init__(self, *args, **kwargs):
        self.mag = 0.0
        super().__init__(*args, **kwargs)
        self.type = const.OBJ_FIXED_STAR

    def __str__(self):
        string = super().__str__()[:-1]
        return f'{string} {self.mag}>'

    # === Properties === #

    # Map magnitudes to orbs
    _ORBS = [[2, 7.5], [3, 5.5], [4, 3.5], [5, 1.5]]

    def orb(self):
        """ Returns the orb of this fixed star. """
        for (mag, orb) in FixedStar._ORBS:
            if self.mag < mag:
                return orb
        return 0.5

    # === Functions === #

    def aspects(self, obj):
        """ Returns true if this star aspects another object.
        Fixed stars only aspect by conjunctions.

        """
        dist = angle.closest_distance(self.lon, obj.lon)
        return abs(dist) < self.orb()

    def house(self) -> House:
        """ Returns the house of this star. """
        return self.chart.houses.get_object_house(self)
