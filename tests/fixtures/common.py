"""
Data for use in tests

"""

from pyastra import const
from pyastra.datetime import Datetime
from pyastra.geopos import GeoPos

date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')

VALUES_TROPICAL = {
    "Sun": {"lon": 352.7901775496469, "lat": 0.00014414517761478568, "sign": "Pisces"},
    "Moon": {"lon": 262.38170335764823, "lat": 5.0295581635409015, "sign": "Sagittarius"},
    "Mercury": {"lon": 330.8159619417929, "lat": -2.016388564383163, "sign": "Pisces"},
    "Venus": {"lon": 25.503113452458788, "lat": -0.10138015090476464, "sign": "Aries"},
    "Mars": {"lon": 16.546701128126458, "lat": -0.3380896321593386, "sign": "Aries"},
    "Jupiter": {"lon": 133.6435198996773, "lat": 0.9817697082853792, "sign": "Leo"},
    "Saturn": {"lon": 244.92931933561383, "lat": 2.0925014023293085, "sign": "Sagittarius"},
    "North Node": {"lon": 191.14117786657647, "lat": 0.0, "sign": "Libra"},
    "South Node": {"lon": 11.14117786657647, "lat": 0.0, "sign": "Aries"},
    "Syzygy": {"lon": 164.8397825511794, "lat": -2.2354152114936516, "sign": "Virgo"},
    "Pars Fortuna": {"lon": 63.04996403881222, "lat": 0.0, "sign": "Gemini"},

    "House1": {"lon": 153.45843823081086, "size": 30.0, "sign": "Virgo"},
    "House2": {"lon": 182.85776945206248, "size": 30.0, "sign": "Libra"},
    "House3": {"lon": 212.04098344444918, "size": 30.0, "sign": "Scorpio"},
    "House4": {"lon": 239.317537858671, "size": 30.0, "sign": "Scorpio"},
    "House5": {"lon": 269.8771421491226, "size": 30.0, "sign": "Sagittarius"},
    "House6": {"lon": 300.42481616766565, "size": 30.0, "sign": "Aquarius"},
    "House7": {"lon": 333.4584382308109, "size": 30.0, "sign": "Pisces"},
    "House8": {"lon": 2.8577694520624846, "size": 30.0, "sign": "Aries"},
    "House9": {"lon": 32.04098344444918, "size": 30.0, "sign": "Taurus"},
    "House10": {"lon": 59.31753785867098, "size": 30.0, "sign": "Taurus"},
    "House11": {"lon": 89.87714214912262, "size": 30.0, "sign": "Gemini"},
    "House12": {"lon": 120.42481616766565, "size": 30.0, "sign": "Leo"},

    "Asc": {"lon": 153.45843823081086, "sign": "Virgo"},
    "IC": {"lon": 239.317537858671, "sign": "Scorpio"},
    "Desc": {"lon": 333.4584382308109, "sign": "Pisces"},
    "MC": {"lon": 59.31753785867098, "sign": "Taurus"},

    "Algenib": {"lon": 9.363332208900212, "lat": 12.600754908395206, "sign": "Aries"},
    "Alpheratz": {"lon": 14.515271384711838, "lat": 25.681178583648936, "sign": "Aries"},
    "Algol": {"lon": 56.37784987541937, "lat": 22.43223304126827, "sign": "Taurus"},
    "Alcyone": {"lon": 60.203579677603855, "lat": 4.052932584247496, "sign": "Gemini"},
    "Aldebaran": {"lon": 70.00151991972375, "lat": -5.466765551372648, "sign": "Gemini"},
    "Rigel": {"lon": 77.04252773330272, "lat": -31.123742002509417, "sign": "Gemini"},
    "Capella": {"lon": 82.0713830249819, "lat": 22.866658332696808, "sign": "Gemini"},
    "Betelgeuse": {"lon": 88.96874334761785, "lat": -16.026542330520844, "sign": "Gemini"},
    "Sirius": {"lon": 104.2948611333815, "lat": -39.61213299774762, "sign": "Cancer"},
    "Canopus": {"lon": 105.18067328643583, "lat": -75.82699840809937, "sign": "Cancer"},
    "Castor": {"lon": 110.45573980105307, "lat": 10.097703453992676, "sign": "Cancer"},
    "Pollux": {"lon": 113.42948454191026, "lat": 6.685853967964133, "sign": "Cancer"},
    "Procyon": {"lon": 115.99954436089028, "lat": -16.0240613590668, "sign": "Cancer"},
    "Asellus Borealis": {"lon": 127.75558396534085, "lat": 3.191912330340212, "sign": "Leo"},
    "Asellus Australis": {"lon": 128.9396865195274, "lat": 0.0776537417009728, "sign": "Leo"},
    "Alphard": {"lon": 147.4973299663273, "lat": -22.382250795959838, "sign": "Leo"},
    "Regulus": {"lon": 150.0467943706389, "lat": 0.46535773172484896, "sign": "Virgo"},
    "Denebola": {"lon": 171.8353862315384, "lat": 12.265703318069995, "sign": "Virgo"},
    "Algorab": {"lon": 193.66950463074977, "lat": -12.19737235135794, "sign": "Libra"},
    "Spica": {"lon": 204.0593549926635, "lat": -2.055526411260269, "sign": "Libra"},
    "Arcturus": {"lon": 204.4524183242977, "lat": 30.724129476258618, "sign": "Libra"},
    "Alphecca": {"lon": 222.51636599158712, "lat": 44.31879461160149, "sign": "Scorpio"},
    "Zuben Eshamali": {"lon": 229.58790017669193, "lat": 8.493417675530754, "sign": "Scorpio"},
    "Unukalhai": {"lon": 232.2926928272246, "lat": 25.50452033420928, "sign": "Scorpio"},
    "Agena": {"lon": 234.00819808132943, "lat": -44.13599183235419, "sign": "Scorpio"},
    "Rigel Kentaurus": {"lon": 239.67477901885044, "lat": -42.598004633009104, "sign": "Scorpio"},
    "Antares": {"lon": 249.97672909473243, "lat": -4.571525824852803, "sign": "Sagittarius"},
    "Lesath": {"lon": 264.2257567013243, "lat": -14.00904426994501, "sign": "Sagittarius"},
    "Vega": {"lon": 285.5257686562842, "lat": 61.72744725222478, "sign": "Capricorn"},
    "Altair": {"lon": 301.98782228546713, "lat": 29.300815471768846, "sign": "Aquarius"},
    "Deneb Algedi": {"lon": 323.7515354758217, "lat": -2.604137631339398, "sign": "Aquarius"},
    "Fomalhaut": {"lon": 334.06951609791975, "lat": -21.136898342598553, "sign": "Pisces"},
    "Deneb": {"lon": 335.52837979503687, "lat": 59.904086226173426, "sign": "Pisces"},
    "Achernar": {"lon": 345.5170329665451, "lat": -59.37830474568324, "sign": "Pisces"}
}


