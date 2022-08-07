def make_division_by(n: int):
    """This closure returns a function that returns the division of an x number by n
    """
    # You have to code here:

    def division(x: int):
        # Assert x is an int
        assert type(x) == int, "Solo puedes ingresar números"
        # Return as integer
        return x // n

    # Return division function, remember n value
    return division


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18)) # Expected output 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100)) # Expected output 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54)) # Expected output 3


if __name__ == '__main__':
    run()