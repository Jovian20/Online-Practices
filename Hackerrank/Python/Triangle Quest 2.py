# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

AC = math.sqrt(AB**2 + BC**2)

MC = AC/2

rad_c = math.asin(AB/AC) 
MB=math.sqrt(BC**2+MC**2-math.cos(rad_c)*(2*BC*MC))
rad_mb=math.acos((MB**2+BC**2-MC**2)/(2*MB*BC))
print(str(round(180/math.pi*rad_mb))+chr(176))
