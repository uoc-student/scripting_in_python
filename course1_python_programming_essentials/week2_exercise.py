"""
Challenge: Write a Python function triangle_area that takes the parameters 
x_0, y_0, x_1, y_1, x_2 and y_2 (all numbers), and returns the area of the
triangle with vertices (x_0, y_0), ...
Use the function point_distance as a helper function
"""

def point_distance(x_0, y_0, x_1, y_1):
    x_distance = (x_0 - x_1) ** 2
    y_distance = (y_0 - y_1) ** 2
    return (x_distance + y_distance) ** (1/2)


def triangle_area(x_0, y_0, x_1, y_1, x_2, y_2):
    """
    Heron's formula = sqrt(s*(s-a)*(s-b)*(s-c))
    semi-perimeter s = (a + b + c) / 2
    """

    a = point_distance(x_0, y_0, x_1, y_1)
    b = point_distance(x_0, y_0, x_2, y_2)
    c = point_distance(x_1, y_1, x_2, y_2)

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** (1/2)
    area = round(area, 2)

    return area


"""
Challenge: Write a Python function print_digits that takes an integer number 
in the range [0,100) and prints the message "The tens digit is %, and the ones digit is %.",  
where the percent signs should be replaced with the appropriate values. 
(Hint: Use the arithmetic operators for integer division  // and remainder % to find the two digits. 
Note that this function should print the desired message, rather than returning it as a string.
"""

def print_digits(number):
    assert(number >=0 and number < 100)

    tens = number // 10
    ones = number % 10
    print("Then tens digit is " + str(tens) + ", and the ones digit is " + str(ones) + ".")



"""
Challenge: Powerball is lottery game in which 6 numbers are drawn at random. 
Players can purchase a lottery ticket with a specific number combination and, 
if the number on the ticket matches the numbers generated in a random drawing, 
the player wins a massive jackpot. Write a Python function powerball 
that takes no arguments and prints the message "Today’s numbers are %, %, %, %, and %. 
The Powerball number is %.". The first five numbers should be random integers in the range 
[1,60)[1,60). In reality, these five numbers must all be distinct, 
but for this problem, we will allow duplicates. The Powerball number is a random integer in the range [1,36)[1,36).
Note that this function should print the desired message, rather than returning it as a string
"""
import random

def powerball():
    num1 = random.randrange(1, 60)
    num2 = random.randrange(1, 60)
    num3 = random.randrange(1, 60)
    num4 = random.randrange(1, 60)
    num5 = random.randrange(1, 60)
    power_num = random.randrange(1, 36)

    print("Today’s numbers are " + str(num1) + ", " + str(num2) + 
          ", " + str(num3) + ", " + str(num4) + ", " + str(num5) + 
          ". The powerball is " + str(power_num) + ".")


def q5_equation(x):
    return (-5*x**5 + 67*x**2 - 47)

def test5():
    print("0: ", q5_equation(0))
    print("1: ", q5_equation(1))
    print("2: ", q5_equation(2))
    print("3: ", q5_equation(3))

#test5()

def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    FV = present_value * (1 + rate_per_period) **periods
    return FV
    
def test6():
    print("$500 at 4% compounded daily for 10 years yields $", future_value(500, .04, 10, 10))
    print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))

#test6()


def q7_area_equilateral_triangle(side):
    area = (3 ** (1 / 2)  * side ** 2) / 4
    return area

def test7():
    print("2: ", q7_area_equilateral_triangle(2))
    print("5: ", q7_area_equilateral_triangle(5))

test7()