# This is a decorator
def uppercases(func):
    # Have an indented function
    def envelope(text):
        # Make text in upper
        return func(text).upper()
    # With a clousure
    return envelope


# Apply decorator via sugar syntax
@uppercases
def message(name):
    # Return a message with the parameter in it
    return f'{name}, recibiste un mensaje'
    

if __name__ == '__main__':
    # Print message with the string 'Fabricio'
    print(message('Fabricio'))