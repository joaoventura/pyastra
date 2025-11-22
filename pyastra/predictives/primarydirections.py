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


def get_arc(prom, sig, mc, pos, zodiacal=True):
    """
    Returns the arc of direction between a promissor and a significator chart object.
    Arguments are also the MC, the geoposition and zero_lat to assume zero ecliptical latitudes.
    
    Zero_Lat true => Zodiacal directions, false => Mundane directions
    """
    zero_lat = zodiacal is True
    p_ra, p_decl = prom.eq_coords(zero_lat)
    s_ra, s_decl = sig.eq_coords(zero_lat)
    mc_ra, _ = mc.eq_coords()
    return arc(p_ra, p_decl, s_ra, s_decl, mc_ra, pos.lat)


# === Classes === #

class DirectionPoint:
    """
    Represents a Promissor or a Significator in a Primary Direction.
    It contains information about the point type (term, antiscia, dexter or sinister aspect, etc.)
    as well as the point coordinates.

    """

    def __init__(self, point_type, obj_id, aspect=const.NO_ASPECT, term_sign=None, lat=0.0, lon=0.0):
        self.point_type = point_type
        self.obj_id = obj_id
        self.aspect = aspect
        self.term_sign = term_sign
        self.lat = lat
        self.lon = lon

        # Compute equatorial coordinates
        self.ra_m, self.decl_m = utils.eq_coords(lon, lat)
        self.ra_z, self.decl_z = (self.ra_m, self.decl_m)
        if lat != 0:
            self.ra_z, self.decl_z = utils.eq_coords(lon, 0)

    def __str__(self):
        """ Returns the direction in human-readable format. """
        if self.point_type == const.PD_POINT_TYPE_TERM:
            return f'Terms of {self.obj_id} in {self.term_sign}'
        if self.point_type in [const.PD_POINT_TYPE_DEXTER_ASPECT,
                               const.PD_POINT_TYPE_SINISTER_ASPECT]:
            return f'{self.point_type} {const.ASPECT_NAMES[self.aspect]} of {self.obj_id}'
        if self.point_type == const.PD_POINT_TYPE_BODY:
            if self.aspect != 0:
                return f'{const.ASPECT_NAMES[self.aspect]} of {self.obj_id}'
            return f'{self.obj_id}'
        if self.point_type == const.PD_POINT_TYPE_ANTISCIA:
            return f'Antiscia of {self.obj_id}'
        if self.point_type == const.PD_POINT_TYPE_CONTRA_ANTISCIA:
            return f'Contra-Antiscia of {self.obj_id}'
        return 'Invalid direction'

    def __repr__(self):
        return f'DirectionPoint {str(self.__dict__)}'


class Direction:
    """
    Represents a primary direction.
    It contains information about the arc of direction, the promissor and significator as well as
    the type of direction (zodiacal or mundane).

    """

    def __init__(self, arc, promissor, significator, direction_type):
        self.arc: float = arc
        self.promissor: DirectionPoint = promissor
        self.significator: DirectionPoint = significator
        self.direction_type: str = direction_type

    def __str__(self):
        type_str = "Mundane" if self.direction_type == const.PD_TYPE_MUNDANE else "Zodiacal"
        return f"{self.arc:.4f} - {self.promissor} to {self.significator} ({type_str})"

    def __repr__(self):
        return f"Direction: {str(self.__dict__)}"


