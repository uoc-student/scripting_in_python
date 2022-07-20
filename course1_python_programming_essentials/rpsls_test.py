import rpsls


def test_name_to_number():
    print("Test calls to name_to_number")
    print(rpsls.name_to_number("rock") == 0)
    print(rpsls.name_to_number("Spock") == 1)
    print(rpsls.name_to_number("paper") == 2)
    print(rpsls.name_to_number("lizard") == 3)
    print(rpsls.name_to_number("scissors") == 4)
    print(rpsls.name_to_number("spool") == "Bad name input")
    print("*****************************")

test_name_to_number()


def test_number_to_name():
    print("Test calls to number_to_name")
    print(rpsls.number_to_name(0) == "rock")
    print(rpsls.number_to_name(1) == "Spock")
    print(rpsls.number_to_name(2) == "paper")
    print(rpsls.number_to_name(3) == "lizard")
    print(rpsls.number_to_name(4) == "scissors")
    print(rpsls.number_to_name(5) == "Bad number input")
    print("*****************************")

test_number_to_name()


def test_rpsls(): 
    print("Test calls to rpsls")
    rpsls.rpsls("rock")
    rpsls.rpsls("Spock")
    rpsls.rpsls("paper")
    rpsls.rpsls("lizard")
    rpsls.rpsls("scissors")
    print("*****************************")

test_rpsls()