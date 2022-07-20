import random
import string


def generate_random_alphabet():
    alphabet_letters = string.ascii_lowercase
    random_order = random.sample(alphabet_letters, len(alphabet_letters))
    return ''.join(random_order)


if __name__ == '__main__':
    print(generate_random_alphabet())
