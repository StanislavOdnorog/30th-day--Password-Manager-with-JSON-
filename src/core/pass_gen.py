import random
import string


class PassGen:
    @staticmethod
    def generate_pass():
        letters = list(string.ascii_letters)
        numbers = list(string.digits)
        symbols = ["!", "#", "$", "%", "&", "*", "+"]
        password = []

        [password.append(random.choice(letters)) for _ in range(random.randint(4, 8))]
        [password.append(random.choice(symbols)) for _ in range(random.randint(4, 8))]
        [password.append(random.choice(numbers)) for _ in range(random.randint(4, 8))]

        random.shuffle(password)
        return "".join(password)
