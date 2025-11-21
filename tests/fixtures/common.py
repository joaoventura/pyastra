"""
Data for use in tests

"""

from pyastra import const
from pyastra.datetime import Datetime
from pyastra.geopos import GeoPos

date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')

VALUES_TROPICAL = {
    "Sun": {
        "lon": 352.7901775496469,
        "lon_speed": 0.997625656913294,
        "lat": 0.00014414517761478568,
        "lat_speed": 1.0786620560389873e-05,
        "sign": "Pisces"
    },
    "Moon": {
        "lon": 262.38170335764823,
        "lon_speed": 13.266868595371195,
        "lat": 5.0295581635409015,
        "lat_speed": 0.37011075946785954,
        "sign": "Sagittarius"
    },
    "Mercury": {
        "lon": 330.8159619417929,
        "lon_speed": 1.4969799152763041,
        "lat": -2.016388564383163,
        "lat_speed": -0.061960300356529545,
        "sign": "Pisces"
    },
    "Venus": {
        "lon": 25.503113452458788,
        "lon_speed": 1.2113797578692604,
        "lat": -0.10138015090476464,
        "lat_speed": 0.05182162001901608,
        "sign": "Aries"
    },
    "Mars": {
        "lon": 16.546701128126458,
        "lon_speed": 0.755080908740368,
        "lat": -0.3380896321593386,
        "lat_speed": 0.011740580188750377,
        "sign": "Aries"
    },
    "Jupiter": {
        "lon": 133.6435198996773,
        "lon_speed": -0.07927348649801765,
        "lat": 0.9817697082853792,
        "lat_speed": -0.0005178124348966173,
        "sign": "Leo"
    },
    "Saturn": {
        "lon": 244.92931933561383,
        "lon_speed": 0.0015556476137059089,
        "lat": 2.0925014023293085,
        "lat_speed": 0.0026896136924664115,
        "sign": "Sagittarius"
    },
    "North Node": {
        "lon": 191.14117786657647,
        "lon_speed": -0.0529467471023026,
        "lat": 0.0,
        "lat_speed": 0.0,
        "sign": "Libra"
    },
    "South Node": {
        "lon": 11.14117786657647,
        "lon_speed": 0.0,
        "lat": 0.0,
        "lat_speed": 0.0,
        "sign": "Aries"
    },
    "Syzygy": {
        "lon": 164.8397825511794,
        "lon_speed": 11.812258379842785,
        "lat": -2.2354152114936516,
        "lat_speed": 0.9783565241596873,
        "sign": "Virgo"
    },
    "Pars Fortuna": {
        "lon": 63.04996403881222,
        "lon_speed": 0.0,
        "lat": 0.0,
        "lat_speed": 0.0,
        "sign": "Gemini"
    },
    "House1": {
        "lon": 153.45843823081086,
        "size": 29.39933122125163,
        "sign": "Virgo"
    },
    "House2": {
        "lon": 182.85776945206248,
        "size": 29.183213992386698,
        "sign": "Libra"
    },
    "House3": {
        "lon": 212.04098344444918,
        "size": 27.276554414221806,
        "sign": "Scorpio"
    },
    "House4": {
        "lon": 239.317537858671,
        "size": 30.55960429045163,
        "sign": "Scorpio"
    },
    "House5": {
        "lon": 269.8771421491226,
        "size": 30.547674018543034,
        "sign": "Sagittarius"
    },
    "House6": {
        "lon": 300.42481616766565,
        "size": 33.03362206314523,
        "sign": "Aquarius"
    },
    "House7": {
        "lon": 333.4584382308109,
        "size": 29.3993312212516,
        "sign": "Pisces"
    },
    "House8": {
        "lon": 2.8577694520624846,
        "size": 29.183213992386698,
        "sign": "Aries"
    },
    "House9": {
        "lon": 32.04098344444918,
        "size": 27.2765544142218,
        "sign": "Taurus"
    },
    "House10": {
        "lon": 59.31753785867098,
        "size": 30.559604290451638,
        "sign": "Taurus"
    },
    "House11": {
        "lon": 89.87714214912262,
        "size": 30.547674018543034,
        "sign": "Gemini"
    },
    "House12": {
        "lon": 120.42481616766565,
        "size": 33.0336220631452,
        "sign": "Leo"
    },
    "Asc": {
        "lon": 153.45843823081086,
        "sign": "Virgo"
    },
    "IC": {
        "lon": 239.317537858671,
        "sign": "Scorpio"
    },
    "Desc": {
        "lon": 333.4584382308109,
        "sign": "Pisces"
    },
    "MC": {
        "lon": 59.31753785867098,
        "sign": "Taurus"
    },
    "Algenib": {
        "mag": 2.84,
        "lon": 9.363332208900212,
        "lat": 12.600754908395206,
        "sign": "Aries"
    },
    "Alpheratz": {
        "mag": 2.06,
        "lon": 14.515271384711838,
        "lat": 25.681178583648936,
        "sign": "Aries"
    },
    "Algol": {
        "mag": 2.12,
        "lon": 56.37784987541937,
        "lat": 22.43223304126827,
        "sign": "Taurus"
    },
    "Alcyone": {
        "mag": 2.87,
        "lon": 60.203579677603855,
        "lat": 4.052932584247496,
        "sign": "Gemini"
    },
    "Aldebaran": {
        "mag": 0.86,
        "lon": 70.00151991972375,
        "lat": -5.466765551372648,
        "sign": "Gemini"
    },
    "Rigel": {
        "mag": 0.13,
        "lon": 77.04252773330272,
        "lat": -31.123742002509417,
        "sign": "Gemini"
    },
    "Capella": {
        "mag": 0.08,
        "lon": 82.0713830249819,
        "lat": 22.866658332696808,
        "sign": "Gemini"
    },
    "Betelgeuse": {
        "mag": 0.42,
        "lon": 88.96874334761785,
        "lat": -16.026542330520844,
        "sign": "Gemini"
    },
    "Sirius": {
        "mag": -1.46,
        "lon": 104.2948611333815,
        "lat": -39.61213299774762,
        "sign": "Cancer"
    },
    "Canopus": {
        "mag": -0.74,
        "lon": 105.18067328643583,
        "lat": -75.82699840809937,
        "sign": "Cancer"
    },
    "Castor": {
        "mag": 1.58,
        "lon": 110.45573980105307,
        "lat": 10.097703453992676,
        "sign": "Cancer"
    },
    "Pollux": {
        "mag": 1.14,
        "lon": 113.42948454191026,
        "lat": 6.685853967964133,
        "sign": "Cancer"
    },
    "Procyon": {
        "mag": 0.37,
        "lon": 115.99954436089028,
        "lat": -16.0240613590668,
        "sign": "Cancer"
    },
    "Asellus Borealis": {
        "mag": 4.652,
        "lon": 127.75558396534085,
        "lat": 3.191912330340212,
        "sign": "Leo"
    },
    "Asellus Australis": {
        "mag": 3.94,
        "lon": 128.9396865195274,
        "lat": 0.0776537417009728,
        "sign": "Leo"
    },
    "Alphard": {
        "mag": 1.97,
        "lon": 147.4973299663273,
        "lat": -22.382250795959838,
        "sign": "Leo"
    },
    "Regulus": {
        "mag": 1.4,
        "lon": 150.0467943706389,
        "lat": 0.46535773172484896,
        "sign": "Virgo"
    },
    "Denebola": {
        "mag": 2.13,
        "lon": 171.8353862315384,
        "lat": 12.265703318069995,
        "sign": "Virgo"
    },
    "Algorab": {
        "mag": 2.94,
        "lon": 193.66950463074977,
        "lat": -12.19737235135794,
        "sign": "Libra"
    },
    "Spica": {
        "mag": 0.97,
        "lon": 204.0593549926635,
        "lat": -2.055526411260269,
        "sign": "Libra"
    },
    "Arcturus": {
        "mag": -0.05,
        "lon": 204.4524183242977,
        "lat": 30.724129476258618,
        "sign": "Libra"
    },
    "Alphecca": {
        "mag": 2.24,
        "lon": 222.51636599158712,
        "lat": 44.31879461160149,
        "sign": "Scorpio"
    },
    "Zuben Eshamali": {
        "mag": 2.62,
        "lon": 229.58790017669193,
        "lat": 8.493417675530754,
        "sign": "Scorpio"
    },
    "Unukalhai": {
        "mag": 2.63,
        "lon": 232.2926928272246,
        "lat": 25.50452033420928,
        "sign": "Scorpio"
    },
    "Agena": {
        "mag": 0.6,
        "lon": 234.00819808132943,
        "lat": -44.13599183235419,
        "sign": "Scorpio"
    },
    "Rigel Kentaurus": {
        "mag": -0.1,
        "lon": 239.67477901885044,
        "lat": -42.598004633009104,
        "sign": "Scorpio"
    },
    "Antares": {
        "mag": 0.91,
        "lon": 249.97672909473243,
        "lat": -4.571525824852803,
        "sign": "Sagittarius"
    },
    "Lesath": {
        "mag": 2.7,
        "lon": 264.2257567013243,
        "lat": -14.00904426994501,
        "sign": "Sagittarius"
    },
    "Vega": {
        "mag": 0.03,
        "lon": 285.5257686562842,
        "lat": 61.72744725222478,
        "sign": "Capricorn"
    },
    "Altair": {
        "mag": 0.76,
        "lon": 301.98782228546713,
        "lat": 29.300815471768846,
        "sign": "Aquarius"
    },
    "Deneb Algedi": {
        "mag": 2.83,
        "lon": 323.7515354758217,
        "lat": -2.604137631339398,
        "sign": "Aquarius"
    },
    "Fomalhaut": {
        "mag": 1.16,
        "lon": 334.06951609791975,
        "lat": -21.136898342598553,
        "sign": "Pisces"
    },
    "Deneb": {
        "mag": 1.25,
        "lon": 335.52837979503687,
        "lat": 59.904086226173426,
        "sign": "Pisces"
    },
    "Achernar": {
        "mag": 0.46,
        "lon": 345.5170329665451,
        "lat": -59.37830474568324,
        "sign": "Pisces"
    }
}

