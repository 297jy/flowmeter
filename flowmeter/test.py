import struct
from flowmeter.common.api import math


x = [int('01', 16), int('17', 16), int('00', 16), int('00', 16)]
print("%.300lf" % math.calculate_double(x))

