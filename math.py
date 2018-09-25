import math

#The equation quadratic
print("Hi, want some help with equation quadratic? insert number below")
a = input("enter 'a':")
b = input("enter 'b':")
c = input("enter 'c':")

a = int(a)
b = int(b)
c = int(c)

D = b**2 - 4 * a * c
print('The D is:')
print(D)
if D > 0:
    x1 = ( -b + math.sqrt(D) ) / 2 * a
    x2 = ( -b - math.sqrt(D) ) / 2 * a
    print("That's good, you have solutions!")
    print(round(float(x1)), round(float(x2)))
elif D < 0:
    try:
     raise ValueError
    except ValueError:
      print ('Oh, not this time')
elif D == 0:
    print('A solution for this one')
    x = ( -b + math.sqrt(D) ) / 2 * a
    print(round(float(x)))