VALUES_SIDEREAL_FAGAN_BRADLEY = {
    "Sun": {
        "lon": 327.836552645053,
        "lon_speed": 0.9975803975548786,
        "lat": 0.00014414517761542888,
        "lat_speed": 1.060304669271518e-05,
        "sign": "Aquarius"
    },
    "Moon": {
        "lon": 237.4280784530544,
        "lon_speed": 13.266823353080504,
        "lat": 5.029558163540909,
        "lat_speed": 0.37010930967439215,
        "sign": "Scorpio"
    },
    "Mercury": {
        "lon": 305.8623370371991,
        "lon_speed": 1.496934700825181,
        "lat": -2.0163885643831616,
        "lat_speed": -0.061961013592158914,
        "sign": "Aquarius"
    },
    "Venus": {
        "lon": 0.5494885478649718,
        "lon_speed": 1.2113345008171554,
        "lat": -0.10138015090476742,
        "lat_speed": 0.051822249821322254,
        "sign": "Aries"
    },
    "Mars": {
        "lon": 351.59307622353265,
        "lon_speed": 0.7550356576428834,
        "lat": -0.3380896321593395,
        "lat_speed": 0.011740996772176522,
        "sign": "Pisces"
    },
    "Jupiter": {
        "lon": 108.68989499508349,
        "lon_speed": -0.07931872858548193,
        "lat": 0.9817697082853729,
        "lat_speed": -0.000516753942212708,
        "sign": "Cancer"
    },
    "Saturn": {
        "lon": 219.97569443102,
        "lon_speed": 0.0015104108920353664,
        "lat": 2.0925014023293125,
        "lat_speed": 0.002688288759099268,
        "sign": "Scorpio"
    },
    "North Node": {
        "lon": 166.18755296198265,
        "lon_speed": -0.05299200645862551,
        "lat": -2.7998803283568783e-16,
        "lat_speed": -1.4594419870406485e-18,
        "sign": "Virgo"
    },
    "South Node": {
        "lon": 346.18755296198265,
        "lon_speed": 0.0,
        "lat": 0.0,
        "lat_speed": 0.0,
        "sign": "Pisces"
    },
    "Syzygy": {
        "lon": 139.88628225465519,
        "lon_speed": 11.812256954572113,
        "lat": -2.2354152114936525,
        "lat_speed": 0.9783548607240241,
        "sign": "Leo"
    },
    "Pars Fortuna": {
        "lon": 38.096339134218454,
        "lon_speed": 0.0,
        "lat": 0.0,
        "lat_speed": 0.0,
        "sign": "Taurus"
    },
    "House1": {
        "lon": 128.50481332621703,
        "size": 29.39933122125163,
        "sign": "Leo"
    },
    "House2": {
        "lon": 157.90414454746866,
        "size": 29.183213992386698,
        "sign": "Virgo"
    },
    "House3": {
        "lon": 187.08735853985536,
        "size": 27.276554414221806,
        "sign": "Libra"
    },
    "House4": {
        "lon": 214.36391295407716,
        "size": 30.55960429045163,
        "sign": "Scorpio"
    },
    "House5": {
        "lon": 244.9235172445288,
        "size": 30.547674018543034,
        "sign": "Sagittarius"
    },
    "House6": {
        "lon": 275.47119126307183,
        "size": 33.03362206314523,
        "sign": "Capricorn"
    },
    "House7": {
        "lon": 308.50481332621706,
        "size": 29.3993312212516,
        "sign": "Aquarius"
    },
    "House8": {
        "lon": 337.90414454746866,
        "size": 29.183213992386698,
        "sign": "Pisces"
    },
    "House9": {
        "lon": 7.087358539855366,
        "size": 27.2765544142218,
        "sign": "Aries"
    },
    "House10": {
        "lon": 34.363912954077165,
        "size": 30.55960429045163,
        "sign": "Taurus"
    },
    "House11": {
        "lon": 64.9235172445288,
        "size": 30.547674018543034,
        "sign": "Gemini"
    },
    "House12": {
        "lon": 95.47119126307183,
        "size": 33.0336220631452,
        "sign": "Cancer"
    },
    "Asc": {
        "lon": 128.50481332621703,
        "sign": "Leo"
    },
    "IC": {
        "lon": 214.36391295407716,
        "sign": "Scorpio"
    },
    "Desc": {
        "lon": 308.504813326217,
        "sign": "Aquarius"
    },
    "MC": {
        "lon": 34.363912954077165,
        "sign": "Taurus"
    },
    "Algenib": {
        "mag": 2.84,
        "lon": 344.4097073043064,
        "lat": 12.600754908395206,
        "sign": "Pisces"
    },
    "Alpheratz": {
        "mag": 2.06,
        "lon": 349.56164648011804,
        "lat": 25.681178583648933,
        "sign": "Pisces"
    },
    "Algol": {
        "mag": 2.12,
        "lon": 31.42422497082554,
        "lat": 22.43223304126827,
        "sign": "Taurus"
    },
    "Alcyone": {
        "mag": 2.87,
        "lon": 35.24995477301004,
        "lat": 4.052932584247497,
        "sign": "Taurus"
    },
    "Aldebaran": {
        "mag": 0.86,
        "lon": 45.047895015129924,
        "lat": -5.466765551372646,
        "sign": "Taurus"
    },
    "Rigel": {
        "mag": 0.13,
        "lon": 52.088902828708896,
        "lat": -31.12374200250941,
        "sign": "Taurus"
    },
    "Capella": {
        "mag": 0.08,
        "lon": 57.117758120388096,
        "lat": 22.866658332696808,
        "sign": "Taurus"
    },
    "Betelgeuse": {
        "mag": 0.42,
        "lon": 64.01511844302404,
        "lat": -16.026542330520854,
        "sign": "Gemini"
    },
    "Sirius": {
        "mag": -1.46,
        "lon": 79.34123622878768,
        "lat": -39.61213299774761,
        "sign": "Gemini"
    },
    "Canopus": {
        "mag": -0.74,
        "lon": 80.22704838184201,
        "lat": -75.82699840809937,
        "sign": "Gemini"
    },
    "Castor": {
        "mag": 1.58,
        "lon": 85.50211489645926,
        "lat": 10.097703453992672,
        "sign": "Gemini"
    },
    "Pollux": {
        "mag": 1.14,
        "lon": 88.47585963731645,
        "lat": 6.685853967964131,
        "sign": "Gemini"
    },
    "Procyon": {
        "mag": 0.37,
        "lon": 91.04591945629646,
        "lat": -16.0240613590668,
        "sign": "Cancer"
    },
    "Asellus Borealis": {
        "mag": 4.652,
        "lon": 102.80195906074704,
        "lat": 3.191912330340208,
        "sign": "Cancer"
    },
    "Asellus Australis": {
        "mag": 3.94,
        "lon": 103.98606161493359,
        "lat": 0.07765374170096874,
        "sign": "Cancer"
    },
    "Alphard": {
        "mag": 1.97,
        "lon": 122.5437050617335,
        "lat": -22.382250795959845,
        "sign": "Leo"
    },
    "Regulus": {
        "mag": 1.4,
        "lon": 125.09316946604511,
        "lat": 0.46535773172484923,
        "sign": "Leo"
    },
    "Denebola": {
        "mag": 2.13,
        "lon": 146.8817613269446,
        "lat": 12.265703318069994,
        "sign": "Leo"
    },
    "Algorab": {
        "mag": 2.94,
        "lon": 168.71587972615598,
        "lat": -12.197372351357942,
        "sign": "Virgo"
    },
    "Spica": {
        "mag": 0.97,
        "lon": 179.10573008806966,
        "lat": -2.055526411260265,
        "sign": "Virgo"
    },
    "Arcturus": {
        "mag": -0.05,
        "lon": 179.4987934197039,
        "lat": 30.724129476258618,
        "sign": "Virgo"
    },
    "Alphecca": {
        "mag": 2.24,
        "lon": 197.5627410869933,
        "lat": 44.31879461160149,
        "sign": "Libra"
    },
    "Zuben Eshamali": {
        "mag": 2.62,
        "lon": 204.6342752720981,
        "lat": 8.493417675530758,
        "sign": "Libra"
    },
    "Unukalhai": {
        "mag": 2.63,
        "lon": 207.3390679226308,
        "lat": 25.50452033420928,
        "sign": "Libra"
    },
    "Agena": {
        "mag": 0.6,
        "lon": 209.05457317673563,
        "lat": -44.13599183235419,
        "sign": "Libra"
    },
    "Rigel Kentaurus": {
        "mag": -0.1,
        "lon": 214.72115411425665,
        "lat": -42.598004633009104,
        "sign": "Scorpio"
    },
    "Antares": {
        "mag": 0.91,
        "lon": 225.02310419013864,
        "lat": -4.571525824852803,
        "sign": "Scorpio"
    },
    "Lesath": {
        "mag": 2.7,
        "lon": 239.27213179673052,
        "lat": -14.009044269945003,
        "sign": "Scorpio"
    },
    "Vega": {
        "mag": 0.03,
        "lon": 260.57214375169036,
        "lat": 61.72744725222478,
        "sign": "Sagittarius"
    },
    "Altair": {
        "mag": 0.76,
        "lon": 277.0341973808733,
        "lat": 29.300815471768864,
        "sign": "Capricorn"
    },
    "Deneb Algedi": {
        "mag": 2.83,
        "lon": 298.7979105712278,
        "lat": -2.604137631339397,
        "sign": "Capricorn"
    },
    "Fomalhaut": {
        "mag": 1.16,
        "lon": 309.1158911933259,
        "lat": -21.136898342598553,
        "sign": "Aquarius"
    },
    "Deneb": {
        "mag": 1.25,
        "lon": 310.57475489044305,
        "lat": 59.90408622617344,
        "sign": "Aquarius"
    },
    "Achernar": {
        "mag": 0.46,
        "lon": 320.5634080619513,
        "lat": -59.37830474568324,
        "sign": "Aquarius"
    }
}

