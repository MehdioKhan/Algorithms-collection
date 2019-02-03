def merge_sort(low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid + 1, high)
        merge(low, mid, high)


def merge(low, mid, high):
    result = [0 for l in range(high - low + 1)]
    i = low
    k = 0
    j = mid + 1
    global s
    while i <= mid and j <= high:
        if s[i] <= s[j]:
            result[k] = s[i]
            i += 1
        else:
            result[k] = s[j]
            j += 1
        k += 1
    while i <= mid:
        result[k] = s[i]
        i += 1
        k += 1
    while j <= high:
        result[k] = s[j]
        j += 1
        k += 1
    for d in range(low, high - low + 1):
        s[d] = result[d]


def main():
    global s
    s = [6, 7, 43, 2, 5, 6, 7, 12, 3, 4]
    merge_sort(0, len(s)-1)
    print(s)


if __name__ == "__main__":
    main()
