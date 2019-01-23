def find_longest_incr_subsequence(a):
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


def find_longest_cmn_subsequence(s1, s2):
    n, m = len(s1), len(s2)
    arr = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                arr[i+1][j+1] = arr[i][j] + 1
            else:
                arr[i+1][j+1] = max(arr[i+1][j], arr[i][j+1])
    return arr[-1][-1]

if __name__ == "__main__":
    print(find_longest_incr_subsequence([5, 4, 3, 2, 1, 0]))
    print(find_longest_incr_subsequence([0, 1, 2, 3, 4, 5]))
    print(find_longest_incr_subsequence([1, 2, 1, 7]))
    print(find_longest_cmn_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6]))