VALUES_SIDEREAL_LAHIRI = {
    "Sun": {
        "lon": 328.71976028788066,
        "lon_speed": 0.9975803974980352,
        "lat": 0.00014414517761542888,
        "lat_speed": 1.0603046692715183e-05,
        "sign": "Aquarius"
    },
    "Moon": {
        "lon": 238.311286095882,
        "lon_speed": 13.26682335302366,
        "lat": 5.029558163540909,
        "lat_speed": 0.37010930967439215,
        "sign": "Scorpio"
    },
    "Mercury": {
        "lon": 306.7455446800267,
        "lon_speed": 1.4969347007683376,
        "lat": -2.016388564383161,
        "lat_speed": -0.06196101359215892,
        "sign": "Aquarius"
    },
    "Venus": {
        "lon": 1.432696190692557,
        "lon_speed": 1.2113345007603122,
        "lat": -0.10138015090476742,
        "lat_speed": 0.051822249821322254,
        "sign": "Aries"
    },
    "Mars": {
        "lon": 352.47628386636023,
        "lon_speed": 0.7550356575860399,
        "lat": -0.3380896321593395,
        "lat_speed": 0.011740996772176526,
        "sign": "Pisces"
    },
    "Jupiter": {
        "lon": 109.57310263791108,
        "lon_speed": -0.07931872864232536,
        "lat": 0.9817697082853731,
        "lat_speed": -0.0005167539422127089,
        "sign": "Cancer"
    },
    "Saturn": {
        "lon": 220.8589020738476,
        "lon_speed": 0.0015104108351919447,
        "lat": 2.0925014023293125,
        "lat_speed": 0.0026882887590992687,
        "sign": "Scorpio"
    },
    "North Node": {
        "lon": 167.07076060481023,
        "lon_speed": -0.052992006515468947,
        "lat": -2.7998803283568783e-16,
        "lat_speed": -1.4594419870406485e-18,
        "sign": "Virgo"
    },
    "South Node": {
        "lon": 347.07076060481023,
        "lon_speed": 0.0,
        "lat": 0.0,
        "lat_speed": 0.0,
        "sign": "Pisces"
    },
    "Syzygy": {
        "lon": 140.76948989747996,
        "lon_speed": 11.812256954572115,
        "lat": -2.2354152114936525,
        "lat_speed": 0.9783548607240243,
        "sign": "Leo"
    },
    "Pars Fortuna": {
        "lon": 38.97954677704598,
        "lon_speed": 0.0,
        "lat": 0.0,
        "lat_speed": 0.0,
        "sign": "Taurus"
    },
    "House1": {
        "lon": 129.38802096904462,
        "size": 29.39933122125163,
        "sign": "Leo"
    },
    "House2": {
        "lon": 158.78735219029625,
        "size": 29.183213992386698,
        "sign": "Virgo"
    },
    "House3": {
        "lon": 187.97056618268294,
        "size": 27.276554414221806,
        "sign": "Libra"
    },
    "House4": {
        "lon": 215.24712059690475,
        "size": 30.55960429045163,
        "sign": "Scorpio"
    },
    "House5": {
        "lon": 245.80672488735638,
        "size": 30.547674018543034,
        "sign": "Sagittarius"
    },
    "House6": {
        "lon": 276.3543989058994,
        "size": 33.03362206314523,
        "sign": "Capricorn"
    },
    "House7": {
        "lon": 309.38802096904465,
        "size": 29.3993312212516,
        "sign": "Aquarius"
    },
    "House8": {
        "lon": 338.78735219029625,
        "size": 29.183213992386698,
        "sign": "Pisces"
    },
    "House9": {
        "lon": 7.970566182682951,
        "size": 27.2765544142218,
        "sign": "Aries"
    },
    "House10": {
        "lon": 35.24712059690475,
        "size": 30.55960429045163,
        "sign": "Taurus"
    },
    "House11": {
        "lon": 65.80672488735638,
        "size": 30.547674018543034,
        "sign": "Gemini"
    },
    "House12": {
        "lon": 96.35439890589942,
        "size": 33.0336220631452,
        "sign": "Cancer"
    },
    "Asc": {
        "lon": 129.38802096904462,
        "sign": "Leo"
    },
    "IC": {
        "lon": 215.24712059690475,
        "sign": "Scorpio"
    },
    "Desc": {
        "lon": 309.38802096904465,
        "sign": "Aquarius"
    },
    "MC": {
        "lon": 35.24712059690475,
        "sign": "Taurus"
    },
    "Algenib": {
        "mag": 2.84,
        "lon": 345.29291494713397,
        "lat": 12.600754908395206,
        "sign": "Pisces"
    },
    "Alpheratz": {
        "mag": 2.06,
        "lon": 350.4448541229456,
        "lat": 25.681178583648936,
        "sign": "Pisces"
    },
    "Algol": {
        "mag": 2.12,
        "lon": 32.307432613653134,
        "lat": 22.43223304126827,
        "sign": "Taurus"
    },
    "Alcyone": {
        "mag": 2.87,
        "lon": 36.133162415837624,
        "lat": 4.052932584247497,
        "sign": "Taurus"
    },
    "Aldebaran": {
        "mag": 0.86,
        "lon": 45.93110265795752,
        "lat": -5.466765551372646,
        "sign": "Taurus"
    },
    "Rigel": {
        "mag": 0.13,
        "lon": 52.972110471536475,
        "lat": -31.123742002509417,
        "sign": "Taurus"
    },
    "Capella": {
        "mag": 0.08,
        "lon": 58.000965763215675,
        "lat": 22.866658332696808,
        "sign": "Taurus"
    },
    "Betelgeuse": {
        "mag": 0.42,
        "lon": 64.89832608585162,
        "lat": -16.026542330520854,
        "sign": "Gemini"
    },
    "Sirius": {
        "mag": -1.46,
        "lon": 80.22444387161526,
        "lat": -39.61213299774761,
        "sign": "Gemini"
    },
    "Canopus": {
        "mag": -0.74,
        "lon": 81.11025602466961,
        "lat": -75.82699840809937,
        "sign": "Gemini"
    },
    "Castor": {
        "mag": 1.58,
        "lon": 86.38532253928685,
        "lat": 10.097703453992668,
        "sign": "Gemini"
    },
    "Pollux": {
        "mag": 1.14,
        "lon": 89.35906728014403,
        "lat": 6.685853967964131,
        "sign": "Gemini"
    },
    "Procyon": {
        "mag": 0.37,
        "lon": 91.92912709912405,
        "lat": -16.024061359066803,
        "sign": "Cancer"
    },
    "Asellus Borealis": {
        "mag": 4.652,
        "lon": 103.68516670357462,
        "lat": 3.1919123303402084,
        "sign": "Cancer"
    },
    "Asellus Australis": {
        "mag": 3.94,
        "lon": 104.86926925776118,
        "lat": 0.07765374170096874,
        "sign": "Cancer"
    },
    "Alphard": {
        "mag": 1.97,
        "lon": 123.42691270456109,
        "lat": -22.382250795959845,
        "sign": "Leo"
    },
    "Regulus": {
        "mag": 1.4,
        "lon": 125.9763771088727,
        "lat": 0.46535773172484923,
        "sign": "Leo"
    },
    "Denebola": {
        "mag": 2.13,
        "lon": 147.76496896977218,
        "lat": 12.265703318069994,
        "sign": "Leo"
    },
    "Algorab": {
        "mag": 2.94,
        "lon": 169.59908736898356,
        "lat": -12.197372351357942,
        "sign": "Virgo"
    },
    "Spica": {
        "mag": 0.97,
        "lon": 179.98893773089725,
        "lat": -2.055526411260265,
        "sign": "Virgo"
    },
    "Arcturus": {
        "mag": -0.05,
        "lon": 180.38200106253146,
        "lat": 30.724129476258618,
        "sign": "Libra"
    },
    "Alphecca": {
        "mag": 2.24,
        "lon": 198.44594872982088,
        "lat": 44.31879461160149,
        "sign": "Libra"
    },
    "Zuben Eshamali": {
        "mag": 2.62,
        "lon": 205.5174829149257,
        "lat": 8.493417675530758,
        "sign": "Libra"
    },
    "Unukalhai": {
        "mag": 2.63,
        "lon": 208.22227556545838,
        "lat": 25.50452033420928,
        "sign": "Libra"
    },
    "Agena": {
        "mag": 0.6,
        "lon": 209.9377808195632,
        "lat": -44.13599183235419,
        "sign": "Libra"
    },
    "Rigel Kentaurus": {
        "mag": -0.1,
        "lon": 215.6043617570842,
        "lat": -42.598004633009104,
        "sign": "Scorpio"
    },
    "Antares": {
        "mag": 0.91,
        "lon": 225.9063118329662,
        "lat": -4.571525824852803,
        "sign": "Scorpio"
    },
    "Lesath": {
        "mag": 2.7,
        "lon": 240.1553394395581,
        "lat": -14.009044269945003,
        "sign": "Sagittarius"
    },
    "Vega": {
        "mag": 0.03,
        "lon": 261.45535139451795,
        "lat": 61.72744725222478,
        "sign": "Sagittarius"
    },
    "Altair": {
        "mag": 0.76,
        "lon": 277.9174050237009,
        "lat": 29.300815471768857,
        "sign": "Capricorn"
    },
    "Deneb Algedi": {
        "mag": 2.83,
        "lon": 299.6811182140554,
        "lat": -2.604137631339397,
        "sign": "Capricorn"
    },
    "Fomalhaut": {
        "mag": 1.16,
        "lon": 309.9990988361535,
        "lat": -21.136898342598553,
        "sign": "Aquarius"
    },
    "Deneb": {
        "mag": 1.25,
        "lon": 311.45796253327063,
        "lat": 59.90408622617344,
        "sign": "Aquarius"
    },
    "Achernar": {
        "mag": 0.46,
        "lon": 321.4466157047789,
        "lat": -59.37830474568324,
        "sign": "Aquarius"
    }
}


