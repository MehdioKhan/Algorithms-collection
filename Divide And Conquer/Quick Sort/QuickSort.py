def quick_sort(low, high):
    if low < high:
        pivot_point = partition(low, high)
        quick_sort(low, pivot_point)
        quick_sort(pivot_point+1, high)


def partition(low, high):
    pp = s[low]  # or pp=low
    j = low
    for i in range(low + 1, high + 1):
        if s[i] < pp:  # or if s[i]<s[j]:
            j += 1  # or comment
            s[i], s[j] = s[j], s[i]
            # j += 1  # or uncomment

    pp = j
    s[low], s[pp] = s[pp], s[low]  # or delete
    return pp


def main():

    global s
    s = [1, 7, 8, 6]
    print(s)
    quick_sort(0, len(s)-1)
    print(s)


if __name__ == '__main__':
    main()
