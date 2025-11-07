"""
This module provides useful functions for handling essential dignities. It provides easy access to
an essential dignity table, functions for retrieving information from the table and to compute
scores and almutems.

"""

from pyastra import const
from . import tables

# Face variants
CHALDEAN_FACES = 'Chaldean Faces'
TRIPLICITY_FACES = 'Triplicity Faces'

# Term variants
EGYPTIAN_TERMS = 'Egyptian Terms'
TETRABIBLOS_TERMS = 'Tetrabiblos Terms'
LILLY_TERMS = 'Lilly Terms'

# Defaults
FACES = tables.CHALDEAN_FACES
TERMS = tables.EGYPTIAN_TERMS
TABLE = tables.ESSENTIAL_DIGNITIES


def set_faces(variant):
    """ Sets the default faces variant. """
    global FACES
    if variant == CHALDEAN_FACES:
        FACES = tables.CHALDEAN_FACES
    else:
        FACES = tables.TRIPLICITY_FACES


def set_terms(variant):
    """ Sets the default terms of the Dignities table. """
    global TERMS
    if variant == EGYPTIAN_TERMS:
        TERMS = tables.EGYPTIAN_TERMS
    elif variant == TETRABIBLOS_TERMS:
        TERMS = tables.TETRABIBLOS_TERMS
    elif variant == LILLY_TERMS:
        TERMS = tables.LILLY_TERMS


# === Table properties === #

def ruler(sign):
    """ Returns the ruler of the sign. """
    return TABLE[sign]['ruler']


def exalt(sign):
    """ Returns the exaltation. """
    return TABLE[sign]['exalt'][0]


def exalt_deg(sign):
    """ Returns the exaltation degree. """
    return TABLE[sign]['exalt'][1]


def day_trip(sign):
    """ Returns the diurnal triplicity. """
    return TABLE[sign]['trip'][0]


def night_trip(sign):
    """ Returns the nocturnal triplicity. """
    return TABLE[sign]['trip'][1]


def part_trip(sign):
    """ Returns the participant triplicity. """
    return TABLE[sign]['trip'][2]


def exile(sign):
    """ Returns the exile. """
    return TABLE[sign]['exile']


def fall(sign):
    """ Returns the fall. """
    return TABLE[sign]['fall'][0]


def fall_deg(sign):
    """ Returns the fall degree. """
    return TABLE[sign]['fall'][1]


def term(sign, lon):
    """ Returns the term for a sign and longitude. """
    terms = TERMS[sign]
    for (obj_id, a, b) in terms:
        if a <= lon < b:
            return obj_id
    return None


def face(sign, lon):
    """ Returns the face for a sign and longitude. """
    faces = FACES[sign]
    if lon < 10:
        return faces[0]
    if lon < 20:
        return faces[1]
    return faces[2]


# === Complex properties === #

def get_info(sign, lon):
    """ Returns the complete essential dignities for a sign and longitude. """
    return {
        'ruler': ruler(sign),
        'exalt': exalt(sign),
        'dayTrip': day_trip(sign),
        'nightTrip': night_trip(sign),
        'partTrip': part_trip(sign),
        'term': term(sign, lon),
        'face': face(sign, lon),
        'exile': exile(sign),
        'fall': fall(sign)
    }


def is_peregrine(ID, sign, lon):
    """ Returns if an object is peregrine on a sign and longitude. """
    info = get_info(sign, lon)
    for dign, obj_id in info.items():
        if dign not in ['exile', 'fall'] and ID == obj_id:
            return False
    return True


# === Scores === #

SCORES = {
    'ruler': 5,
    'exalt': 4,
    'dayTrip': 3,
    'nightTrip': 3,
    'partTrip': 3,
    'term': 2,
    'face': 1,
    'fall': -4,
    'exile': -5,
}


def score(obj_id, sign, lon):
    """ Returns the score of an object on a sign and longitude. """
    info = get_info(sign, lon)
    dignities = [dign for (dign, objID) in info.items() if objID == obj_id]
    return sum([SCORES[dign] for dign in dignities])


def almutem(sign, lon):
    """ Returns the almutem for a given sign and longitude. """
    planets = const.LIST_SEVEN_PLANETS
    res = [None, 0]
    for obj_id in planets:
        sc = score(obj_id, sign, lon)
        if sc > res[1]:
            res = [obj_id, sc]
    return res[0]


# ----------------------- #
#   EssentialInfo Class   #
# ----------------------- #

class EssentialInfo:
    """ This class represents the Essential dignities information for a given object. """

    def __init__(self, obj):
        self.obj = obj
        # Include info in instance properties
        info = get_info(obj.sign, obj.signlon)
        self.__dict__.update(info)
        # Add score and almutem
        self.score = score(obj.id, obj.sign, obj.signlon)
        self.almutem = almutem(obj.sign, obj.signlon)

    def get_info(self):
        """ Returns the essential dignities for this object. """
        return get_info(self.obj.sign, self.obj.signlon)

    def get_dignities(self):
        """ Returns the dignities belonging to this object. """
        info = self.get_info()
        dignities = [dign for (dign, objID) in info.items()
                     if objID == self.obj.id]
        return dignities

    def is_peregrine(self):
        """ Returns if this object is peregrine. """
        return is_peregrine(self.obj.id, self.obj.sign, self.obj.signlon)
