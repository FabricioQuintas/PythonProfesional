import time as t

def fibo_gen(max = None):
    a, b = 0, 1
    while True:
        if max and max <= a:
            break
        else:
            yield a
            a, b = b, a+b

def run():
    while True:
        try:
            # Ask for a number
            number = int(input("Ingrese un numero: "))
            assert number > 0, "El número debe ser mayor a 0, por favor vuelva a intentarlo"
            
            fibonacci = fibo_gen(number)

            # Itinerate through fibonacci
            for element in fibonacci:
                print(element)
                t.sleep(1) # Sleep time
            quit()
        except (AssertionError, ValueError) as e:
            print(e)

if __name__ == '__main__':
    run()