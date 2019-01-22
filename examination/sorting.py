import random

# quadratic sorting
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def insertion_sort(a):
    for i in range(1, len(a)):
        j = i-1
        while j >= 0 and a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            j -= 1
    return a


def selection_sort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a


def count_sort(a, k):
    b = [0]*(k+1)
    for num in a:
        b[num] += 1

    i = 0
    for num, count in enumerate(b):
        for j in range(i, i+count):
            a[j] = num
        i = i+count

    return a


def merge_sort(a):
    if len(a) > 1:
        split_idx = len(a) // 2
        a_left, a_right = a[:split_idx], a[split_idx:]
        merge_sort(a_left)
        merge_sort(a_right)
        i, j, idx = 0, 0, 0
        while i < len(a_left) and j < len(a_right):
            if a_left[i] < a_right[j]:
                a[idx] = a_left[i]
                i += 1
            else:
                a[idx] = a_right[j]
                j += 1
            idx += 1

        while i < len(a_left):
            a[idx] = a_left[i]
            i += 1
            idx += 1

        while j < len(a_right):
            a[idx] = a_right[j]
            j += 1
            idx += 1
        return a

    else:
        return a


def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        q = random.choice(a)
        l = [x for x in a if x < q]
        m = [x for x in a if x == q]
        r = [x for x in a if x > q]
        return quick_sort(l) + m + quick_sort(r)

if __name__ == '__main__':
    print(bubble_sort([5, 4, 3, 2, 1, 0]))
    print(insertion_sort([5, 4, 3, 2, 1, 0]))
    print(selection_sort([5, 4, 3, 2, 1, 0]))
    print(count_sort([5, 4, 3, 2, 1, 0, 0, 0, 4, 1], 5))
    print(merge_sort([5, 4, 3, 2, 1]))
    print(quick_sort([-1, 0, 14, 5, 5, 1, 2, -5, 17]))
