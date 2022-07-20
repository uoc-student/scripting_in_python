"""
There are 5280 feet in a mile. Write a Python statement that calculates and prints the number of feet in 1313 miles. 
"""

def milesToFeet(miles):
    feet_in_mile = 5280
    total_feet = feet_in_mile * miles
    
    return total_feet

def test1():
    print(milesToFeet(13) == 68640)

test1()


"""
Write a Python statement that calculates and prints the number of seconds in 7 hours, 21 minutes and 37 seconds.
"""
def timeToSeconds(hours, minutes, seconds):
    return (hours * 60 * 60 + minutes * 60 + seconds)

def test2():
    print(timeToSeconds(7, 21, 37) == 26497)

test2()


"""
The perimeter of a rectangle is 2w + 2h, where w and h are the lengths of its sides. 
Write a Python statement that calculates and prints the length in inches of the perimeter 
of a rectangle with sides of length 4 and 7 inches. 
"""

def perimeterRectangle(w, h):
    return (2 * w + 2 * h)

def test3():
    print(perimeterRectangle(4, 7) == 22)

test3()


"""
The area of a rectangle is wh, where ww and hh are the lengths of its sides. 
Note that the multiplication operation is not shown explicitly in this formula. 
This is standard practice in mathematics, but not in programming. 
Write a Python statement that calculates and prints the area in square inches of a 
rectangle with sides of length 4 and 7 inches.
"""

def areaRectangle(w, h):
    return (w * h)

def test4():
    print(areaRectangle(4, 7) == 28)

test4()


"""
The circumference of a circle is 2πr where r is the radius of the circle. 
Write a Python statement that calculates and prints the circumference in inches 
of a circle whose radius is 8 inches. Assume that the constant π=3.14. 
"""
pi = 3.14

def circumference(r):
    return (2 * pi * r)

def test5():
    print(circumference(8) == 50.24)

test5()


"""
The area of a circle is πr^2 where r is the radius of the circle. 
Write a Python statement that calculates and prints the area in square inches 
of a circle whose radius is 8 inches. Assume that the constant π=3.14.
"""
def areaCircle(r):
    return (pi * r ** 2)

def test6():
    print(areaCircle(8) == 200.96)

test6()


"""
Given p dollars, the future value of this money when compounded yearly 
at a rate of rr percent interest for y years is p(1+0.01r)^y
Write a Python statement that calculates and prints the value of 
1000 dollars compounded at 7 percent interest for 10 years.
"""

def compInterest(dollars, rate, years):
    compounded_return = dollars * (1 + 0.01 * rate)**years\
    
    return compounded_return

def test7():
    print(compInterest(1000, 7, 10) == 1967.1513572895665)

test7()


"""
Write a single Python statement that combines the three strings "My name is", "Joe" and "Warren"
(plus a couple of other small strings) into one larger string"My name is Joe Warren."
and prints the result.
"""

def concatenateStrings(str1, str2, str3):
    return str1 + " " + str2 + " " + str3 + "."

def test8():
    print ("My name is Joe Warren." == concatenateStrings("My name is", "Joe", "Warren"))

test8()


"""
Write a Python expression that creates the string "Joe Warren is 56 years old." 
from several strings including "Joe Warren" and the number 56 and then prints the result.
"""

def concatenateNumStr(str, num):
    return (str + " is", num, "years old.")

def test9():
    print(("Joe Warren is", 56, "years old.") == concatenateNumStr("Joe Warren", 56))

test9()


"""
+++ Challenge +++
The distance between two points (x0,y0) and (x1,y1) is srt((x0 - x1)^2 + (y0 - y1)^2).
Write a Python statement that calculates and prints the distance between the points (2, 2) and (5, 6). 
(Hint: Remember that a square root can be computed by raising a value to the 0.5 power.)
"""

def distanceTwoPoints(x0, y0, x1, y1):
    xs = (x0 - x1)**2
    ys = (y0 - y1)**2
    distance = (xs + ys)**(1/2)

    return distance

def test10():
    print(distanceTwoPoints(2, 2, 5, 6) == 5.0)

test10()


