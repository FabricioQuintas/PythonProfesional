# Def will receive an integer, and return a boolean
def is_prime(num: int) -> bool:
    # Itinerate from 1 to the number on the argument
    # If num % x == 0, its a divisor
    divs = [x for x in range(1,num+1) if num%x == 0]
    # Return true if have only 2 divs (prime number)
    return len(divs) == 2


def run():
    # Set a int number
    number: int = 8
    # Print if is prime
    print(is_prime(number))


if __name__ == '__main__':
    run()