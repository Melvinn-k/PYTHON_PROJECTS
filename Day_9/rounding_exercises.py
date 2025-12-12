#Basic Rounding
#Round the number 7.68 to the nearest whole number.
num = 7.68
print(round(num))

#Decimal Places
#Round 12.34567 to 2 decimal places.
number = 12.34567
print(round(number, 2))

#More Decimal Places
#Round 98.123456 to 4 decimal places.
num = 98.123456
print(round(num, 4))

#Always Round Down
#Use floor rounding to round 9.999 down.
import math 
print(math.floor(9.999))

#Always Round Up
#Use ceil rounding to round 6.0001 up.
import math
num = 6.0001
print(math.ceil(num))

#Convert to Money Format
#Format 4500.5 to exactly 2 decimal places (like currency).
price = 4500.5
print(f"{price:.2f}")

#Remove Decimals Completely
#Convert 89.765 to an integer (no decimals).
x = 89.765
print(int(x))

#Combined Rounding
#Round 3.5555 to 2 decimal places → what do you get?
num = 3.5555
print(round(num, 2))

#Real-world: Shopping VAT
#A product costs 254.789 Ksh.
#Round the price to 2 decimal places.
cost = 254.789
print(f"{cost:.2f}")

#Real-world: Taxi App
#A distance recorded is 12.0001 km.
#Round it up to charge the customer correctly.
import math
distance = 12.0001
print(math.ceil(distance))

