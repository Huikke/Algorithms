import random

def random_list_generator(length = 10, max = 100, min = 1):
    list = [random.randint(min, max) for i in range(0, length)]
    return list


if __name__ == "__main__":
    print(random_list_generator())