"""
Useful functions for handling aspects between objects in pyastra.
An aspect is an angular relation between a planet and another object.

This module has the following base terminology:
- Active/Passive object: The active object is the planet responsible for the aspect.
- Separation: the angular distance between the active and passive object.
- Orb: the orb distance (>0) between active and passive objects.
- Obj.orb: is the orb allowed by the aspect.
- Type: the type of the aspect.
- Direction/Condition/Movement/etc. are properties of an aspect.
- Movement: The objects have their movements, but the aspect movement can be also exact.

Major aspects must be within orb of one of the planets.
Minor aspects only when within a max allowed orb.

"""

from pyastra.core import angle
from pyastra import const

# Orb for minor and exact aspects
MAX_MINOR_ASP_ORB = 3
MAX_EXACT_ORB = 0.3


# === Private functions === #

def _raw_aspect(obj1, obj2, asp_list) -> dict | None:
    """ Returns a dictionary with the aspect type, orb, separation, and active/passive objects."""

    # Ignore same object
    if obj1.id == obj2.id:
        return None

    # Determine which object is the 'active' (faster) and which is the 'passive'
    speed1 = abs(obj1.lon_speed) if obj1.is_planet() else -1.0
    speed2 = abs(obj2.lon_speed) if obj2.is_planet() else -1.0
    active, passive = (obj1, obj2) if speed1 > speed2 else (obj2, obj1)

    # Only planets can be active objects
    if active.id in [const.SYZYGY, const.NORTH_NODE, const.SOUTH_NODE, const.PARS_FORTUNA]:
        return None

    # Calculate angular separation
    separation = angle.closest_distance(active.lon, passive.lon)
    abs_sep = abs(separation)

    # Find the best match for the aspect type
    for asp_type in asp_list:
        asp_orb = abs(abs_sep - asp_type)

        # Check aspect orb
        if asp_type in const.MAJOR_ASPECTS:
            # For major aspects ignore aspects out of orb
            if asp_orb > active.orb() and asp_orb > passive.orb():
                continue
        else:
            # For minor aspects ignore aspects out of max orb
            if asp_orb > MAX_MINOR_ASP_ORB:
                continue

        # Return valid aspect within orb
        return {
            'asp_type': asp_type,
            'asp_orb': asp_orb,
            'separation': separation,
            'active': active,
            'passive': passive
        }

    return None


def _aspect_properties(asp_dict):
    """ Returns the properties of an aspect given by the 'asp_dict'. """

    asp_type = asp_dict['asp_type']
    asp_orb = asp_dict['asp_orb']
    sep = asp_dict['separation']
    active = asp_dict['active']
    passive = asp_dict['passive']

    # Properties
    props_active = {
        'id': active.id,
        'in_orb': False,
        'movement': const.NO_MOVEMENT
    }
    props_passive = {
        'id': passive.id,
        'in_orb': False,
        'movement': const.NO_MOVEMENT
    }
    props = {
        'asp_type': asp_type,
        'asp_orb': asp_orb,
        'direction': -1,
        'condition': -1,
        'active': props_active,
        'passive': props_passive
    }

    if asp_type == const.NO_ASPECT:
        return props

    # Aspect within orb
    props_active['in_orb'] = asp_orb <= active.orb()
    props_passive['in_orb'] = asp_orb <= passive.orb()

    # Direction
    props['direction'] = const.DEXTER if sep <= 0 else const.SINISTER

    # Sign conditions
    # Note: if obj1 is before obj2, orb_dir will be less than zero
    orb_dir = sep - asp_type if sep >= 0 else sep + asp_type
    offset = active.signlon + orb_dir
    if 0 <= offset < 30:
        props['condition'] = const.ASSOCIATE
    else:
        props['condition'] = const.DISSOCIATE

        # Movement of the individual objects
    if abs(orb_dir) < MAX_EXACT_ORB:
        props_active['movement'] = props_passive['movement'] = const.EXACT
    else:
        # Active object applies to Passive if it is before
        # and direct, or after the Passive and Rx.
        props_active['movement'] = const.SEPARATIVE
        if (orb_dir > 0 and active.is_direct()) or \
                (orb_dir < 0 and active.is_retrograde()):
            props_active['movement'] = const.APPLICATIVE
        elif active.is_stationary():
            props_active['movement'] = const.STATIONARY

        # The Passive applies or separates from the Active
        # if it has a different direction..
        # Note: Non-planets have zero speed
        props_passive['movement'] = const.NO_MOVEMENT
        obj2speed = passive.lon_speed if passive.is_planet() else 0.0
        same_dir = active.lon_speed * obj2speed >= 0
        if not same_dir:
            props_passive['movement'] = props_active['movement']

    return props


