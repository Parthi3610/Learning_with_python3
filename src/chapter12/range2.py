import random


def make_random_no_dup(num, lower_value, higher_value):

    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_value, higher_value)
            if candidate not in result:
                break
        result.append(candidate)
    return result

xs = make_random_no_dup(5,1,6)
print(xs)