from cmath import log


MEGA_OHM = 1000000
MIN_PERCENT = 7
MAX_PRECENT = 25

douglasFurMcToMegaOhms = [
    [7, 22400],
    [8, 4780],
    [9, 1660],
    [10, 630],
    [11, 265],
    [12, 120],
    [13, 60],
    [14, 33],
    [15, 18.6],
    [16, 11.2],
    [17, 7.1],
    [18, 4.6],
    [19, 3.09],
    [20, 2.14],
    [21, 1.51],
    [22, 1.1],
    [23, 0.79],
    [24, 0.6],
    [25, 0.46],
]

furWhiteMcToMegaOhms = [
    [7, 57600],
    [8, 15850],
    [9, 3980],
    [10, 1120],
    [11, 415],
    [12, 180],
    [13, 83],
    [14, 46],
    [15, 26.9],
    [16, 16.6],
    [17, 11],
    [18, 6.6],
    [19, 4.47],
    [20, 3.02],
    [21, 2.14],
    [22, 1.55],
    [23, 1.12],
    [24, 0.86],
    [25, 0.62],
]

whitePineMcToMegaOhms = [
    [7, 20900],
    [8, 5620],
    [9, 2090],
    [10, 850], # 850,000,000
    [11, 405],
    [12, 200],
    [13, 102],
    [14, 58],
    [15, 33.1],
    [16, 19.9],
    [17, 12.3],
    [18, 7.9],
    [19, 5.01],
    [20, 3.31],
    [21, 2.19],
    [22, 1.51],
    [23, 1.05],
    [24, 0.74],
    [25, 0.52],
]

def getWoodResistance(woodType = 'douglas'):
    if woodType == 'fur white':
        return furWhiteMcToMegaOhms
    
    if woodType == 'white pine':
        return whitePineMcToMegaOhms

    return douglasFurMcToMegaOhms

def resistanceToPercentage(resistance, woodType = 'douglas'):
    i = 0
    percent = MAX_PRECENT
    woodResistances = getWoodResistance(woodType)

    for mcToMegaOhm in woodResistances:
        # No reason to keep looping
        if percent != MAX_PRECENT:
            break

        mc = mcToMegaOhm[0]
        ohm = mcToMegaOhm[1] * MEGA_OHM
        
        if resistance == ohm:
            percent = mc
            break

        if resistance > ohm:
            if i == 0:
                percent = mc
                break
            
            prevMcToMegaOhm = woodResistances[i - 1]
            prevMc = prevMcToMegaOhm[0]
            prevMegaOhm = prevMcToMegaOhm[1] * MEGA_OHM

            subPercent = (resistance - ohm) / (prevMegaOhm - ohm)
            totalPercent = prevMc + subPercent
            percent = totalPercent
            break;
        
        i += 1
    
    return percent

def formatToPercentage(number):
    if number >= MAX_PRECENT:
        return '>25%'
    if number <= MIN_PERCENT:
        return '<7%'
    return "{0}%".format(round(number, 2))