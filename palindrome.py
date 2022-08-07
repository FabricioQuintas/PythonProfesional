# Checked this file with mypy

# Function that receive a string and return a boolean
def is_palindrome(string: str) -> bool:
    # Replace all spaces, lowercase it, and strip
    string = string.replace(" ", "").lower().strip()
    # Return the boolean if is palindrome
    return string == string[::-1]


def run():
    print(is_palindrome('Hola Mundo!'))


if __name__ == '__main__':
    run()