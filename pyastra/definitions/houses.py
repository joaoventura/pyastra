"""
House properties

"""

from pyastra import const
from pyastra.definitions import base


_houses = const.LIST_HOUSES

# House conditions
CONDITION = dict(zip(_houses, [const.ANGULAR, const.SUCCEDENT, const.CADENT] * 4))

# House genders
GENDER = dict(zip(_houses, base.GENDERS * 4))

# Houses above and below horizon
ABOVE_HORIZON = [
    const.HOUSE7, const.HOUSE8, const.HOUSE9, const.HOUSE10, const.HOUSE11, const.HOUSE12
]

BELOW_HORIZON = [
    const.HOUSE1, const.HOUSE2, const.HOUSE3, const.HOUSE4, const.HOUSE5, const.HOUSE6
]

# House meanings
MEANING = {
    const.HOUSE1: "Life, vitality, the physical body, appearance, and temperament.",
    const.HOUSE2: "Financial resources, movable possessions, sustenance, and personal values.",
    const.HOUSE3: "Siblings, communication, short journeys, and primary education.",
    const.HOUSE4: "Father, home, roots, real estate, and the end of all things.",
    const.HOUSE5: "Children, pleasures, creativity, romance, and investments.",
    const.HOUSE6: "Illness, subordinate work, small animals, and daily routine.",
    const.HOUSE7: "Partnerships, marriage, open enemies, and the 'other'.",
    const.HOUSE8: "Death, inheritance, other people's money, and transformative crises.",
    const.HOUSE9: "Religion, philosophy, long journeys, higher education, and divinity.",
    const.HOUSE10: "Career, honor, destiny, the mother, and public recognition.",
    const.HOUSE11: "Friends, hopes, protectors, and social groups.",
    const.HOUSE12: "Hidden enemies, isolation, large animals, and self-undoing."
}