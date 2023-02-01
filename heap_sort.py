from random_generator import random_list_generator

def heap_sort(A):
    form_heap(A)
    A_heap = len(A) - 1

    for i in range(A_heap, 0, -1):
        A[0], A[i] = A[i], A[0]
        fix_heap(A, 0, i)

def form_heap(A):    
    for i in range(len(A) // 2 - 1, -1, -1):
        fix_heap(A, i, len(A))

def fix_heap(A, i, heap_size):
    biggest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heap_size and A[left] > A[i]:
        biggest = left
    if right < heap_size and A[right] > A[biggest]:
            biggest = right
    if biggest != i:
        A[i], A[biggest] = A[biggest], A[i]
        fix_heap(A, biggest, heap_size)


def max(A, heap_size):
    if heap_size < 0:
        print("Heap is empty")
        return None
    else:
        return A[0]
    
def delete_max(A, heap_size):
    if heap_size < 0:
        print("Heap is empty")
        return None
    else:
        max = A[0]
        A[0] = A[heap_size]
        heap_size -= 1
        fix_heap(A, 0, heap_size)
        return max

def increase_priority(A, i, key):
    if key < A[i]:
        print("New value can't be smaller than previous value")
        return None
    else:
        A[i] = key
        parent = A[(i + 1) // 2 - 1]
        while i > 0 and parent < i[i]:
            A[i], A[parent] = A[parent], A[i]
            i = parent

def add(A, key, heap_size):
    heap_size += 1
    A[heap_size] = -1 # On the basis the list contains on natural numbers, otherwise should be -∞
    increase_priority(A, heap_size, key)


if __name__ == "__main__":
    list = random_list_generator(20, 100, 1)
    print("List:", list)
    form_heap(list)
    print("Heap Form:", list)
    heap_sort(list)
    print("Result:", list)

# Note: max, delete_max, increase_priority and add functions haven't been tested