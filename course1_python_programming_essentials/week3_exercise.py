"""
Write a Python function is_even that takes as input the parameter number (an integer) 
and returns True if number is even and False if number is odd. 
Hint: Apply the remainder operator to number % 2 and compare to zero.
"""

def is_even(number):
    return (number % 2 == 0)


def test1():
    print(is_even(8) == True)
    print(is_even(3) == False)
    print(is_even(12) == True)


#test1()


"""
Write a Python function is_cool that takes as input the string name 
and returns True if name is either "Joe", "John" or "Stephen" and returns False otherwise. 
(Let's see if Scott manages to catch this. ☺ ) 
"""

def is_cool(name):
    return (name == "Joe" or name == "John" or name == "Stephen")


def test2():
    name = "Joe"
    if is_cool(name):
        print(name, "is cool.")
    else:
        print(name, "is not cool.")

    name = "John"
    if is_cool(name):
        print(name, "is cool.")
    else:
        print(name, "is not cool.")
        
    name = "Stephen"
    if is_cool(name):
        print(name, "is cool.")
    else:
        print(name, "is not cool.")
        
    name = "Scott"
    if is_cool(name):
        print(name, "is cool.")
    else:
        print(name, "is not cool.")


#test2()


"""
Write a Python function is_lunchtime that takes as input the parameters 
hour (an integer in the range [1, 12][1,12]) and is_am 
(a Boolean “flag” that represents whether the hour is before noon). 
The function should return True when the input corresponds to 11am or 12pm (noon) 
and False otherwise. If the problem specification is unclear, look at the test cases 
in the provided template. Our solution does not use conditional statements.
"""

def is_lunchtime(hour, is_am):
    return ((hour == 11 and is_am) or (hour == 12 and not is_am))


def test3():
    def is_lunchtime_test(hour, is_am):
        """Tests the is_lunchtime function."""
        print(hour, end = "")
        if is_am:
            print("AM", end = "")
        else:
            print("PM", end = "")
        if is_lunchtime(hour, is_am):
            print(" is lunchtime.")
        else:
            print(" is not lunchtime.")

    is_lunchtime_test(11, True)
    is_lunchtime_test(12, True)
    is_lunchtime_test(11, False)
    is_lunchtime_test(12, False)
    is_lunchtime_test(10, False)


#test3()


"""
Write a Python function is_leap_year that take as input the parameter year 
and returns True if year (an integer) is a leap year according to the Gregorian calendar 
and False otherwise. The Wikipedia entry for leap years contains a simple algorithmic rule 
for determining whether a year is a leap year. 
Your main task will be to translate this rule into Python
"""

def is_leap_year(year):
    return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))


def test4():
    print(is_leap_year(2000) == True)
    print(is_leap_year(1996) == True)
    print(is_leap_year(1800) == False)
    print(is_leap_year(2013) == False)


#test4()


"""
Write a Python function interval_intersect that takes parameters a, b, c, and d 
and returns True if the intervals [a, b] and [c, d] intersect and False otherwise. 
While this test may seem tricky, the solution is actually very simple and consists of one line of Python code. 
(You may assume that  a≤b and c≤d.)
"""

def interval_intersect(segment1_lower, segment1_upper, segment2_lower, segment2_upper):
    return ((segment1_lower <= segment2_upper) and (segment1_upper >= segment2_lower))

def test5():
    print(interval_intersect(0, 1, 0, 2) == True)
    print(interval_intersect(1, 2, 0, 1) == True)
    print(interval_intersect(0, 1, 2, 3) == False)
    print(interval_intersect(2, 3, 0, 1) == False)
    print(interval_intersect(0, 3, 1, 2) == True)
    print(interval_intersect(2, 4, 2, 4) == True)


#test5()

"""
Write a Python function name_and_age that take as input the parameters name (a string) 
and age (a number) and returns a string of the form "% is % years old." 
where the percents are the string forms of name and age. 
The function should include an error check for the case when age is less than zero. 
In this case, the function should return the string "Error: Invalid age".
"""

