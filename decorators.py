from datetime import datetime

# Decorator to know how many times a function take to execute
def execution_time(func):
    def wrapper(*args, **kwargs):
        # Save initial time
        initial_time = datetime.now()
        func(*args, **kwargs)
        # Save final time
        final_time = datetime.now()
        # know the difference between them
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    # Closure
    return wrapper


@execution_time # Decorator
def random_func():
    # Itinerate through, without saving his index
    for _ in range(1, 100000000):
        pass


@execution_time # Decorator
def suma(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    suma(5, 5)
    random_func()