import time

class FiboIter():
    def __init__(self, max=None):
        if max != None:
            assert max > 0, 'El número debe ser mayor a 0'
            print(f'Los fibonacci hasta el número {max} son:')
        else:
            print("Los fibonacci son:")
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.next = 0
        self.counter = 0
        return self

    def __next__(self):
        # If there is a max, and is higher than this iteration fibonacci
        if self.max and self.next >= self.max:
            raise StopIteration # Stop iterations
        elif self.counter == 0:
            self.counter += 1 # Count
            return self.n1 # Return first Fibonacci value
        elif self.counter == 1:
            self.counter += 1 # Count
            return self.n2 # Return second Fibonacci value
        else:
            self.aux = self.n1 + self.n2 # Fibonacci sum

            self.n1, self.n2 = self.n2, self.aux # Swapping

            self.next = self.n1 + self.n2 # Save next value to set a stop

            self.counter += 1 # Count
            return self.aux

def run():
    while True:
        try:
            # Ask for a number
            number = int(input("Ingrese un numero: "))
            # Create class FiboIter
            fibonacci = FiboIter(number)

            # Itinerate through fibonacci
            for element in fibonacci:
                print(element)
                time.sleep(0.5) # Sleep time
            quit()
        except (AssertionError, ValueError) as e:
            print(e)


if __name__ == '__main__':
    run()