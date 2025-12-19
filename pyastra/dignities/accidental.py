"""
This module implements some utility functions for handling the accidental dignities of an Astrology
Chart.
  
"""

from copy import copy

from pyastra import const
from pyastra.core import aspects, props, angle
from pyastra.dignities import essential
from pyastra.tools.chartdynamics import ChartDynamics

# Relations with Sun
COMBUST = 'Combust'
CAZIMI = 'Cazimi'
UNDER_SUN = 'Under the Sun'

# Light
LIGHT_AUGMENTING = 'Augmenting Light'
LIGHT_DIMINISHING = 'Diminishing Light'

# Orientality
ORIENTAL = 'Oriental'
OCCIDENTAL = 'Occidental'

# Haiz
HAIZ = 'Haiz'
CHAIZ = 'Contra-Haiz'


# === Base functions === #

def sun_relation(obj, sun):
    """ Returns an object's relation with the sun. """
    if obj.id == const.SUN:
        return None
    dist = abs(angle.closest_distance(sun.lon, obj.lon))
    if dist < 0.2833:
        return CAZIMI
    if dist < 8.0:
        return COMBUST
    if dist < 16.0:
        return UNDER_SUN
    return None


def light(obj, sun):
    """ Returns if an object is augmenting or diminishing light. """
    dist = angle.distance(sun.lon, obj.lon)
    faster = sun if sun.lon_speed > obj.lon_speed else obj
    if faster == sun:
        return LIGHT_DIMINISHING if dist < 180 else LIGHT_AUGMENTING
    return LIGHT_AUGMENTING if dist < 180 else LIGHT_DIMINISHING


def orientality(obj, sun):
    """ Returns if an object is oriental or occidental to the sun. """
    dist = angle.distance(sun.lon, obj.lon)
    return OCCIDENTAL if dist < 180 else ORIENTAL


def via_combusta(obj):
    """ Returns if an object is in the Via Combusta. """
    return 195 < obj.lon < 225


def haiz(obj, chart):
    """ Returns if an object is in Haiz. """
    obj_gender = obj.gender()
    obj_faction = obj.faction()

    if obj.id == const.MERCURY:
        # Gender and faction of mercury depends on orientality
        sun = chart.get_object(const.SUN)
        orientality_mercury = orientality(obj, sun)
        if orientality_mercury == ORIENTAL:
            obj_gender = const.MASCULINE
            obj_faction = const.DIURNAL
        else:
            obj_gender = const.FEMININE
            obj_faction = const.NOCTURNAL

    # Object gender match sign gender?
    sign_gender = props.sign.gender[obj.sign]
    gender_conformity = obj_gender == sign_gender

    # Match faction
    faction_conformity = False
    diurnal_chart = chart.is_diurnal()

    if obj.id == const.SUN and not diurnal_chart:
        # Sun is in conformity only when above horizon
        faction_conformity = False
    else:
        # Get list of houses in the chart's diurnal faction
        if diurnal_chart:
            diurnal_faction = props.house.aboveHorizon
            nocturnal_faction = props.house.belowHorizon
        else:
            diurnal_faction = props.house.belowHorizon
            nocturnal_faction = props.house.aboveHorizon

        # Get the object's house and match factions
        obj_house = chart.houses.get_object_house(obj)
        if (obj_faction == const.DIURNAL and obj_house.id in diurnal_faction or
                obj_faction == const.NOCTURNAL and obj_house.id in nocturnal_faction):
            faction_conformity = True

    # Match things
    if gender_conformity and faction_conformity:
        return HAIZ
    if not gender_conformity and not faction_conformity:
        return CHAIZ
    return None


# ---------------------------- #
#   Accidental Dignity Class   #
# ---------------------------- #

# House scores
HOUSE_SCORES = {
    const.HOUSE1: 5,
    const.HOUSE2: 3,
    const.HOUSE3: 1,
    const.HOUSE4: 4,
    const.HOUSE5: 3,
    const.HOUSE6: -3,
    const.HOUSE7: 4,
    const.HOUSE8: -4,
    const.HOUSE9: 2,
    const.HOUSE10: 5,
    const.HOUSE11: 4,
    const.HOUSE12: -5,
}


