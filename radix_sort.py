from random_generator import random_list_generator

def radix_sort(A, d):
    for i in range(d-1, -1, -1):
        B = [0] * len(A)
        radix_counting_sort(A, B, 10, i)
        for i in range(len(A)): # For transfering the new list to old one without losing the link to the original list
            A[i] = B[i]

def radix_counting_sort(A, B, k, d):
    C = [0] * k
    for j in range(len(A)):
        C[int(A[j][d])] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[int(A[j][d])]-1] = A[j]
        C[int(A[j][d])] -= 1


if __name__ == "__main__":
    list = random_list_generator(10, 999, 1)
    for i in range(len(list)):
        if list[i] < 10:
            list[i] = "00" + str(list[i])
        elif list[i] < 100:
            list[i] = "0" + str(list[i])
        else:
            list[i] = str(list[i])

    print("List:", list)
    radix_sort(list, 3)
    print("Result:", list)