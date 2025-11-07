"""
This module implements the ChartDynamics class for handling some of the dynamics of an
astrology Chart.
  
"""

from pyastra import const
from pyastra import aspects
from pyastra.dignities import essential


# ----------------------- #
#   ChartDynamics Class   #
# ----------------------- #

class ChartDynamics:
    """ Chart dynamics class. """

    def __init__(self, chart):
        self.chart = chart

    # === Dignities and Mutual Reception === #

    def in_dignities(self, id_a, id_b):
        """ Returns the dignities of A which belong to B. """
        obj_a = self.chart.get(id_a)
        info = essential.get_info(obj_a.sign, obj_a.signlon)
        # Should we ignore exile and fall?
        return [dign for (dign, obj_id) in info.items() if obj_id == id_b]

    def receives(self, id_a, id_b):
        """
        Returns the dignities where A receives B.
        A receives B when (1) B aspects A and (2) B is in dignities of A.

        """
        obj_a = self.chart.get(id_a)
        obj_b = self.chart.get(id_b)
        asp = aspects.is_aspecting(obj_b, obj_a, const.MAJOR_ASPECTS)
        return self.in_dignities(id_b, id_a) if asp else []

    def disposits(self, id_a, id_b):
        """ Returns the dignities where A is dispositor of B. """
        return self.in_dignities(id_b, id_a)

    def mutual_receptions(self, id_a, id_b):
        """ Returns all pairs of dignities in mutual reception. """
        AB = self.receives(id_a, id_b)
        BA = self.receives(id_b, id_a)
        # Returns a product of both lists
        return [(a, b) for a in AB for b in BA]

    def re_mutual_receptions(self, id_a, id_b):
        """ Returns ruler and exaltation mutual receptions. """
        mr = self.mutual_receptions(id_a, id_b)
        filter_ = ['ruler', 'exalt']
        # Each pair of dignities must be 'ruler' or 'exalt'
        return [(a, b) for (a, b) in mr if (a in filter_ and b in filter_)]

    # === Aspects === #

    def valid_aspects(self, obj_id, asp_list):
        """
        Returns a list with the aspects an object makes with the other six planets, considering a
        list of possible aspects. 
        
        """
        obj = self.chart.get_object(obj_id)
        res = []

        for other_id in const.LIST_SEVEN_PLANETS:
            if obj_id == other_id:
                continue

            other_obj = self.chart.get_object(other_id)
            asp_type = aspects.aspect_type(obj, other_obj, asp_list)
            if asp_type != const.NO_ASPECT:
                res.append({
                    'id': other_id,
                    'asp': asp_type,
                })
        return res

    def aspects_by_cat(self, obj_id, asp_list):
        """
        Returns the aspects an object makes with the other six planets, separated by category
        (applicative, separative, exact). Aspects must be within orb of the object.
        
        """
        res = {
            const.APPLICATIVE: [],
            const.SEPARATIVE: [],
            const.EXACT: [],
            const.NO_MOVEMENT: []
        }

        obj_a = self.chart.get_object(obj_id)
        valid = self.valid_aspects(obj_id, asp_list)
        for elem in valid:
            obj_b = self.chart.get_object(elem['id'])
            asp = aspects.get_aspect(obj_a, obj_b, asp_list)
            role = asp.get_role(obj_a.id)
            if role['inOrb']:
                movement = role['movement']
                res[movement].append({
                    'id': obj_b.id,
                    'asp': asp.type,
                    'orb': asp.orb
                })

        return res

    def immediate_aspects(self, obj_id, asp_list):
        """ Returns the last separation and next application considering list of aspects. """

        asps = self.aspects_by_cat(obj_id, asp_list)

        applications = asps[const.APPLICATIVE]
        separations = asps[const.SEPARATIVE]
        exact = asps[const.EXACT]

        # Get applications and separations sorted by orb
        applications = applications + [val for val in exact if val['orb'] >= 0]
        applications = sorted(applications, key=lambda var: var['orb'])
        separations = sorted(separations, key=lambda var: var['orb'])

        return (
            separations[0] if separations else None,
            applications[0] if applications else None
        )

    def is_voc(self, obj_id):
        """
        Returns if a planet is Void of Course.
        A planet is not VOC if has any exact or applicative aspects ignoring the sign status
        (associate or dissociate).
        
        """
        asps = self.aspects_by_cat(obj_id, const.MAJOR_ASPECTS)
        applications = asps[const.APPLICATIVE]
        exacts = asps[const.EXACT]
        return len(applications) == 0 and len(exacts) == 0
