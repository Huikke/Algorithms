from random_generator import random_list_generator
import random

def binary_search(list, find_x):
    A = list
    n = len(list)-1
    x = find_x

    min = 0
    max = n
    while True:
        mid = int((min + max) / 2)
        if A[mid] == x:
            return mid
        elif min > max:
            return -1
        elif x < A[mid]:
            max = mid - 1
        elif x > A[mid]:
            min = mid + 1


if __name__ == "__main__":
    list = sorted(random_list_generator(11, 10, 1))
    x = random.randint(1, 10)
    print("List:", list)
    print("x:", x)
    
    print("Result:", binary_search(list, x) + 1)