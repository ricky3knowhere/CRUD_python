import random, string


def random_string(length: int) -> str:
    result = "".join(random.choice(string.ascii_letters) for i in range(length))
    return result
