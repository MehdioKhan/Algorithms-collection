import math
import pprint


def check(data):
    """
    Check if loaded data is true
    """

    for i in range(len(data)):
        for j in range(len(data[i])):
            if i > j:
                data[j][i] = data[j][i]


def csv2array():
    """
    Reads data from a csv file and convert it to 2D array
    """
    SEPERATOR = ','
    d = open('data.csv', 'r')
    lines = []
    for line in d.readlines():
        line = line.replace('\n', '')
        temp = line[line.index(',')+1:]
        lines.append(temp.split(SEPERATOR))
    d.close()
    lines = lines[1:]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i != j:
                if lines[i][j] == '0':
                    lines[i][j] = math.inf
                else:
                    lines[i][j] = int(lines[i][j])
            else:
                lines[i][j] = int(lines[i][j])
    check(lines)
    return lines


def city_name_extractor():
    """
    Extract cities and give them number
    """
    SEPERATOR = ','
    d = open('data.csv', 'r')
    city_dict = {}
    city_list = d.readline().replace('\n', '').split(SEPERATOR)[1:]
    i = 1
    for t in city_list:
        city_dict[i] = t
        i += 1
    d.close()
    return city_dict


def dijkstra(n, w, src):
    """
    Dijkstra main algorithm
    """
    flag = [False for i in range(n)]
    i = j = vnear = temp = 0
    touch = []
    length = []
    flag[src] = True
    for i in range(0, n):
        touch.append(src)
        length.append(w[src][i])
    for k in range(0, n):
        mini = math.inf
        for i in range(0, n):
            if(length[i] < mini and not flag[i]):
                vnear = i
                mini = length[i]
        for i in range(0, n):
            temp = length[vnear]+w[vnear][i]
            if temp < length[i] and not flag[i]:
                length[i] = temp
                touch[i] = vnear
        flag[vnear] = True

    return touch, length


def path(src, dest, touch):
    """
    print internal path from source to dest
    """
    k = touch[dest]
    if k != src:
        path(src, k, touch)
        print('{}-->'.format(cities[k+1]), end='')


def printpath(src, dest, touch, length):
    """
    Print complete path from source to dest
    """
    if length[dest] == math.inf:
        print("There is no route from {} to {}".format(
            cities[src + 1], cities[dest + 1]))
    else:
        print('{}-->'.format(cities[src+1]), end='')
        path(src, dest, touch)
        print('{}'.format(cities[dest+1]))
        print('Shortest path length is {}'.format(length[dest]))


def header():
    print("************************************************************")
    print("Dijkstra algorithm implementation on cities of Kerman, Yazd,\n"
          "Fars, Sistan and Baluchestan, Hormozghan and South Khorasan\n"
          "which has a population above 25000.\n")
    print("************************************************************")
    print("Use following city codes to determine distance between source other cities:\n")
    indent = 20
    for i in range(1, len(cities) // 2+1):
        j = i + len(cities) // 2
        s = ''
        if i < 10:
            s = ' '
        temp = str(i) + s + ' : ' + cities[i]
        for k in range(indent - len(cities[i])):
            temp += ' '
        temp += str(j) + ' : ' + cities[j]
        print(temp)
    source = int(input("Please enter source city code : "))
    print()
    return source


def main():
    global cities
    cities = city_name_extractor()
    data = csv2array()
    # g = [
    #     [0, 7, 4, 6, 1],
    #     [inf, 0, inf, inf, inf],
    #     [inf, 2, 0, 5, inf],
    #     [inf, 3, inf, 0, inf],
    #     [inf, inf, inf, 1, 0]
    # ]
    n = len(data)
    src = header()-1

    touch, lenght = dijkstra(n, data, src)
    for i in range(1, n):
        if src != i:
            printpath(src, i, touch, lenght)
            print()


if __name__ == '__main__':
    main()
