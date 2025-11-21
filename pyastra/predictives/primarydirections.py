"""
This module implements the Primary Directions method.

Default assumptions:
- only directions with the primary motion (direct)
- only semi-arc method
- in-zodiaco aspects of promissors to significators
- in-mundo directions uses latitude of both promissors and significators

"""

from pyastra import angle
from pyastra import utils
from pyastra import const
from pyastra.dignities import tables


# === Base functions === #

def arc(p_ra, p_decl, s_ra, s_decl, mc_ra, lat):
    """
    Returns the arc of direction between a Promissor and Significator.
    It uses the generic proportional semi-arc method.
    
    """
    pDArc, pNArc = utils.dnarcs(p_decl, lat)
    sDArc, sNArc = utils.dnarcs(s_decl, lat)

    # Select meridian and arcs to be used. Default is MC and Diurnal arcs.
    md_ra = mc_ra
    s_arc = sDArc
    p_arc = pDArc
    if not utils.is_above_horizon(s_ra, s_decl, mc_ra, lat):
        # Use IC and Nocturnal arcs
        md_ra = angle.norm(mc_ra + 180)
        s_arc = sNArc
        p_arc = pNArc

    # Promissor and Significator distance to meridian
    p_dist = angle.closest_distance(md_ra, p_ra)
    s_dist = angle.closest_distance(md_ra, s_ra)

    # Promissor should be after significator (in degrees)
    if p_dist < s_dist:
        p_dist += 360

    # Meridian distances proportional to respective semi-arcs
    s_prop_dist = s_dist / (s_arc / 2.0)
    p_prop_dist = p_dist / (p_arc / 2.0)

    # The arc is how much of the promissor's semi-arc is needed to reach the significator
    return (p_prop_dist - s_prop_dist) * (p_arc / 2.0)


def get_arc(prom, sig, mc, pos, zerolat):
    """
    Returns the arc of direction between a promissor and a significator.
    Arguments are also the MC, the geoposition and zerolat to assume zero ecliptical latitudes.
    
    ZeroLat true => inZodiaco, false => inMundo
    """
    p_ra, p_decl = prom.eq_coords(zerolat)
    s_ra, s_decl = sig.eq_coords(zerolat)
    mc_ra, _ = mc.eq_coords()
    return arc(p_ra, p_decl, s_ra, s_decl, mc_ra, pos.lat)


# ---------------------------- #
#   Primary Directions Class   #
# ---------------------------- #

class Direction:
    """
    Represents a primary direction.

    """

    def __init__(self, **kwargs):
        self.arc = kwargs.get('arc')
        self.promissor = kwargs.get('promissor')
        self.significator = kwargs.get('significator')
        self.zodiac = kwargs.get('zodiac')

    def __str__(self):
        return f"Direction: {str(self.__dict__)}"


