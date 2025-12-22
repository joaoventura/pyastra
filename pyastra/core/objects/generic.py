"""
This module implements the GenericObject class.
Generic objects are all astrological objects that have a position in the chart.

"""

from pyastra import const, utils
from pyastra.core import angle
from pyastra.core.sign import Sign


class GenericObject:
    """
    This class represents a generic object and includes properties which are common to all
    objects on a chart.

    """

    def __init__(self, **kwargs):
        self.id = const.NO_PLANET
        self.type = const.OBJ_GENERIC
        self.lon = 0.0
        self.lat = 0.0

        # Strong reference to chart which may cause problems in long-running applications.
        self.chart = None
        self.__dict__.update(kwargs)

    @classmethod
    def from_dict(cls, _dict):
        """ Builds instance from dictionary of properties. """
        obj = cls()
        obj.__dict__.update(_dict)
        return obj

    def copy(self):
        """ Returns a deep copy of this object. """
        return self.from_dict(self.__dict__)

    def __str__(self):
        lon = angle.to_string(self.signlon)
        return f'<{self.id} {self.sign} {lon}>'

    def __repr__(self):
        return self.__str__()

    # === Properties === #

    @property
    def sign(self) -> Sign:
        """ Object sign (from longitude). """
        return Sign(const.LIST_SIGNS[int(self.lon / 30)])

    @property
    def signlon(self) -> float:
        """ Object longitude in sign. """
        return self.lon % 30

    def orb(self):
        """ Returns the orb of this object. """
        return -1.0

    def is_planet(self):
        """ Returns if this object is a planet. """
        return self.type == const.OBJ_PLANET

    def eq_coords(self, zerolat=False):
        """
        Returns the Equatorial Coordinates of this object.
        Receives a boolean parameter to consider a zero latitude.

        """
        lat = 0.0 if zerolat else self.lat
        return utils.eq_coords(self.lon, lat)

    # === Functions === #

    def relocate(self, lon):
        """ Relocates this object to a new longitude. """
        self.lon = angle.norm(lon)

    def antiscia(self):
        """ Returns the antiscia object. """
        obj = self.copy()
        obj.type = const.OBJ_GENERIC
        obj.relocate(360 - obj.lon + 180)
        return obj

    def cantiscia(self):
        """ Returns the contra-antiscia object. """
        obj = self.copy()
        obj.type = const.OBJ_GENERIC
        obj.relocate(360 - obj.lon)
        return obj
