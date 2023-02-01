from random_generator import random_list_generator

def insertion_sort(list):
    A = list

    for j in range(1, len(list)):
        new = A[j]
        i = j - 1
        while i >= 0 and A[i] > new:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = new


if __name__ == "__main__":
    list = random_list_generator(20, 100, 1)
    print("List:", list)
    insertion_sort(list)
    print("Result:", list)