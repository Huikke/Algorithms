from random_generator import random_list_generator
from insertion_sort import insertion_sort

def bucket_sort(A):
    n = len(A)
    B = [None] * n
    for i in range(n):
        if B[int(n*A[i])] == None:
            B[int(n*A[i])] = [A[i]]
        else:
            B[int(n*A[i])].append(A[i])
    for i in range(n):
        if B[i] != None:
            insertion_sort(B[i])
    m = 0
    for i in range(n):
        if B[i] != None:
            for j in range(len(B[i])):
                A[m] = B[i][j]
                m += 1


if __name__ == "__main__":
    list = random_list_generator(10, 99, 0)
    for i in range(len(list)):
        list[i] /= 100

    print("List:", list)
    bucket_sort(list)
    print("Result:", list)