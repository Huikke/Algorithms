from random_generator import random_list_generator
import random

def quick_select(A, p, r, i):
    if p == r:
        return A[p]
    q = partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return quick_select(A, p, q-1, i)
    elif i > k:
        return quick_select(A, q+1, r, i-k)

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
    list = random_list_generator(10, 100, 1)
    i = random.randint(1, len(list))

    print("List:", list)
    print("i:", i)
    print("Result:", quick_select(list, 0, len(list)-1, i))
    print("List after:", list)