class AccidentalDignity:
    """ This class provides methods to access the accidental dignities of an object in a Chart. """

    def __init__(self, obj, chart):
        self.obj = obj
        self.chart = chart
        self.dyn = ChartDynamics(chart)
        self.score_properties = None

    # === Houses === #

    def house(self):
        """ Returns the object's house. """
        house = self.chart.houses.get_object_house(self.obj)
        return house

    def house_score(self):
        """ Returns the score of the object's house. """
        house = self.house()
        return HOUSE_SCORES[house.id]

    # === Relation with Sun === #

    def sun_relation(self):
        """ Returns the relation of the object with the sun. """
        sun = self.chart.get_object(const.SUN)
        return sun_relation(self.obj, sun)

    def is_cazimi(self):
        """ Is object cazimi. """
        return self.sun_relation() == CAZIMI

    def is_under_sun(self):
        """ Is object under the sun. """
        return self.sun_relation() == UNDER_SUN

    def is_combust(self):
        """ Is object combust. """
        return self.sun_relation() == COMBUST

    def light(self):
        """ Returns if object is augmenting or diminishing its light. """
        sun = self.chart.get_object(const.SUN)
        return light(self.obj, sun)

    def is_augmenting_light(self):
        """ Returns if object is augmenting of light. """
        return self.light() == LIGHT_AUGMENTING

    def orientality(self):
        """ Returns the orientality of the object. """
        sun = self.chart.get_object(const.SUN)
        return orientality(self.obj, sun)

    def is_oriental(self):
        """ Return if object is oriental. """
        return self.orientality() == ORIENTAL

    # === Joys === #

    def in_house_joy(self):
        """ Returns if the object is in its house of joy. """
        house = self.house()
        return props.object.houseJoy[self.obj.id] == house.id

    def in_sign_joy(self):
        """ Returns if the object is in its sign of joy. """
        return props.object.signJoy[self.obj.id] == self.obj.sign

    # === Mutual Receptions === #

    def re_mutual_receptions(self):
        """
        Returns all mutual receptions with the object and other planets, indexed by planet ID.
        It only includes ruler and exaltation receptions.
        
        """
        planets = copy(const.LIST_SEVEN_PLANETS)
        planets.remove(self.obj.id)
        mrs = {}
        for obj_id in planets:
            mr = self.dyn.re_mutual_receptions(self.obj.id, obj_id)
            if mr:
                mrs[obj_id] = mr
        return mrs

    def eq_mutual_receptions(self):
        """
        Returns a list with mutual receptions with the object and other planets, when the reception
        is the same for both (both ruler or both exaltation).
        
        It basically returns a list with every ruler-ruler and exalt-exalt mutual receptions
        
        """
        mrs = self.re_mutual_receptions()
        res = []
        for _, receptions in mrs.items():
            for pair in receptions:
                if pair[0] == pair[1]:
                    res.append(pair[0])
        return res

    # === Aspects to benefics and malefics === #

    def __aspect_lists(self, ids, asp_list):
        """
        Returns a list with the aspects that the object makes to the objects in ids. It considers
        only conjunctions and other exact/applicative aspects if in aspList.
        
        """
        res = []

        for other_id in ids:
            # Ignore same
            if other_id == self.obj.id:
                continue

            # Get aspects to the other object
            other_obj = self.chart.get_object(other_id)
            asp = aspects.get_aspect(self.obj, other_obj, asp_list)

            if asp.type == const.NO_ASPECT:
                continue
            if asp.type == const.CONJUNCTION:
                res.append(asp.type)
            else:
                # Only exact or applicative aspects
                movement = asp.movement()
                if movement in [const.EXACT, const.APPLICATIVE]:
                    res.append(asp.type)

        return res

    def aspect_benefics(self):
        """ Returns a list with the good aspects the object makes to the benefics. """
        benefics = [const.VENUS, const.JUPITER]
        return self.__aspect_lists(benefics, asp_list=[0, 60, 120])

    def aspect_malefics(self):
        """ Returns a list with the bad aspects the object makes to the malefics. """
        malefics = [const.MARS, const.SATURN]
        return self.__aspect_lists(malefics, asp_list=[0, 90, 180])

    # == Application and Separation from benefics and malefics == #

    def __sep_app(self, ids, asp_list):
        """
        Returns true if the object last and next movement are separations and applications to
        objects in list IDs. It only considers aspects in asp_list.
        
        This function is static since it does not test if the next application will be indeed
        perfected. It considers only a snapshot of the chart and not its astronomical movement.
        
        """
        sep, app = self.dyn.immediate_aspects(self.obj.id, asp_list)
        if sep is None or app is None:
            return False
        sep_condition = sep['id'] in ids
        app_condition = app['id'] in ids
        return sep_condition == app_condition == True

    def is_auxilied(self):
        """
        Returns if the object is separating and applying to a benefic considering good aspects.
        
        """
        benefics = [const.VENUS, const.JUPITER]
        return self.__sep_app(benefics, asp_list=[0, 60, 120])

    def is_surrounded(self):
        """ Returns if the object is separating and applying to a malefic with bad aspects. """
        malefics = [const.MARS, const.SATURN]
        return self.__sep_app(malefics, asp_list=[0, 90, 180])

    # === Aspects to Moon Nodes === #

    def is_conj_north_node(self):
        """ Returns if object is conjunct north node. """
        node = self.chart.get_object(const.NORTH_NODE)
        return aspects.has_aspect(self.obj, node, asp_list=[0])

    def is_conj_south_node(self):
        """ Returns if object is conjunct south node. """
        node = self.chart.get_object(const.SOUTH_NODE)
        return aspects.has_aspect(self.obj, node, asp_list=[0])

    # === Void of Course, Feral and Haiz === #

    def is_voc(self):
        """ Return if the object is Void of Course. """
        return self.dyn.is_voc(self.obj.id)

    def is_feral(self):
        """ Returns true if the object does not have any aspects. """
        planets = copy(const.LIST_SEVEN_PLANETS)
        planets.remove(self.obj.id)
        for other_id in planets:
            other_obj = self.chart.get_object(other_id)
            if aspects.has_aspect(self.obj, other_obj, const.MAJOR_ASPECTS):
                return False
        return True

    def haiz(self):
        """ Returns the object haiz. """
        return haiz(self.obj, self.chart)

    # === Scores === #

    def get_score_properties(self):
        """ Returns the accidental dignity score of the object as dict. """
        obj = self.obj
        score = {}

        # Peregrine
        is_peregrine = essential.is_peregrine(obj.id, obj.sign, obj.signlon)
        score['peregrine'] = -5 if is_peregrine else 0

        # Ruler-Ruler and Exalt-Exalt mutual receptions
        mr = self.eq_mutual_receptions()
        score['mr_ruler'] = +5 if 'ruler' in mr else 0
        score['mr_exalt'] = +4 if 'exalt' in mr else 0

        # House scores
        score['house'] = self.house_score()

        # Joys
        score['joy_sign'] = +3 if self.in_sign_joy() else 0
        score['joy_house'] = +2 if self.in_house_joy() else 0

        # Relations with sun
        score['cazimi'] = +5 if self.is_cazimi() else 0
        score['combust'] = -6 if self.is_combust() else 0
        score['under_sun'] = -4 if self.is_under_sun() else 0
        score['no_under_sun'] = 0
        if obj.id != const.SUN and not self.sun_relation():
            score['no_under_sun'] = +5

        # Light
        score['light'] = 0
        if obj.id != const.SUN:
            score['light'] = +1 if self.is_augmenting_light() else -1

        # Orientality
        score['orientality'] = 0
        if obj.id in [const.SATURN, const.JUPITER, const.MARS]:
            score['orientality'] = +2 if self.is_oriental() else -2
        elif obj.id in [const.VENUS, const.MERCURY, const.MOON]:
            score['orientality'] = -2 if self.is_oriental() else +2

        # Moon nodes
        score['north_node'] = -3 if self.is_conj_north_node() else 0
        score['south_node'] = -5 if self.is_conj_south_node() else 0

        # Direction and speed
        score['direction'] = 0
        if obj.id not in [const.SUN, const.MOON]:
            score['direction'] = +4 if obj.is_direct() else -5
        score['speed'] = +2 if obj.is_fast() else -2

        # Aspects to benefics
        asp_ben = self.aspect_benefics()
        score['benefic_asp0'] = +5 if const.CONJUNCTION in asp_ben else 0
        score['benefic_asp120'] = +4 if const.TRINE in asp_ben else 0
        score['benefic_asp60'] = +3 if const.SEXTILE in asp_ben else 0

        # Aspects to malefics
        asp_mal = self.aspect_malefics()
        score['malefic_asp0'] = -5 if const.CONJUNCTION in asp_mal else 0
        score['malefic_asp180'] = -4 if const.OPPOSITION in asp_mal else 0
        score['malefic_asp90'] = -3 if const.SQUARE in asp_mal else 0

        # Auxily and Surround
        score['auxilied'] = +5 if self.is_auxilied() else 0
        score['surround'] = -5 if self.is_surrounded() else 0

        # Voc and Feral
        score['feral'] = -3 if self.is_feral() else 0
        score['void'] = -2 if (self.is_voc() and score['feral'] == 0) else 0

        # Haiz
        haiz = self.haiz()
        score['haiz'] = 0
        if haiz == HAIZ:
            score['haiz'] = +3
        elif haiz == CHAIZ:
            score['haiz'] = -2

        # Moon via combusta
        score['viacombusta'] = 0
        if obj.id == const.MOON and via_combusta(obj):
            score['viacombusta'] = -2

        return score

    def get_active_properties(self):
        """ Returns the non-zero accidental dignities. """
        score = self.get_score_properties()
        return {key: value for (key, value) in score.items()
                if value != 0}

    def score(self):
        """ Returns the sum of the accidental dignities score. """
        if not self.score_properties:
            self.score_properties = self.get_score_properties()
        return sum(self.score_properties.values())
