memo = []
total = 0
count = 0

def averageNumber(number):
    global total
    global count
    count = count + 1
    total = total + number
    
    return total / count