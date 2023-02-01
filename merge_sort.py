from random_generator import random_list_generator
import math

def merge_sort(A, p, r):
    if p < r:
        q = (p + (r-1)) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    V = [0] * n1
    O = [0] * n2
    
    for i in range(n1):
        V[i] = A[p+i]
    for j in range(n2):
        O[j] = A[q+1+j]
    V.append(math.inf)
    O.append(math.inf)

    i = 0
    j = 0

    for k in range(p, r+1):
        if V[i] <= O[j]:
            A[k] = V[i]
            i += 1
        elif V[i] > O[j]:
            A[k] = O[j]
            j += 1


if __name__ == "__main__":
    list = random_list_generator(10, 100, 1)
    print("List:", list)
    merge_sort(list, 0, len(list)-1)
    print("Result:", list)