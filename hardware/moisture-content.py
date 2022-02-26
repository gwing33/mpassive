from os import remove
from machine import ADC
from util import resistanceToPercentage
import time

INPUT_VOLTAGE = 3.3
KNOWN_RESISTOR = 10000000
CONVERSION_FACTOR = 3.3 / 65535

bPin = ADC(28)
cPin = ADC(26)
memo = []
total = 0

while True:
    bV = bPin.read_u16()
    cV = cPin.read_u16()
    bVolt = bV * CONVERSION_FACTOR
    cVolt = cV * CONVERSION_FACTOR

    if cVolt > bVolt:
        print('BELOW: ', bV, cV)
    else:
        d_V_ab = INPUT_VOLTAGE - bVolt
        current = d_V_ab / KNOWN_RESISTOR

        if current == 0:
            print('Zero current')
        else:
            resistance = (bVolt - cVolt) / current

            total = total + resistance
            memo.append(resistance)

            if len(memo) > 60:
                removeVal = memo[0]
                total = total - removeVal
                memo.pop(0)

            avgResistance = total / len(memo)
            avgPercent = resistanceToPercentage(avgResistance)
            percent = resistanceToPercentage(resistance)
            print("Resistance: ", resistance, percent)
            print("Avg: ", avgPercent)
            print("\n")
    time.sleep_ms(1000)
