from random_generator import random_list_generator

def min(A):
    min = A[0]
    for i in range(1, len(A)):
        if A[i] < min:
            min = A[i]
    return min

def max(A):
    max = A[0]
    for i in range(1, len(A)):
        if A[i] > max:
            max = A[i]
    return max

def minmax(A, n):
    for i in range(1, n//2+1):
        if A[2*i-2] > A[2*i-1]:
            A[2*i-2], A[2*i-1] = A[2*i-1], A[2*i-2]
    min = A[0]
    for i in range(2, n, 2): # n+1 so the equation rolls upward
        if A[i] < min:
            min = A[i]
    max = A[n-1]
    i = 1
    while i < n:
        if A[i] > max:
            max = A[i]
        i += 2
    return min, max


if __name__ == "__main__":
    list = random_list_generator(10, 20, 1)
    print("List:", list)
    print("Min:", min(list))
    print("Max:", max(list))
    print("Minmax:", minmax(list, len(list)))