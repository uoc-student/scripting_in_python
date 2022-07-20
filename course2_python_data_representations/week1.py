"""
Template - Function that swaps and capitalizes first and last names
"""


def name_swap(name_string):
    """
    Given the string name string of the form "first last", return 
    the string "Last First" where both names are now capitalized
    """
    
    # Enter code here
    swapped_name = name_string.split(" ")
    swapped_name[0] = swapped_name[0][0].upper() + swapped_name[0][1:]
    swapped_name[1] = swapped_name[1][0].upper() + swapped_name[1][1:]
    return swapped_name[1] + " " + swapped_name[0]

def test_name_swap():
    print("test_name_swap")
    print(name_swap("joe warren") == "Warren Joe")
    print(name_swap("scott rixner") == "Rixner Scott")
    print(name_swap("john greiner") == "Greiner John")
    print("******************")

test_name_swap()


def count_vowels(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    
    for vowel in vowels:
        count += word.count(vowel)

    return count


def test_count_vowels():
    print("test_count_vowels")
    print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
    print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))
    print("******************")

test_count_vowels()


def demystify(l1_string):
    demistified = l1_string.replace('l', 'a')
    demistified = demistified.replace('1', 'b')
    return demistified

def test_demystify():
    print("test_demystify")
    print(demystify("lll111l1l1l1111lll"))
    print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
    print("******************")

test_demystify()