class PrimaryDirections:
    """
    This class computes the Primary Directions for a Chart.
    
    Given the complexity of all possible combinations, this class builds the promissor and
    significator objects in the following functions:
    
    T() - Returns a term DirectionPoint
    A() - Returns the antiscia DirectionPoint
    C() - Returns the contra antiscia DirectionPoint
    D() - Returns the dexter aspect DirectionPoint
    S() - Returns the sinister aspect DirectionPoint
    N() - Returns the conjunction or opposition aspect DirectionPoint
    
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

    def T(self, obj_id, sign) -> DirectionPoint:
        """ Returns the term of an object in a sign. """
        return DirectionPoint(
            point_type=const.PD_POINT_TYPE_TERM,
            obj_id=obj_id,
            term_sign=sign,
            lon = self.terms[sign][obj_id]
        )

    def A(self, obj_id) -> DirectionPoint:
        """ Returns the Antiscia of an object. """
        obj = self.chart.get_object(obj_id).antiscia()
        return DirectionPoint(
            point_type=const.PD_POINT_TYPE_ANTISCIA,
            obj_id=obj_id,
            lat=obj.lat,
            lon=obj.lon
        )

    def C(self, obj_id) -> DirectionPoint:
        """ Returns the CAntiscia of an object. """
        obj = self.chart.get_object(obj_id).cantiscia()
        return DirectionPoint(
            point_type=const.PD_POINT_TYPE_CONTRA_ANTISCIA,
            obj_id=obj_id,
            lat=obj.lat,
            lon=obj.lon
        )

    def D(self, obj_id, asp) -> DirectionPoint:
        """ Returns the dexter aspect of an object. """
        obj = self.chart.get_object(obj_id).copy()
        obj.relocate(obj.lon - asp)
        return DirectionPoint(
            point_type=const.PD_POINT_TYPE_DEXTER_ASPECT,
            obj_id=obj_id,
            aspect=asp,
            lat=obj.lat,
            lon=obj.lon
        )

    def S(self, obj_id, asp) -> DirectionPoint:
        """ Returns the sinister aspect of an object. """
        obj = self.chart.get_object(obj_id).copy()
        obj.relocate(obj.lon + asp)
        return DirectionPoint(
            point_type=const.PD_POINT_TYPE_SINISTER_ASPECT,
            obj_id=obj_id,
            aspect=asp,
            lat=obj.lat,
            lon=obj.lon
        )

    def N(self, obj_id, asp=0) -> DirectionPoint:
        """ Returns the conjunction or opposition aspect of an object. """
        obj = self.chart.get(obj_id).copy()
        obj.relocate(obj.lon + asp)
        return DirectionPoint(
            point_type=const.PD_POINT_TYPE_BODY,
            obj_id=obj_id,
            aspect=asp,
            lat=obj.lat,
            lon=obj.lon
        )

    # === Arcs === #

    def compute_arc(self, prom: DirectionPoint, sig: DirectionPoint):
        """ Computes the in-zodiaco and in-mundo arcs between a promissor and a significator. """
        return {
            'arcm': arc(prom.ra_m, prom.decl_m, sig.ra_m, sig.decl_m, self.mcRA, self.lat),
            'arcz': arc(prom.ra_z, prom.decl_z, sig.ra_z, sig.decl_z, self.mcRA, self.lat)
        }

    # === Lists === #

    def _iter_significators(self):
        """ Generates all significators. """
        significator_ids = self.SIG_OBJECTS + self.SIG_HOUSES + self.SIG_ANGLES
        for obj_id in significator_ids:
            yield self.N(obj_id, asp=0)

    def _iter_promissors(self, asp_list):
        """ Generates all promissors. """
        for obj_id in self.SIG_OBJECTS:

            # Aspects of objects
            for asp in asp_list:
                if asp in [0, 180]:
                    # Conjunction and opposition
                    yield self.N(obj_id, asp)
                else:
                    # Dexter and sinister aspects
                    yield self.D(obj_id, asp)
                    yield self.S(obj_id, asp)

            # Antiscias and Contra-antiscias
            yield self.A(obj_id)
            yield self.C(obj_id)

        # Terms
        for sign, terms in self.terms.items():
            for obj_id, _ in terms.items():
                yield self.T(obj_id, sign)

    def _build_directions(self, prom, sig) -> list[Direction]:
        """ Builds a list of directions from promissor and significator objects. """
        if prom.obj_id == sig.obj_id:
            return []

        res = []
        arcs = self.compute_arc(prom, sig)
        for (arc_type, dtype) in [('arcm', const.PD_TYPE_MUNDANE), ('arcz', const.PD_TYPE_ZODIACAL)]:
            if 0 < arcs[arc_type] < self.MAX_ARC:
                res.append(Direction(
                    arc=arcs[arc_type],
                    promissor=prom,
                    significator=sig,
                    direction_type=dtype,
                ))

        return res

    def get_list(self, asp_list) -> list[Direction]:
        """
        Computes primary directions between all promissors and significators
        and returns a sorted list of Directions.

        """
        res = []

        significators = list(self._iter_significators())
        for prom in self._iter_promissors(asp_list):
            for sig in significators:
                directions = self._build_directions(prom, sig)
                res.extend(directions)

        return sorted(res, key=lambda obj: obj.arc)

    @staticmethod
    def get_table(chart, asp_list=const.MAJOR_ASPECTS):
        """ Returns an instance of the Primary Directions table. """
        return PDTable(chart, asp_list)


class PDTable:
    """ Represents the Primary Directions table for a chart. """

    def __init__(self, chart, asp_list=const.MAJOR_ASPECTS):
        pd = PrimaryDirections(chart)
        self.table = pd.get_list(asp_list)

    def all(self):
        """Returns all directions."""
        return list(direction for direction in self.table)

    def filter_by(self, **filters):
        """ Returns directions by filter. """
        res = []
        for direction in self.table:
            if 'direction_type' in filters and direction.direction_type != filters['direction_type']:
                continue
            if 'promissor_type' in filters and direction.promissor.point_type != filters['promissor_type']:
                continue
            if 'promissor' in filters and direction.promissor.obj_id != filters['promissor']:
                continue
            if 'significator' in filters and direction.significator.obj_id != filters['significator']:
                continue
            if 'aspects' in filters and direction.promissor.aspect not in filters['aspects']:
                continue
            if 'arc_min' in filters and direction.arc < filters['arc_min']:
                continue
            if 'arc_max' in filters and direction.arc > filters['arc_max']:
                continue
            res.append(direction)

        return res
