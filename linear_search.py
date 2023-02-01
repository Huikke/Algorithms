from random_generator import random_list_generator
import random

def linear_search(list, find_x):
    A = list
    n = len(list)-1
    x = find_x

    i = 0
    while i <= n:
        if A[i] == x:
            return i
        else:
            i += 1
    return -1


if __name__ == "__main__":
    list = random_list_generator(11, 10, 1)
    x = random.randint(1, 10)
    print("List:", list)
    print("x:", x)
    
    print("Result:", linear_search(list, x) + 1)