def name_and_age (name, age):
    if age < 0:
        return "Error: Invalid age"
    return name + " is " + str(age) + " years old."



"""
Write a Python function print_digits that takes an integer number in the range [0,100) 
and prints the message "The tens digit is %, and the ones digit is %." 
Where the percents should be replaced with the appropriate values. The function should include an error check 
for the case when number is negative or greater than or equal to 100. In those cases, the function should 
instead print "Error: Input is not a two-digit number."
"""

def print_digits(number):
    if number >= 100 or number < 0:
        print("Error: Input is not a two-digit number.")
    else:
        print("The tens digit is " + str(number // 10) + " and the ones digit is " + str(number % 10) + ".")


"""
Write a Python function name_lookup that takes a string first_name 
that corresponds to one of "Joe", "Scott", "John" or "Stephen" 
and then returns their corresponding last name "Warren", "Rixner", "Greiner" or "Wong". 
If first_name doesn't match any of those strings, return the string "Error: Not an instructor".
"""

def name_lookup(name):
    instructors = {"Joe":"Warren", "Scott":"Rixner", "John":"Greiner", "Stephen":"Wong"}

    if name in instructors:
        return (instructors[name])
    else:
        return "Error: Not an instructor"


def test8():
    first_name = "Joe"
    print(first_name + "'s last name is", name_lookup(first_name))
          
    first_name = "Scott"
    print(first_name + "'s last name is", name_lookup(first_name))
          
    first_name = "John"
    print(first_name + "'s last name is", name_lookup(first_name))
          
    first_name = "Stephen"
    print(first_name + "'s last name is", name_lookup(first_name))
          
    first_name = "Mary"
    print(first_name + "'s last name is", name_lookup(first_name))


#test8()


"""
Pig Latin is a language game that involves altering words via a simple set of rules. 
Write a Python function pig_latin that takes a string word and applies the following rules 
to generate a new word in Pig Latin. If the first letter in word is a consonant, 
append the consonant plus "ay" to the end of the remainder of the word. 
For example, pig_latin("pig") would return "igpay". If the first letter in word is a vowel, 
append "way" to the end of the word. For example, pig_latin("owl") returns "owlway". 
You can assume that word is in lower case. The provided template includes code to extract the first letter 
and the rest of word in Python. Note that, in full Pig Latin, the leading consonant cluster is moved to the end of the word. 
However, we don't know enough Python to implement full Pig Latin just yet.
"""

def pig_latin(word):
    vowels = ["a", "e", "i", "o", "u"]

    if word[0] in vowels:
        return word + "way"
    else:
        return word[1 : ] + word[0] + "ay"


def test9():
    word = "pig"
    print(pig_latin(word) == "igpay")

    word = "owl"
    print(pig_latin(word) == "owlway")

    word = "python"
    print(pig_latin(word) == "ythonpay")


#test9()


"""
Challenge: Given numbers a, b, and c, the quadratic equation a x^2 + b x + c = 0 
can have zero, one or two real solutions. 
Write a Python function smaller_root that takes an input the numbers a, b and c 
and returns the smaller solution to this equation if one exists. 
If the equation has no real solution, print the message "Error: No real solutions" and simply return. 
Note that, in this case, the function will actually return the special Python value None
"""

def smaller_root (a, b, c):
    discriminant = (b ** 2) - (4 * a * c)

    if (discriminant < 0 or a == 0):
        print("Error: No real solutions")
        return

    sol1 = (-b + discriminant ** (1/2)) / (2 * a)
    sol2 = (-b - discriminant ** (1/2)) / (2 * a) 

    return (min(sol1, sol2))

def test10():
    print(smaller_root (1, 2, 3)) # No solution
    print(smaller_root (2, 0, -10)) # -2.2360
    print(smaller_root (6, -3, 5)) # No solution

#test10()


def collatz_conjecture(number, times):  

    if times == 0:
        print("result: ", number)
        return number
    else:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1

        times -= 1
        collatz_conjecture(number, times)


def test11():
    collatz_conjecture(1071, 14)


#test11()