ASPECTS = {
    "Sun": {
        "Moon": {
            "type": 90,
            "active_id": "Moon",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Mercury": {
            "type": -1,
            "active_id": "Mercury",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Venus": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Mars": {
            "type": -1,
            "active_id": "Sun",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Jupiter": {
            "type": -1,
            "active_id": "Sun",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Saturn": {
            "type": 120,
            "active_id": "Sun",
            "movement": "Applicative",
            "mutual_aspect": False,
            "mutual_movement": False
        },
        "North Node": {
            "type": -1,
            "active_id": "Sun",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "South Node": {
            "type": -1,
            "active_id": "Sun",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Syzygy": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Pars Fortuna": {
            "type": 60,
            "active_id": "Sun",
            "movement": "Applicative",
            "mutual_aspect": False,
            "mutual_movement": False
        }
    },
    "Moon": {
        "Sun": {
            "type": 90,
            "active_id": "Moon",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Mercury": {
            "type": 60,
            "active_id": "Moon",
            "movement": "Applicative",
            "mutual_aspect": False,
            "mutual_movement": False
        },
        "Venus": {
            "type": 120,
            "active_id": "Moon",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Mars": {
            "type": 120,
            "active_id": "Moon",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Jupiter": {
            "type": 120,
            "active_id": "Moon",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": True
        },
        "Saturn": {
            "type": -1,
            "active_id": "Moon",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "North Node": {
            "type": 60,
            "active_id": "Moon",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": True
        },
        "South Node": {
            "type": 120,
            "active_id": "Moon",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Syzygy": {
            "type": 90,
            "active_id": "Moon",
            "movement": "Separative",
            "mutual_aspect": False,
            "mutual_movement": False
        },
        "Pars Fortuna": {
            "type": -1,
            "active_id": "Moon",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        }
    },
    "Mercury": {
        "Sun": {
            "type": -1,
            "active_id": "Mercury",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Moon": {
            "type": 60,
            "active_id": "Moon",
            "movement": "Applicative",
            "mutual_aspect": False,
            "mutual_movement": False
        },
        "Venus": {
            "type": 60,
            "active_id": "Mercury",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Mars": {
            "type": -1,
            "active_id": "Mercury",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Jupiter": {
            "type": -1,
            "active_id": "Mercury",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Saturn": {
            "type": 90,
            "active_id": "Mercury",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "North Node": {
            "type": -1,
            "active_id": "Mercury",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "South Node": {
            "type": -1,
            "active_id": "Mercury",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Syzygy": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Pars Fortuna": {
            "type": 90,
            "active_id": "Mercury",
            "movement": "Applicative",
            "mutual_aspect": False,
            "mutual_movement": False
        }
    },
    "Venus": {
        "Sun": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Moon": {
            "type": 120,
            "active_id": "Moon",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Mercury": {
            "type": 60,
            "active_id": "Mercury",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Mars": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Jupiter": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Saturn": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "North Node": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "South Node": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Syzygy": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Pars Fortuna": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        }
    },
    "Mars": {
        "Sun": {
            "type": -1,
            "active_id": "Sun",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Moon": {
            "type": 120,
            "active_id": "Moon",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Mercury": {
            "type": -1,
            "active_id": "Mercury",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Venus": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Jupiter": {
            "type": 120,
            "active_id": "Mars",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": True
        },
        "Saturn": {
            "type": -1,
            "active_id": "Mars",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "North Node": {
            "type": 180,
            "active_id": "Mars",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": True
        },
        "South Node": {
            "type": 0,
            "active_id": "Mars",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Syzygy": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Pars Fortuna": {
            "type": -1,
            "active_id": "Mars",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        }
    },
    "Jupiter": {
        "Sun": {
            "type": -1,
            "active_id": "Sun",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Moon": {
            "type": 120,
            "active_id": "Moon",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": True
        },
        "Mercury": {
            "type": -1,
            "active_id": "Mercury",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Venus": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Mars": {
            "type": 120,
            "active_id": "Mars",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": True
        },
        "Saturn": {
            "type": 120,
            "active_id": "Jupiter",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": True
        },
        "North Node": {
            "type": 60,
            "active_id": "Jupiter",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "South Node": {
            "type": 120,
            "active_id": "Jupiter",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Syzygy": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Pars Fortuna": {
            "type": -1,
            "active_id": "Jupiter",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        }
    },
    "Saturn": {
        "Sun": {
            "type": 120,
            "active_id": "Sun",
            "movement": "Applicative",
            "mutual_aspect": False,
            "mutual_movement": False
        },
        "Moon": {
            "type": -1,
            "active_id": "Moon",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Mercury": {
            "type": 90,
            "active_id": "Mercury",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Venus": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Mars": {
            "type": -1,
            "active_id": "Mars",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Jupiter": {
            "type": 120,
            "active_id": "Jupiter",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": True
        },
        "North Node": {
            "type": -1,
            "active_id": "North Node",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "South Node": {
            "type": 120,
            "active_id": "Saturn",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Syzygy": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Pars Fortuna": {
            "type": 180,
            "active_id": "Saturn",
            "movement": "Separative",
            "mutual_aspect": False,
            "mutual_movement": False
        }
    },
    "North Node": {
        "Sun": {
            "type": -1,
            "active_id": "Sun",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Moon": {
            "type": 60,
            "active_id": "Moon",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": True
        },
        "Mercury": {
            "type": -1,
            "active_id": "Mercury",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Venus": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Mars": {
            "type": 180,
            "active_id": "Mars",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": True
        },
        "Jupiter": {
            "type": 60,
            "active_id": "Jupiter",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Saturn": {
            "type": -1,
            "active_id": "North Node",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "South Node": {
            "type": -1,
            "active_id": "North Node",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Syzygy": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Pars Fortuna": {
            "type": -1,
            "active_id": "North Node",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        }
    },
    "South Node": {
        "Sun": {
            "type": -1,
            "active_id": "Sun",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Moon": {
            "type": 120,
            "active_id": "Moon",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Mercury": {
            "type": -1,
            "active_id": "Mercury",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Venus": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Mars": {
            "type": 0,
            "active_id": "Mars",
            "movement": "Separative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Jupiter": {
            "type": 120,
            "active_id": "Jupiter",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "Saturn": {
            "type": 120,
            "active_id": "Saturn",
            "movement": "Applicative",
            "mutual_aspect": True,
            "mutual_movement": False
        },
        "North Node": {
            "type": -1,
            "active_id": "North Node",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Syzygy": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Pars Fortuna": {
            "type": -1,
            "active_id": "Pars Fortuna",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        }
    },
    "Syzygy": {
        "Sun": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Moon": {
            "type": 90,
            "active_id": "Moon",
            "movement": "Separative",
            "mutual_aspect": False,
            "mutual_movement": False
        },
        "Mercury": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Venus": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Mars": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Jupiter": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Saturn": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "North Node": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "South Node": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Pars Fortuna": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        }
    },
    "Pars Fortuna": {
        "Sun": {
            "type": 60,
            "active_id": "Sun",
            "movement": "Applicative",
            "mutual_aspect": False,
            "mutual_movement": False
        },
        "Moon": {
            "type": -1,
            "active_id": "Moon",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Mercury": {
            "type": 90,
            "active_id": "Mercury",
            "movement": "Applicative",
            "mutual_aspect": False,
            "mutual_movement": False
        },
        "Venus": {
            "type": -1,
            "active_id": "Venus",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Mars": {
            "type": -1,
            "active_id": "Mars",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Jupiter": {
            "type": -1,
            "active_id": "Jupiter",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Saturn": {
            "type": 180,
            "active_id": "Saturn",
            "movement": "Separative",
            "mutual_aspect": False,
            "mutual_movement": False
        },
        "North Node": {
            "type": -1,
            "active_id": "North Node",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "South Node": {
            "type": -1,
            "active_id": "South Node",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        },
        "Syzygy": {
            "type": -1,
            "active_id": "Syzygy",
            "movement": "None",
            "mutual_aspect": False,
            "mutual_movement": True
        }
    }
}


if __name__ == '__main__':
    # Check for correctness of ayanamsa diff from tropical to sidereal zodiac
    from pyastra import angle
    values = []
    for k, v in VALUES_TROPICAL.items():
        v1 = VALUES_SIDEREAL_FAGAN_BRADLEY[k]
        print(k, angle.norm(v['lon']-v1['lon']))
        values.append(angle.norm(v['lon']-v1['lon']))

    print(values)
    avg = sum(values)/len(values)
    print(avg, [v for v in values if (v-avg) > 0.00001])
