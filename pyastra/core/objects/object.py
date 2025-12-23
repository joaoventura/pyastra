"""
This module implements the Object class.
Objects are astrology objects such as planets, lunar nodes, arabic parts, and others.

"""

from pyastra import const
from pyastra import definitions
from pyastra.core import angle
from pyastra.core.aspects import Aspect
from pyastra.core.objects.generic import GenericObject
from pyastra.core.objects.house import House
from pyastra.dignities.accidental import AccidentalDignity
from pyastra.dignities.essential import EssentialInfo


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
        return definitions.planets.ORB[self.id]

    def mean_motion(self):
        """ Returns the mean daily motion of this object. """
        return definitions.planets.MEAN_MOTION[self.id]

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
        return definitions.planets.GENDER[self.id]

    def faction(self):
        """ Returns the faction of this object. """
        return definitions.planets.FACTION[self.id]

    def element(self):
        """ Returns the element of this object. """
        return definitions.planets.ELEMENT[self.id]

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

    # === Aspects === #

    def get_aspect(self, other, asp_list=const.MAJOR_ASPECTS):
        """ Returns the aspect between this object and another. """
        return Aspect.from_objects(self, other, asp_list)