# === Public functions === #

def aspect_type(obj1, obj2, asp_list):
    """ Returns the aspect type between objects considering a list of possible aspects. """
    asp_dict = _raw_aspect(obj1, obj2, asp_list)
    return asp_dict['asp_type'] if asp_dict else const.NO_ASPECT


def has_aspect(obj1, obj2, asp_list):
    """
    Returns if there is an aspect between objects considering a list of possible aspects.
    """
    asp_type = aspect_type(obj1, obj2, asp_list)
    return asp_type != const.NO_ASPECT


def is_aspecting(obj1, obj2, asp_list):
    """ Returns if obj1 aspects obj2 within orb, considering a list of possible aspects. """
    asp_dict = _raw_aspect(obj1, obj2, asp_list)
    if asp_dict:
        return asp_dict['asp_orb'] < obj1.orb()
    return False


def get_aspect(obj1, obj2, asp_list):
    """ Builds an Aspect from two objects considering a list of possible aspects. """
    return Aspect.from_objects(obj1, obj2, asp_list)


# ---------------- #
#   Aspect Class   #
# ---------------- #

class AspectObject:
    """
    Dummy class to represent the Active and Passive objects and to allow access to their
    properties using the dot notation.
    
    """

    def __init__(self, properties):
        self.id = None
        self.movement = None
        self.in_orb = None
        self.__dict__.update(properties)


class Aspect:
    """ This class represents an aspect with all its properties. """

    def __init__(self, properties):
        self.type = properties.get('asp_type', None)
        self.orb = properties.get('asp_orb', None)
        self.direction = properties.get('direction')
        self.condition = properties.get('condition')
        self.active = AspectObject(properties.get('active'))
        self.passive = AspectObject(properties.get('passive'))

    @classmethod
    def from_objects(cls, obj1, obj2, asp_list):
        """ Builds an Aspect from two objects within a list of possible aspects. """
        asp_dict = _raw_aspect(obj1, obj2, asp_list)
        if not asp_dict:
            asp_dict = {
                'asp_type': const.NO_ASPECT,
                'asp_orb': 0,
                'separation': 0,
                'active': obj1,
                'passive': obj2
            }
        asp_props = _aspect_properties(asp_dict)
        return Aspect(asp_props)

    def exists(self):
        """ Returns if this aspect is valid. """
        return self.type != const.NO_ASPECT

    def movement(self):
        """
        Returns the movement of this aspect.
        The movement is the one of the active object, except if the active is separating but within
        less than 1 degree.
        
        """
        mov = self.active.movement
        if self.orb < 1 and mov == const.SEPARATIVE:
            mov = const.EXACT
        return mov

    def mutual_aspect(self):
        """ Returns if both object are within aspect orb. """
        return self.active.in_orb == self.passive.in_orb == True

    def mutual_movement(self):
        """ Returns if both objects are mutually applying or separating. """
        return self.active.movement == self.passive.movement

    def get_role(self, obj_id):
        """ Returns the role (active or passive) of an object in this aspect. """
        if self.active.id == obj_id:
            return {
                'role': 'active',
                'in_orb': self.active.in_orb,
                'movement': self.active.movement
            }
        if self.passive.id == obj_id:
            return {
                'role': 'passive',
                'in_orb': self.passive.in_orb,
                'movement': self.passive.movement
            }
        return None

    def in_orb(self, obj_id):
        """ Returns if the object (given by ID) is within orb in the Aspect. """
        role = self.get_role(obj_id)
        return role['in_orb'] if role else None

    def __str__(self):
        return '<%s %s %s %s %s>' % (self.active.id,
                                     self.passive.id,
                                     self.type,
                                     self.active.movement,
                                     angle.to_string(self.orb))
