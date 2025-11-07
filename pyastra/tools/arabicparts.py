"""
This module provides useful functions for computing Arabic Parts.
  
"""

from pyastra import const
from pyastra.object import GenericObject
from pyastra.dignities import essential

# Define arabic parts
PARS_FORTUNA = const.PARS_FORTUNA
PARS_SPIRIT = 'Pars Spirit'
PARS_FAITH = 'Pars Faith'
PARS_SUBSTANCE = 'Pars Substance'
PARS_WEDDING_MALE = 'Pars Wedding [Male]'
PARS_WEDDING_FEMALE = 'Pars Wedding [Female]'
PARS_SONS = 'Pars Sons'
PARS_FATHER = 'Pars Father'
PARS_MOTHER = 'Pars Mother'
PARS_BROTHERS = 'Pars Brothers'
PARS_DISEASES = 'Pars Diseases'
PARS_DEATH = 'Pars Death'
PARS_TRAVEL = 'Pars Travel'
PARS_FRIENDS = 'Pars Friends'
PARS_ENEMIES = 'Pars Enemies'
PARS_SATURN = 'Pars Saturn'
PARS_JUPITER = 'Pars Jupiter'
PARS_MARS = 'Pars Mars'
PARS_VENUS = 'Pars Venus'
PARS_MERCURY = 'Pars Mercury'
PARS_HORSEMANSHIP = 'Pars Horsemanship'  # aka Bravery

# Define Diurnal and Nocturnal formulas as "Distance of A to B projected from C".
# Note that '$R' stands for the Ruler of something
FORMULAS = {
    PARS_FORTUNA: [
        [const.SUN, const.MOON, const.ASC],  # Diurnal
        [const.MOON, const.SUN, const.ASC]  # Nocturnal
    ],
    PARS_SPIRIT: [
        [const.MOON, const.SUN, const.ASC],
        [const.SUN, const.MOON, const.ASC]
    ],
    PARS_FAITH: [
        [const.MOON, const.MERCURY, const.ASC],
        [const.MERCURY, const.MOON, const.ASC]
    ],
    PARS_SUBSTANCE: [
        ['$R' + const.HOUSE2, const.HOUSE2, const.ASC],
        ['$R' + const.HOUSE2, const.HOUSE2, const.ASC]
    ],
    PARS_WEDDING_MALE: [
        [const.SATURN, const.VENUS, const.ASC],
        [const.SATURN, const.VENUS, const.ASC]
    ],
    PARS_WEDDING_FEMALE: [
        [const.VENUS, const.SATURN, const.ASC],
        [const.VENUS, const.SATURN, const.ASC]
    ],
    PARS_SONS: [
        [const.JUPITER, const.SATURN, const.ASC],
        [const.SATURN, const.JUPITER, const.ASC]
    ],
    PARS_FATHER: [
        [const.SUN, const.SATURN, const.ASC],
        [const.SATURN, const.SUN, const.ASC]
    ],
    PARS_MOTHER: [
        [const.VENUS, const.MOON, const.ASC],
        [const.MOON, const.VENUS, const.ASC]
    ],
    PARS_BROTHERS: [
        [const.SATURN, const.JUPITER, const.ASC],
        [const.SATURN, const.JUPITER, const.ASC]
    ],
    PARS_DISEASES: [
        [const.SATURN, const.MARS, const.ASC],
        [const.MARS, const.SATURN, const.ASC]
    ],
    PARS_DEATH: [
        [const.MOON, const.HOUSE8, const.SATURN],
        [const.MOON, const.HOUSE8, const.SATURN]
    ],
    PARS_TRAVEL: [
        ['$R' + const.HOUSE9, const.HOUSE9, const.ASC],
        ['$R' + const.HOUSE9, const.HOUSE9, const.ASC]
    ],
    PARS_FRIENDS: [
        [const.MOON, const.MERCURY, const.ASC],
        [const.MOON, const.MERCURY, const.ASC]
    ],
    PARS_ENEMIES: [
        ['$R' + const.HOUSE12, const.HOUSE12, const.ASC],
        ['$R' + const.HOUSE12, const.HOUSE12, const.ASC]
    ],
    PARS_SATURN: [
        [const.SATURN, const.PARS_FORTUNA, const.ASC],
        [const.PARS_FORTUNA, const.SATURN, const.ASC]
    ],
    PARS_JUPITER: [
        [PARS_SPIRIT, const.JUPITER, const.ASC],
        [const.JUPITER, PARS_SPIRIT, const.ASC]
    ],
    PARS_MARS: [
        [const.MARS, const.PARS_FORTUNA, const.ASC],
        [const.PARS_FORTUNA, const.MARS, const.ASC]
    ],
    PARS_VENUS: [
        [PARS_SPIRIT, const.VENUS, const.ASC],
        [const.VENUS, PARS_SPIRIT, const.ASC]
    ],
    PARS_MERCURY: [
        [const.MERCURY, const.PARS_FORTUNA, const.ASC],
        [const.PARS_FORTUNA, const.MERCURY, const.ASC]
    ],
    PARS_HORSEMANSHIP: [
        [const.SATURN, const.MOON, const.ASC],
        [const.MOON, const.SATURN, const.ASC]
    ]
}


# === Functions === #

def obj_lon(obj_id, chart):
    """ Returns the longitude of an object. """
    if obj_id.startswith('$R'):
        # Return Ruler
        obj_id = obj_id[2:]
        obj = chart.get(obj_id)
        ruler_id = essential.ruler(obj.sign)
        ruler = chart.get_object(ruler_id)
        return ruler.lon
    if obj_id.startswith('Pars'):
        # Return an arabic part
        return part_lon(obj_id, chart)

    # Return an object
    obj = chart.get(obj_id)
    return obj.lon


def part_lon(obj_id, chart):
    """ Returns the longitude of an arabic part. """
    # Get diurnal or nocturnal formula
    abc = FORMULAS[obj_id][0] if chart.is_diurnal() else FORMULAS[obj_id][1]
    a = obj_lon(abc[0], chart)
    b = obj_lon(abc[1], chart)
    c = obj_lon(abc[2], chart)
    return c + b - a


def get_part(obj_id, chart):
    """ Returns an Arabic Part. """
    obj = GenericObject()
    obj.id = obj_id
    obj.type = const.OBJ_ARABIC_PART
    obj.relocate(part_lon(obj_id, chart))
    return obj
