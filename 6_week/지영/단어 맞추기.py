import sys
def lexicographically_next_permutation(a):
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i+1]):
        i -= 1
    if i < 0:
        return False
    # else
    j = len(a) - 1
    while not (a[j] > a[i]):
        j -= 1
    a[i], a[j] = a[j], a[i]        # swap
    a[i+1:] = reversed(a[i+1:])    # reverse elements from position i+1 till the end of the sequence
    return True

if __name__ == '__main__':
    for _ in range(int(input())):
        arr = list(map(str, sys.stdin.readline().rstrip()))
        lexicographically_next_permutation(arr)
        print(''.join(arr))