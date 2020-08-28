def collatz(number):
    number = (number // 2) if (number % 2 == 0) else (number * 3 + 1)
    print(number)
    return number


def get_integer_from_user():
    print('Type in an integer')
    is_valid_integer = False
    while (not is_valid_integer):
        number = input()
        try:
            return int(number)
        except ValueError:
            print('That is not an integer. Please try again')


def start_collatz_loop():
    number = get_integer_from_user()
    while (not (number == 1)):
        number = collatz(number)


start_collatz_loop()
