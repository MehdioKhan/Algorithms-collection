from math import pow


def normal_mult(a, b, n):
    result = []
    for i in range(n):
        t = []
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += a[i][k]*b[k][j]
            t.append(sum)
        result.append(t)
    return result


def print_matrix(mat, n):
    """
    print matrix
    """
    for i in range(n):
        for j in range(n):
            print('{}   '.format(mat[i][j]), end='')
        print()


def add(a, b, n):
    """
    Adds two squar matrices with size n*n
    """
    # if type(a) == list and type(a) == type(b) and len(a) == len(b):
    result = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(a[i][j]+b[i][j])
        result.append(temp)
    return result
    # else:
    # return None


def neg(mat, n):
    result = []
    for i in range(n):
        t = []
        for j in range(n):
            t.append(-mat[i][j])
        result.append(t)
    return result


def power_of_2(n):
    """
    :param n: input number
    :return: smallest power of 2 greater than n
    """
    if n > 0:
        i = 0
        while True:
            if pow(2, i) >= n:
                return int(pow(2, i))
            else:
                i += 1


def common_size(m1, n1, m2, n2):
    return max(power_of_2(max(m1, n1)), power_of_2(max(m2, n2)))


def max(a, b):
    if a > b:
        return a
    else:
        return b


def extend(mat, m, n, p):
    """
    Extends matrix size to reach size=2^k
    """
    result = []
    for i in range(p):
        t = []
        for j in range(p):
            if i < m and j < n:
                t.append(mat[i][j])
            else:
                t.append(0)
        result.append(t)
    return result


def divide(mat, n):
    """
    Divides matrix to 4 equal peaces
    """
    if type(mat) == list:
        result = []
        if n >= 2:
            m = n//2
            a11 = []
            a12 = []
            a21 = []
            a22 = []
            for i in range(n):
                t11 = []
                t12 = []
                t21 = []
                t22 = []
                for j in range(n):
                    if i < m:
                        if j < m:
                            t11.append(mat[i][j])
                        else:
                            t12.append(mat[i][j])
                    else:
                        if j < m:
                            t21.append(mat[i][j])
                        else:
                            t22.append(mat[i][j])
                if len(t11) != 0:
                    a11.append(t11)
                if len(t12) != 0:
                    a12.append(t12)
                if len(t21) != 0:
                    a21.append(t21)
                if len(t22) != 0:
                    a22.append(t22)
            return a11, a12, a21, a22
        else:
            return mat, mat, mat, mat


def h_merge(c1, c2, n):
    """
    stick two matrixes together horizontally
    """
    result = []
    for i in range(n):
        result.append(c1[i]+c2[i])
    return result


def v_merge(c1, c2, n):
    """
    stick two matrixes together vertically
    """
    result = []
    for i in range(n):
        result.append(c1[i])
    for i in range(n):
        result.append(c2[i])
    return result


def merge(c, n):
    m1 = h_merge(c[0], c[1], n)
    m2 = h_merge(c[2], c[3], n)
    return v_merge(m1, m2, n)


def mult(mat_a, mat_b, n):
    if n == 1:
        c = []
        t = []
        t.append(mat_a[0][0]*mat_b[0][0])
        c.append(t)
        return c
    else:
        c = []
        div_a = divide(mat_a, n)
        div_b = divide(mat_b, n)
        m = n//2
        M1 = mult(add(div_a[0], div_a[3], m), add(div_b[0], div_b[3], m), m)
        M2 = mult(add(div_a[2], div_a[3], m), div_b[0], m)
        M3 = mult(div_a[0], add(div_b[1], neg(div_b[3], m), m), m)
        M4 = mult(div_a[3], add(div_b[2], neg(div_b[0], m), m), m)
        M5 = mult(add(div_a[0], div_a[1], m), div_b[3], m)
        M6 = mult(add(div_a[2], neg(div_a[0], m), m),
                  add(div_b[0], div_b[1], m), m)
        M7 = mult(add(div_a[1], neg(div_a[3], m), m),
                  add(div_b[2], div_b[3], m), m)
        if M1 is not None and M2 is not None and M3 is not None \
                and M4 is not None and M5 is not None and \
                M6 is not None and M7 is not None:
            c.append(add(add(add(M1, M4, m), neg(M5, m), m), M7, m))
            c.append(add(M3, M5, m))
            c.append(add(M2, M4, m))
            c.append(add(add(add(M1, M3, m), neg(M2, m), m), M6, m))
        return merge(c, m)


def main():
    a = [
        [1, 1],
        [2, 2],
        [3, 3],
    ]
    b = [
        [3, 3],
        [4, 4]
    ]

    c = common_size(3, 2, 1, 2)
    print_matrix(mult(extend(a, 3, 2, c), extend(b, 2, 2, c), 4), c)


if __name__ == '__main__':
    main()
