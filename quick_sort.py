from random_generator import random_list_generator

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


if __name__ == "__main__":
    list = random_list_generator(20, 100, 1)
    print("List:", list)
    quick_sort(list, 0, len(list)-1)
    print("Result:", list)