VALUES_SIDEREAL_FAGAN_BRADLEY = {
    "Sun": {"lon": 327.836552645053, "lat": 0.00014414517761542888, "sign": "Aquarius"},
    "Moon": {"lon": 237.4280784530544, "lat": 5.029558163540909, "sign": "Scorpio"},
    "Mercury": {"lon": 305.8623370371991, "lat": -2.0163885643831616, "sign": "Aquarius"},
    "Venus": {"lon": 0.5494885478649718, "lat": -0.10138015090476742, "sign": "Aries"},
    "Mars": {"lon": 351.59307622353265, "lat": -0.3380896321593395, "sign": "Pisces"},
    "Jupiter": {"lon": 108.68989499508349, "lat": 0.9817697082853729, "sign": "Cancer"},
    "Saturn": {"lon": 219.97569443102, "lat": 2.0925014023293125, "sign": "Scorpio"},
    "North Node": {"lon": 166.18755296198265, "lat": -2.7998803283568783e-16, "sign": "Virgo"},
    "South Node": {"lon": 346.18755296198265, "lat": 0.0, "sign": "Pisces"},
    "Syzygy": {"lon": 139.88628225465519, "lat": -2.2354152114936525, "sign": "Leo"},
    "Pars Fortuna": {"lon": 38.096339134218454, "lat": 0.0, "sign": "Taurus"},

    "House1": {"lon": 128.50481332621703, "size": 30.0, "sign": "Leo"},
    "House2": {"lon": 157.90414454746866, "size": 30.0, "sign": "Virgo"},
    "House3": {"lon": 187.08735853985536, "size": 30.0, "sign": "Libra"},
    "House4": {"lon": 214.36391295407716, "size": 30.0, "sign": "Scorpio"},
    "House5": {"lon": 244.9235172445288, "size": 30.0, "sign": "Sagittarius"},
    "House6": {"lon": 275.47119126307183, "size": 30.0, "sign": "Capricorn"},
    "House7": {"lon": 308.50481332621706, "size": 30.0, "sign": "Aquarius"},
    "House8": {"lon": 337.90414454746866, "size": 30.0, "sign": "Pisces"},
    "House9": {"lon": 7.087358539855366, "size": 30.0, "sign": "Aries"},
    "House10": {"lon": 34.363912954077165, "size": 30.0, "sign": "Taurus"},
    "House11": {"lon": 64.9235172445288, "size": 30.0, "sign": "Gemini"},
    "House12": {"lon": 95.47119126307183, "size": 30.0, "sign": "Cancer"},

    "Asc": {"lon": 128.50481332621703, "sign": "Leo"},
    "IC": {"lon": 214.36391295407716, "sign": "Scorpio"},
    "Desc": {"lon": 308.504813326217, "sign": "Aquarius"},
    "MC": {"lon": 34.363912954077165, "sign": "Taurus"},

    "Algenib": {"lon": 344.4097073043064, "lat": 12.600754908395206, "sign": "Pisces"},
    "Alpheratz": {"lon": 349.56164648011804, "lat": 25.681178583648933, "sign": "Pisces"},
    "Algol": {"lon": 31.42422497082554, "lat": 22.43223304126827, "sign": "Taurus"},
    "Alcyone": {"lon": 35.24995477301004, "lat": 4.052932584247497, "sign": "Taurus"},
    "Aldebaran": {"lon": 45.047895015129924, "lat": -5.466765551372646, "sign": "Taurus"},
    "Rigel": {"lon": 52.088902828708896, "lat": -31.12374200250941, "sign": "Taurus"},
    "Capella": {"lon": 57.117758120388096, "lat": 22.866658332696808, "sign": "Taurus"},
    "Betelgeuse": {"lon": 64.01511844302404, "lat": -16.026542330520854, "sign": "Gemini"},
    "Sirius": {"lon": 79.34123622878768, "lat": -39.61213299774761, "sign": "Gemini"},
    "Canopus": {"lon": 80.22704838184201, "lat": -75.82699840809937, "sign": "Gemini"},
    "Castor": {"lon": 85.50211489645926, "lat": 10.097703453992672, "sign": "Gemini"},
    "Pollux": {"lon": 88.47585963731645, "lat": 6.685853967964131, "sign": "Gemini"},
    "Procyon": {"lon": 91.04591945629646, "lat": -16.0240613590668, "sign": "Cancer"},
    "Asellus Borealis": {"lon": 102.80195906074704, "lat": 3.191912330340208, "sign": "Cancer"},
    "Asellus Australis": {"lon": 103.98606161493359, "lat": 0.07765374170096874, "sign": "Cancer"},
    "Alphard": {"lon": 122.5437050617335, "lat": -22.382250795959845, "sign": "Leo"},
    "Regulus": {"lon": 125.09316946604511, "lat": 0.46535773172484923, "sign": "Leo"},
    "Denebola": {"lon": 146.8817613269446, "lat": 12.265703318069994, "sign": "Leo"},
    "Algorab": {"lon": 168.71587972615598, "lat": -12.197372351357942, "sign": "Virgo"},
    "Spica": {"lon": 179.10573008806966, "lat": -2.055526411260265, "sign": "Virgo"},
    "Arcturus": {"lon": 179.4987934197039, "lat": 30.724129476258618, "sign": "Virgo"},
    "Alphecca": {"lon": 197.5627410869933, "lat": 44.31879461160149, "sign": "Libra"},
    "Zuben Eshamali": {"lon": 204.6342752720981, "lat": 8.493417675530758, "sign": "Libra"},
    "Unukalhai": {"lon": 207.3390679226308, "lat": 25.50452033420928, "sign": "Libra"},
    "Agena": {"lon": 209.05457317673563, "lat": -44.13599183235419, "sign": "Libra"},
    "Rigel Kentaurus": {"lon": 214.72115411425665, "lat": -42.598004633009104, "sign": "Scorpio"},
    "Antares": {"lon": 225.02310419013864, "lat": -4.571525824852803, "sign": "Scorpio"},
    "Lesath": {"lon": 239.27213179673052, "lat": -14.009044269945003, "sign": "Scorpio"},
    "Vega": {"lon": 260.57214375169036, "lat": 61.72744725222478, "sign": "Sagittarius"},
    "Altair": {"lon": 277.0341973808733, "lat": 29.300815471768864, "sign": "Capricorn"},
    "Deneb Algedi": {"lon": 298.7979105712278, "lat": -2.604137631339397, "sign": "Capricorn"},
    "Fomalhaut": {"lon": 309.1158911933259, "lat": -21.136898342598553, "sign": "Aquarius"},
    "Deneb": {"lon": 310.57475489044305, "lat": 59.90408622617344, "sign": "Aquarius"},
    "Achernar": {"lon": 320.5634080619513, "lat": -59.37830474568324, "sign": "Aquarius"}
}


