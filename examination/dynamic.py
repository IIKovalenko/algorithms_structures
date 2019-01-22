def find_largest_incr_subsequence(a):
    b = [0]*len(a)
    b[0] = 1
    for i in range(1, len(a)):
        max_local = 0
        for j in range(i):
            if a[j] < a[i] and b[j] > max_local:
                max_local = b[j]
        max_seq = max_local + 1
        b[i] = max_seq
    return max(b)


if __name__ == "__main__":
    print(find_largest_incr_subsequence([5, 4, 3, 2, 1, 0]))
    print(find_largest_incr_subsequence([0, 1, 2, 3, 4, 5]))
    print(find_largest_incr_subsequence([1, 2, 1, 7]))