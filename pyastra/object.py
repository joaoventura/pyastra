"""
This module implements classes to represent Astrology objects, such as planets, Houses
and Fixed-Stars.

"""

from . import const
from . import angle
from . import utils
from . import props
from pyastra.sign import Sign
from pyastra.dignities import essential
from pyastra.dignities.accidental import AccidentalDignity
from pyastra.dignities.essential import EssentialInfo


# ------------------ #
#   Generic Object   #
# ------------------ #

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


# -------------------- #
#   Astrology Object   #
# -------------------- #

class Object(GenericObject):
    """
    This class represents an Astrology object, such as the sun or the moon, and includes properties
    and functions which are common for all objects.
    
    """

    def __init__(self, *args, **kwargs):
        self.lon_speed = 0.0
        self.lat_speed = 0.0
        super().__init__(*args, **kwargs)
        self.type = const.OBJ_PLANET

    def __str__(self):
        string = super().__str__()[:-1]
        lon_speed = angle.to_string(self.lon_speed)
        return f'{string} {lon_speed}>'

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
        if abs(self.lon_speed) < 0.0003:
            return const.STATIONARY
        if self.lon_speed > 0:
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

    @property
    def is_benefic(self) -> bool:
        """ Returns True if the planet is a natural benefic (Jupiter, Venus). """
        return self.id in [const.JUPITER, const.VENUS]

    @property
    def is_malefic(self) -> bool:
        """ Returns True if the planet is a natural malefic (Saturn, Mars). """
        return self.id in [const.SATURN, const.MARS]

    @property
    def is_in_sect(self) -> bool:
        """
        Determines if the planet is in its preferred sect (Day/Night).
        Diurnal: Sun, Jupiter, Saturn | Nocturnal: Moon, Venus, Mars.
        """
        is_day = self.chart.is_diurnal()
        diurnal_planets = [const.SUN, const.JUPITER, const.SATURN]
        nocturnal_planets = [const.MOON, const.VENUS, const.MARS]

        if is_day and self.id in diurnal_planets:
            return True
        if not is_day and self.id in nocturnal_planets:
            return True
        return False

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
        return abs(self.lon_speed) >= self.mean_motion()

    def house(self) -> House:
        """ Returns the house of this object. """
        return self.chart.houses.get_object_house(self)

    # === Dignities === #

    def essential_dignities(self) -> EssentialInfo:
        """ Returns the essential dignities of this object. """
        return EssentialInfo(self)

    def accidental_dignities(self) -> AccidentalDignity:
        """ Returns the accidental dignities of this object. """
        return AccidentalDignity(self, self.chart)

    def describe(self) -> str:
        """ Provides a pedagogical summary of the planet's state. """
        ess = self.essential_dignities()
        acc = self.accidental_dignities()
        status = f"{self.id} in {self.sign}.\n"
        status += f"Sect: {'In Sect' if self.is_in_sect else 'Out of Sect'}.\n"
        status += f"Essential Dignities Score: {ess.score}.\n"
        status += f"Accidental Dignities Score: {acc.score()}."
        return status
    

# ------------------ #
#     House Cusp     #
# ------------------ #

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
        return props.house.condition[self.id]

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
        return props.house.gender[self.id]

    @property
    def meaning(self):
        """ Returns the meaning of this house. """
        return props.house.meaning[self.id]

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