VALUES_SIDEREAL_LAHIRI = {
    "Sun": {"lon": 328.71976028788066, "lat": 0.00014414517761542888, "sign": "Aquarius"},
    "Moon": {"lon": 238.311286095882, "lat": 5.029558163540909, "sign": "Scorpio"},
    "Mercury": {"lon": 306.7455446800267, "lat": -2.016388564383161, "sign": "Aquarius"},
    "Venus": {"lon": 1.432696190692557, "lat": -0.10138015090476742, "sign": "Aries"},
    "Mars": {"lon": 352.47628386636023, "lat": -0.3380896321593395, "sign": "Pisces"},
    "Jupiter": {"lon": 109.57310263791108, "lat": 0.9817697082853731, "sign": "Cancer"},
    "Saturn": {"lon": 220.8589020738476, "lat": 2.0925014023293125, "sign": "Scorpio"},
    "North Node": {"lon": 167.07076060481023, "lat": -2.7998803283568783e-16, "sign": "Virgo"},
    "South Node": {"lon": 347.07076060481023, "lat": 0.0, "sign": "Pisces"},
    "Syzygy": {"lon": 140.76948989747996, "lat": -2.2354152114936525, "sign": "Leo"},
    "Pars Fortuna": {"lon": 38.97954677704598, "lat": 0.0, "sign": "Taurus"},

    "House1": {"lon": 129.38802096904462, "size": 30.0, "sign": "Leo"},
    "House2": {"lon": 158.78735219029625, "size": 30.0, "sign": "Virgo"},
    "House3": {"lon": 187.97056618268294, "size": 30.0, "sign": "Libra"},
    "House4": {"lon": 215.24712059690475, "size": 30.0, "sign": "Scorpio"},
    "House5": {"lon": 245.80672488735638, "size": 30.0, "sign": "Sagittarius"},
    "House6": {"lon": 276.3543989058994, "size": 30.0, "sign": "Capricorn"},
    "House7": {"lon": 309.38802096904465, "size": 30.0, "sign": "Aquarius"},
    "House8": {"lon": 338.78735219029625, "size": 30.0, "sign": "Pisces"},
    "House9": {"lon": 7.970566182682951, "size": 30.0, "sign": "Aries"},
    "House10": {"lon": 35.24712059690475, "size": 30.0, "sign": "Taurus"},
    "House11": {"lon": 65.80672488735638, "size": 30.0, "sign": "Gemini"},
    "House12": {"lon": 96.35439890589942, "size": 30.0, "sign": "Cancer"},

    "Asc": {"lon": 129.38802096904462, "sign": "Leo"},
    "IC": {"lon": 215.24712059690475, "sign": "Scorpio"},
    "Desc": {"lon": 309.38802096904465, "sign": "Aquarius"},
    "MC": {"lon": 35.24712059690475, "sign": "Taurus"},

    "Algenib": {"lon": 345.29291494713397, "lat": 12.600754908395206, "sign": "Pisces"},
    "Alpheratz": {"lon": 350.4448541229456, "lat": 25.681178583648936, "sign": "Pisces"},
    "Algol": {"lon": 32.307432613653134, "lat": 22.43223304126827, "sign": "Taurus"},
    "Alcyone": {"lon": 36.133162415837624, "lat": 4.052932584247497, "sign": "Taurus"},
    "Aldebaran": {"lon": 45.93110265795752, "lat": -5.466765551372646, "sign": "Taurus"},
    "Rigel": {"lon": 52.972110471536475, "lat": -31.123742002509417, "sign": "Taurus"},
    "Capella": {"lon": 58.000965763215675, "lat": 22.866658332696808, "sign": "Taurus"},
    "Betelgeuse": {"lon": 64.89832608585162, "lat": -16.026542330520854, "sign": "Gemini"},
    "Sirius": {"lon": 80.22444387161526, "lat": -39.61213299774761, "sign": "Gemini"},
    "Canopus": {"lon": 81.11025602466961, "lat": -75.82699840809937, "sign": "Gemini"},
    "Castor": {"lon": 86.38532253928685, "lat": 10.097703453992668, "sign": "Gemini"},
    "Pollux": {"lon": 89.35906728014403, "lat": 6.685853967964131, "sign": "Gemini"},
    "Procyon": {"lon": 91.92912709912405, "lat": -16.024061359066803, "sign": "Cancer"},
    "Asellus Borealis": {"lon": 103.68516670357462, "lat": 3.1919123303402084, "sign": "Cancer"},
    "Asellus Australis": {"lon": 104.86926925776118, "lat": 0.07765374170096874, "sign": "Cancer"},
    "Alphard": {"lon": 123.42691270456109, "lat": -22.382250795959845, "sign": "Leo"},
    "Regulus": {"lon": 125.9763771088727, "lat": 0.46535773172484923, "sign": "Leo"},
    "Denebola": {"lon": 147.76496896977218, "lat": 12.265703318069994, "sign": "Leo"},
    "Algorab": {"lon": 169.59908736898356, "lat": -12.197372351357942, "sign": "Virgo"},
    "Spica": {"lon": 179.98893773089725, "lat": -2.055526411260265, "sign": "Virgo"},
    "Arcturus": {"lon": 180.38200106253146, "lat": 30.724129476258618, "sign": "Libra"},
    "Alphecca": {"lon": 198.44594872982088, "lat": 44.31879461160149, "sign": "Libra"},
    "Zuben Eshamali": {"lon": 205.5174829149257, "lat": 8.493417675530758, "sign": "Libra"},
    "Unukalhai": {"lon": 208.22227556545838, "lat": 25.50452033420928, "sign": "Libra"},
    "Agena": {"lon": 209.9377808195632, "lat": -44.13599183235419, "sign": "Libra"},
    "Rigel Kentaurus": {"lon": 215.6043617570842, "lat": -42.598004633009104, "sign": "Scorpio"},
    "Antares": {"lon": 225.9063118329662, "lat": -4.571525824852803, "sign": "Scorpio"},
    "Lesath": {"lon": 240.1553394395581, "lat": -14.009044269945003, "sign": "Sagittarius"},
    "Vega": {"lon": 261.45535139451795, "lat": 61.72744725222478, "sign": "Sagittarius"},
    "Altair": {"lon": 277.9174050237009, "lat": 29.300815471768857, "sign": "Capricorn"},
    "Deneb Algedi": {"lon": 299.6811182140554, "lat": -2.604137631339397, "sign": "Capricorn"},
    "Fomalhaut": {"lon": 309.9990988361535, "lat": -21.136898342598553, "sign": "Aquarius"},
    "Deneb": {"lon": 311.45796253327063, "lat": 59.90408622617344, "sign": "Aquarius"},
    "Achernar": {"lon": 321.4466157047789, "lat": -59.37830474568324, "sign": "Aquarius"}
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
