"""
This module implements classes to represent Astrology objects, such as planets, Houses
and Fixed-Stars.

"""

from . import const
from . import angle
from . import utils
from . import props


# ------------------ #
#   Generic Object   #
# ------------------ #

class GenericObject:
    """
    This class represents a generic object and includes properties which are common to all
    objects on a chart.
    
    """

    def __init__(self, *args, **kwargs):
        self.id = const.NO_PLANET
        self.type = const.OBJ_GENERIC
        self.lon = 0.0
        self.lat = 0.0
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

    # === Properties === #

    @property
    def sign(self) -> str:
        """ Object sign (from longitude). """
        return const.LIST_SIGNS[int(self.lon / 30)]

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
        self.signlon = self.lon % 30
        self.sign = const.LIST_SIGNS[int(self.lon / 30.0)]

    def antiscia(self):
        """ Returns antiscia object. """
        obj = self.copy()
        obj.type = const.OBJ_GENERIC
        obj.relocate(360 - obj.lon + 180)
        return obj

    def cantiscia(self):
        """ Returns contra-antiscia object. """
        obj = self.copy()
        obj.type = const.OBJ_GENERIC
        obj.relocate(360 - obj.lon)
        return obj


# -------------------- #
#   Astrology Object   #
# -------------------- #

class Object(GenericObject):
    """
    This class represents an Astrology object, such as the sun or the moon, and includes properties
    and functions which are common for all objects.
    
    """

    def __init__(self, *args, **kwargs):
        self.type = const.OBJ_PLANET
        self.lonspeed = 0.0
        self.latspeed = 0.0
        super().__init__(*args, **kwargs)

    def __str__(self):
        string = super().__str__()[:-1]
        lonspeed = angle.to_string(self.lonspeed)
        return f'{string} {lonspeed}>'

    # === Properties === #

    def orb(self):
        """ Returns the orb of this object. """
        return props.object.orb[self.id]

    def mean_motion(self):
        """ Returns the mean daily motion of this object. """
        return props.object.meanMotion[self.id]

    def movement(self):
        """ Returns if this object is direct, retrograde 
        or stationary. 
        
        """
        if abs(self.lonspeed) < 0.0003:
            return const.STATIONARY
        if self.lonspeed > 0:
            return const.DIRECT
        return const.RETROGRADE

    def gender(self):
        """ Returns the gender of this object. """
        return props.object.gender[self.id]

    def faction(self):
        """ Returns the faction of this object. """
        return props.object.faction[self.id]

    def element(self):
        """ Returns the element of this object. """
        return props.object.element[self.id]

    # === Functions === #

    def is_direct(self):
        """ Returns if this object is in direct motion. """
        return self.movement() == const.DIRECT

    def is_retrograde(self):
        """ Returns if this object is in retrograde motion. """
        return self.movement() == const.RETROGRADE

    def is_stationary(self):
        """ Returns if this object is stationary. """
        return self.movement() == const.STATIONARY

    def is_fast(self):
        """ Returns if this object is in fast motion. """
        return abs(self.lonspeed) >= self.mean_motion()


# ------------------ #
#     House Cusp     #
# ------------------ #

class House(GenericObject):
    """ This class represents a generic house cusp. """

    # The traditional house offset
    _OFFSET = -5.0

    def __init__(self, *args, **kwargs):
        self.type = const.OBJ_HOUSE
        self.size = 30.0
        super().__init__(*args, **kwargs)

    def __str__(self):
        string = super().__str__()[:-1]
        return f'{string} {self.size}>'

    # === Properties === #

    def num(self):
        """ Returns the number of this house [1..12]. """
        return int(self.id[5:])

    def condition(self):
        """ Returns the condition of this house. 
        The house can be angular, succedent or cadent.
    
        """
        return props.house.condition[self.id]

    def gender(self):
        """ Returns the gender of this house. """
        return props.house.gender[self.id]

    # === Functions === #

    def is_above_horizon(self):
        """ Returns true if this house is above horizon. """
        return self.id in props.house.aboveHorizon

    def in_house(self, lon):
        """ Returns if a longitude belongs to this house. """
        dist = angle.distance(self.lon + House._OFFSET, lon)
        return dist < self.size

    def has_object(self, obj):
        """ Returns true if an object is in this house. """
        return self.in_house(obj.lon)


# ------------------ #
#     Fixed Star     #
# ------------------ #

class FixedStar(GenericObject):
    """ This class represents a generic fixed star. """

    def __init__(self, *args, **kwargs):
        self.type = const.OBJ_FIXED_STAR
        self.mag = 0.0
        super().__init__(*args, **kwargs)

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
