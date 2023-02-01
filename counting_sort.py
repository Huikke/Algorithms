from random_generator import random_list_generator

def counting_sort(A, B, k):
    C = [0] * k
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1


if __name__ == "__main__":
    max = 14
    length = 10
    list = random_list_generator(length, max, 0)
    list2 = [0] * length

    print("List:", list)
    counting_sort(list, list2, max+1)
    print("Result:", list2)