class PrimaryDirections:
    """
    This class represents the Primary Directions for a Chart.
    
    Given the complexity of all possible combinations, this class encodes the objects in the
    following functions:
    
    T() - Returns a term
    A() - Returns the antiscia
    C() - Returns the contra antiscia
    D() - Returns the dexter aspect
    S() - Returns the sinister aspect
    N() - Returns the conjunction or opposition aspect
    
    """

    # Define common significators
    SIG_HOUSES = []
    SIG_ANGLES = [const.ASC, const.MC]
    SIG_OBJECTS = [
        const.SUN, const.MOON, const.MERCURY,
        const.VENUS, const.MARS, const.JUPITER,
        const.SATURN, const.PARS_FORTUNA,
        const.NORTH_NODE, const.SOUTH_NODE
    ]

    # Maximum arc
    MAX_ARC = 100

    def __init__(self, chart):
        self.chart = chart
        self.lat = chart.pos.lat
        mc = self.chart.get_angle(const.MC)
        self.mcRA = mc.eq_coords()[0]
        self.terms = self._build_terms()

    def _build_terms(self):
        """ Builds a data structure indexing the terms longitude by sign and object. """
        term_lons = tables.term_lons(tables.EGYPTIAN_TERMS)
        res = {}
        for (obj_id, sign, lon) in term_lons:
            try:
                res[sign][obj_id] = lon
            except KeyError:
                res[sign] = {}
                res[sign][obj_id] = lon
        return res

    # === Object creation methods === #

    def G(self, obj_id, lat, lon):
        """ Creates a generic entry for an object. """

        # Equatorial coordinates
        eqM = utils.eq_coords(lon, lat)
        eqZ = eqM
        if lat != 0:
            eqZ = utils.eq_coords(lon, 0)

        return {
            'id': obj_id,
            'lat': lat,
            'lon': lon,
            'ra': eqM[0],
            'decl': eqM[1],
            'raZ': eqZ[0],
            'declZ': eqZ[1],
        }

    def T(self, obj_id, sign):
        """ Returns the term of an object in a sign. """
        lon = self.terms[sign][obj_id]
        obj_id = f'T_{obj_id}_{sign}'
        return self.G(obj_id, 0, lon)

    def A(self, obj_id):
        """ Returns the Antiscia of an object. """
        obj = self.chart.get_object(obj_id).antiscia()
        obj_id = f'A_{obj_id}'
        return self.G(obj_id, obj.lat, obj.lon)

    def C(self, obj_id):
        """ Returns the CAntiscia of an object. """
        obj = self.chart.get_object(obj_id).cantiscia()
        obj_id = f'C_{obj_id}'
        return self.G(obj_id, obj.lat, obj.lon)

    def D(self, obj_id, asp):
        """ Returns the dexter aspect of an object. """
        obj = self.chart.get_object(obj_id).copy()
        obj.relocate(obj.lon - asp)
        obj_id = f'D_{obj_id}_{asp}'
        return self.G(obj_id, obj.lat, obj.lon)

    def S(self, obj_id, asp):
        """ Returns the sinister aspect of an object. """
        obj = self.chart.get_object(obj_id).copy()
        obj.relocate(obj.lon + asp)
        obj_id = f'S_{obj_id}_{asp}'
        return self.G(obj_id, obj.lat, obj.lon)

    def N(self, obj_id, asp=0):
        """ Returns the conjunction or opposition aspect of an object. """
        obj = self.chart.get(obj_id).copy()
        obj.relocate(obj.lon + asp)
        obj_id = f'N_{obj_id}_{asp}'
        return self.G(obj_id, obj.lat, obj.lon)

    # === Arcs === #

    def _arc(self, prom, sig):
        """ Computes the in-zodiaco and in-mundo arcs between a promissor and a significator. """
        arcm = arc(prom['ra'], prom['decl'], sig['ra'], sig['decl'], self.mcRA, self.lat)
        arcz = arc(prom['raZ'], prom['declZ'], sig['raZ'], sig['declZ'], self.mcRA, self.lat)
        return {
            'arcm': arcm,
            'arcz': arcz
        }

    def get_arc(self, prom, sig):
        """
        Returns the arcs between a promissor and a significator. Should use the object creation
        functions to build the objects.
        
        """
        res = self._arc(prom, sig)
        res.update({
            'prom': prom['id'],
            'sig': sig['id']
        })
        return res

    # === Lists === #

    def _elements(self, ids, func, asp_list):
        """ Returns the IDs as objects considering the asp_list and the function. """
        res = []
        for asp in asp_list:
            if asp in [0, 180]:
                # Generate func for conjunctions and oppositions
                if func == self.N:
                    res.extend([func(obj_id, asp) for obj_id in ids])
                else:
                    res.extend([func(ID) for ID in ids])
            else:
                # Generate Dexter and Sinister for others
                res.extend([self.D(obj_id, asp) for obj_id in ids])
                res.extend([self.S(obj_id, asp) for obj_id in ids])
        return res

    def _terms(self):
        """ Returns a list with the objects as terms. """
        res = []
        for sign, terms in self.terms.items():
            for obj_id, _ in terms.items():
                res.append(self.T(obj_id, sign))
        return res

    def _build_directions(self, prom, sig) -> list[Direction]:
        """ Builds a list of directions from promissor and significator objects. """
        if prom['id'] == sig['id']:
            return []

        res = []
        arcs = self._arc(prom, sig)
        for (arc, zodiac) in [('arcm', 'M'), ('arcz', 'Z')]:
            if 0 < arcs[arc] < self.MAX_ARC:
                res.append(Direction(
                    arc=arcs[arc],
                    promissor=prom['id'],
                    significator=sig['id'],
                    zodiac=zodiac,
                ))

        return res

    def get_list(self, asp_list):
        """ Returns a sorted list with all primary directions. """
        # Significators
        objects = self._elements(self.SIG_OBJECTS, self.N, [0])
        houses = self._elements(self.SIG_HOUSES, self.N, [0])
        angles = self._elements(self.SIG_ANGLES, self.N, [0])
        significators = objects + houses + angles

        # Promissors
        objects = self._elements(self.SIG_OBJECTS, self.N, asp_list)
        terms = self._terms()
        antiscias = self._elements(self.SIG_OBJECTS, self.A, [0])
        cantiscias = self._elements(self.SIG_OBJECTS, self.C, [0])
        promissors = objects + terms + antiscias + cantiscias

        # Compute all
        res = []
        for prom in promissors:
            for sig in significators:
                directions = self._build_directions(prom, sig)
                res.extend(directions)

        return sorted(res, key=lambda obj: obj.arc)


# ------------------ #
#   PD Table Class   #
# ------------------ #

class PDTable:
    """ Represents the Primary Directions table for a chart. """

    def __init__(self, chart, asp_list=const.MAJOR_ASPECTS):
        pd = PrimaryDirections(chart)
        self.table = pd.get_list(asp_list)

    def view(self, arcmin, arcmax):
        """ Returns the directions within the min and max arcs. """
        res = []
        for direction in self.table:
            if arcmin < direction.arc < arcmax:
                res.append(direction)
        return res

    def by_significator(self, obj_id):
        """ Returns all directions to a significator. """
        res = []
        for direction in self.table:
            if obj_id in direction.significator:
                res.append(direction)
        return res

    def by_promissor(self, obj_id):
        """ Returns all directions to a promissor. """
        res = []
        for direction in self.table:
            if obj_id in direction.promissor:
                res.append(direction)
        return res
