"""
Provide useful for handling aspects between objects in pyastra. An aspect is an angular relation
between a planet and another object.

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

In parameters, objA is the active object and objP is the passive object.

"""

from . import angle
from . import const

# Orb for minor and exact aspects
MAX_MINOR_ASP_ORB = 3
MAX_EXACT_ORB = 0.3


# === Private functions === #

def _orb_list(obj1, obj2, asp_list):
    """
    Returns a list with the orb and angular distances from obj1 to obj2, considering a
    list of possible aspects. 
    
    """
    sep = angle.closest_distance(obj1.lon, obj2.lon)
    abs_sep = abs(sep)
    return [
        {
            'type': asp,
            'orb': abs(abs_sep - asp),
            'separation': sep,
        } for asp in asp_list
    ]


def _aspect_dict(obj1, obj2, asp_list):
    """
    Returns the properties of the aspect of obj1 to obj2, considering a list of possible aspects.
    
    This function makes the following assumptions:
    - Syzygy does not start aspects but receives any aspect.
    - Pars Fortuna and Moon Nodes only starts conjunctions but receive any aspect.
    - All other objects can start and receive any aspect.
      
    Note: this function returns the aspect even if it is not within the orb of obj1
    (but is within the orb of obj2).
    
    """
    # Ignore aspects from same object and Syzygy
    if obj1 == obj2 or obj1.id == const.SYZYGY:
        return None

    orbs = _orb_list(obj1, obj2, asp_list)
    for asp_dict in orbs:
        asp = asp_dict['type']
        orb = asp_dict['orb']

        # Check if aspect is within orb
        if asp in const.MAJOR_ASPECTS:
            # Ignore major aspects out of orb
            if obj1.orb() < orb and obj2.orb() < orb:
                continue
        else:
            # Ignore minor aspects out of max orb
            if MAX_MINOR_ASP_ORB < orb:
                continue

        # Only conjunctions for Pars Fortuna and Nodes
        if obj1.id in [const.PARS_FORTUNA,
                       const.NORTH_NODE,
                       const.SOUTH_NODE] and \
                asp != const.CONJUNCTION:
            continue

        # We have a valid aspect within orb
        return asp_dict

    return None


def _aspect_properties(obj1, obj2, asp_dict):
    """
    Returns the properties of an aspect between obj1 and obj2, given by 'asp_dict'.
    This function assumes obj1 to be the active object, i.e., the one responsible for starting the
    aspect.
    
    """
    orb = asp_dict['orb']
    asp = asp_dict['type']
    sep = asp_dict['separation']

    # Properties
    prop1 = {
        'id': obj1.id,
        'inOrb': False,
        'movement': const.NO_MOVEMENT
    }
    prop2 = {
        'id': obj2.id,
        'inOrb': False,
        'movement': const.NO_MOVEMENT
    }
    prop = {
        'type': asp,
        'orb': orb,
        'direction': -1,
        'condition': -1,
        'active': prop1,
        'passive': prop2
    }

    if asp == const.NO_ASPECT:
        return prop

    # Aspect within orb
    prop1['inOrb'] = orb <= obj1.orb()
    prop2['inOrb'] = orb <= obj2.orb()

    # Direction
    prop['direction'] = const.DEXTER if sep <= 0 else const.SINISTER

    # Sign conditions
    # Note: if obj1 is before obj2, orb_dir will be less than zero
    orb_dir = sep - asp if sep >= 0 else sep + asp
    offset = obj1.signlon + orb_dir
    if 0 <= offset < 30:
        prop['condition'] = const.ASSOCIATE
    else:
        prop['condition'] = const.DISSOCIATE

        # Movement of the individual objects
    if abs(orb_dir) < MAX_EXACT_ORB:
        prop1['movement'] = prop2['movement'] = const.EXACT
    else:
        # Active object applies to Passive if it is before 
        # and direct, or after the Passive and Rx.
        prop1['movement'] = const.SEPARATIVE
        if (orb_dir > 0 and obj1.isDirect()) or \
                (orb_dir < 0 and obj1.isRetrograde()):
            prop1['movement'] = const.APPLICATIVE
        elif obj1.isStationary():
            prop1['movement'] = const.STATIONARY

        # The Passive applies or separates from the Active 
        # if it has a different direction..
        # Note: Non-planets have zero speed
        prop2['movement'] = const.NO_MOVEMENT
        obj2speed = obj2.lonspeed if obj2.isPlanet() else 0.0
        sameDir = obj1.lonspeed * obj2speed >= 0
        if not sameDir:
            prop2['movement'] = prop1['movement']

    return prop


