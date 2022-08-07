# Hola 3 -> HolaHolaHola
# Facundo 2 -> FacundoFacundo
# Platzi 4 -> PlatziPlatziPlatziPlatzi

def make_repeater_of(n: int):
    def repeater(string) -> str:
        assert type(string) == str, "Solo puedes utilizar cadenas"
        # Return the string times n(saved)
        return string * n
    # Return repeater
    return repeater


def run():
    # Save the repeat function
    repeat_2 = make_repeater_of(2)
    repeat_3 = make_repeater_of(3)
    repeat_4 = make_repeater_of(4)

    print(repeat_2("Facundo"))
    print(repeat_3("Hola"))
    print(repeat_4("Platzi"))


if __name__ == '__main__':
    run()