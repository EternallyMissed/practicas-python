import math
import json
factorial_10 = str(math.factorial(10))
archivo = open('C:/Users/Missed/Documents/python/test/1.txt', 'w')
with open('C:/Users/Missed/Documents/python/test/1.txt', 'w') as archivo:
    archivo.write(factorial_10)