def _get_active_passive(obj1, obj2):
    """ Returns which is the active and the passive objects. """
    speed1 = abs(obj1.lonspeed) if obj1.isPlanet() else -1.0
    speed2 = abs(obj2.lonspeed) if obj2.isPlanet() else -1.0
    if speed1 > speed2:
        return {
            'active': obj1,
            'passive': obj2
        }
    else:
        return {
            'active': obj2,
            'passive': obj1
        }


# === Public functions === #

def aspect_type(obj1, obj2, asp_list):
    """ Returns the aspect type between objects consideringa list of possible aspect types. """
    ap = _get_active_passive(obj1, obj2)
    asp_dict = _aspect_dict(ap['active'], ap['passive'], asp_list)
    return asp_dict['type'] if asp_dict else const.NO_ASPECT


def has_aspect(obj1, obj2, asp_list):
    """
    Returns if there is an aspect between objects considering a list of possible aspect types.

    """
    asp_type = aspect_type(obj1, obj2, asp_list)
    return asp_type != const.NO_ASPECT


def is_aspecting(obj1, obj2, asp_list):
    """ Returns if obj1 aspects obj2 within its orb, considering a list of possible aspect types. """
    asp_dict = _aspect_dict(obj1, obj2, asp_list)
    if asp_dict:
        return asp_dict['orb'] < obj1.orb()
    return False


def get_aspect(obj1, obj2, asp_list):
    """
    Returns an Aspect object for the aspect between two objects considering a list of possible
    aspect types.
    
    """
    ap = _get_active_passive(obj1, obj2)
    asp_dict = _aspect_dict(ap['active'], ap['passive'], asp_list)
    if not asp_dict:
        asp_dict = {
            'type': const.NO_ASPECT,
            'orb': 0,
            'separation': 0,
        }
    asp_prop = _aspect_properties(ap['active'], ap['passive'], asp_dict)
    return Aspect(asp_prop)


# ---------------- #
#   Aspect Class   #
# ---------------- #

class AspectObject:
    """
    Dummy class to represent the Active and Passive objects and to allow access to their
    properties using the dot notation.
    
    """

    def __init__(self, properties):
        self.__dict__.update(properties)


class Aspect:
    """ This class represents an aspect with all its properties. """

    def __init__(self, properties):
        self.__dict__.update(properties)
        self.active = AspectObject(self.active)
        self.passive = AspectObject(self.passive)

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
        return self.active.inOrb == self.passive.inOrb == True

    def mutual_movement(self):
        """ Returns if both objects are mutually applying or
        separating.
        
        """
        return self.active.movement == self.passive.movement

    def get_role(self, ID):
        """ Returns the role (active or passive) of an object
        in this aspect.
        
        """
        if self.active.id == ID:
            return {
                'role': 'active',
                'inOrb': self.active.inOrb,
                'movement': self.active.movement
            }
        elif self.passive.id == ID:
            return {
                'role': 'passive',
                'inOrb': self.passive.inOrb,
                'movement': self.passive.movement
            }
        return None

    def in_orb(self, ID):
        """ Returns if the object (given by ID) is within orb
        in the Aspect.
        
        """
        role = self.get_role(ID)
        return role['inOrb'] if role else None

    def __str__(self):
        return '<%s %s %s %s %s>' % (self.active.id,
                                     self.passive.id,
                                     self.type,
                                     self.active.movement,
                                     angle.to_string(self.orb))
