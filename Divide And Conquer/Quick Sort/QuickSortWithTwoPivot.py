def quick_sort(low, high):
    if low < high:
        pivot_point1 = partition1(low, high)
        pivot_point2 = partition2(low, high)
        quick_sort(low, pivot_point1-1)
        quick_sort(pivot_point1+1, pivot_point2)
        quick_sort(pivot_point2+1, high)


def partition1(low, high):
    pp = s[low]
    j = low
    for i in range(low + 1, high + 1):
        if s[i] < pp:
            j += 1
            s[i], s[j] = s[j], s[i]
    pp = j
    s[low], s[pp] = s[pp], s[low]
    return pp


def partition2(low, high):
    pp = s[high]
    j = low-1
    for i in range(low, high):
        if s[i] < pp:
            j += 1
            s[i], s[j] = s[j], s[i]
    pp = j+1
    s[high], s[pp] = s[pp], s[high]
    return pp


def main():

    global s
    s = [1, 7, 3, 4, 5, 2, 3, 4, 5, 6, 102, 9]
    quick_sort(0, len(s)-1)
    print(s)


if __name__ == '__main__':
    main()
