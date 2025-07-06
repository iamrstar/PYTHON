import math
def circle_stats(radius):
  area =  math.pi* radius ** 2
  circumference =  2 * math.pi * radius ** 2
  return round (area,2) ,round( circumference,2)

a , c = circle_stats (3)

print('area: ', a, 'circumference: ', c)

