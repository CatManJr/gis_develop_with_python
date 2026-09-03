from math import log,tan,pi
import sys
lng = float(sys.argv[1])
lat = float(sys.argv[2])
r = 20037508.34
x = int(lng*r/180) 
y = int(log(tan(pi/4+lat*pi/360))*(r/pi))  
print(f"x:{x},y:{y}")