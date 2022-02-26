from decimal import MAX_PREC


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

def getWoodResistance(woodType = 'douglas'):
    if woodType == 'douglas':
        return douglasFurMcToMegaOhms
    return []

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
        
        if resistance > ohm:
            if i == 0:
                percent = mc
                break
            
            prevMcToMegaOhm = douglasFurMcToMegaOhms[i - 1]
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