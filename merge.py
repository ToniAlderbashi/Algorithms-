# By: Tonia Alderbashi
# Merge sort algorithm

from random import randrange


def mergeSort(array):

    size = len(array)
    if size > 1:
        front = array[:size//2]
        back = array[size//2:]
        mergeSort(front)
        mergeSort(back)

        return merge(front, back, array)


def merge(front, back, array):
    p = len(front)
    q = len(back)

    i = j = k = 0

    while i < p and j < q:
        if front[i] <= back[j]:
            array[k] = front[i]
            i += 1
        else:
            array[k] = back[j]
            j += 1
        k += 1

    if i == p:

        while back[j:]:
            array[k] = back[j]
            j += 1
            k += 1

    else:

        while front[i:]:
            array[k] = front[i]
            i += 1
            k += 1

    return array


def main():
    size = randrange(10, 100)
    lst = [randrange(0, size) for j in range(size)]

    print(mergeSort(lst))


main()


def stats():
    print("Hello")
