from os import remove
from machine import ADC
from util import resistanceToPercentage, formatToPercentage
from averageNumber import averageNumber

INPUT_VOLTAGE = 3.3
KNOWN_RESISTOR = 330
CONVERSION_FACTOR = INPUT_VOLTAGE / 65535
R1 = 5000000
ROLLING_WINDOW = 20

WOOD_TYPE = 'douglas'
# WOOD_TYPE = 'fur white'
# WOOD_TYPE = 'white pine'

print('Wood Type: ', WOOD_TYPE)

aPin = ADC(26)
i = 0

while True:
    aV = aPin.read_u16()
    aVolt = aV * CONVERSION_FACTOR
    
    # Pull this out to check if it isn't 0
    x = INPUT_VOLTAGE - aVolt
    
    if x != 0:
        i = i + 1
        resistance = aVolt * R1 / x

        avgResistance = averageNumber(resistance)

        if i == ROLLING_WINDOW:
            avgPercent = resistanceToPercentage(avgResistance, WOOD_TYPE)
            print("Avg Moisture Content: ", formatToPercentage(avgPercent))
            break