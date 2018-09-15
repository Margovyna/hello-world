"""
Яша плавал в бассейне размером N × M метров и устал.
В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков (не обязательно от ближайшего)
и y метров от одного из коротких бортиков.
Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик?
Программа получает на вход числа N, M, x, y.
Программа должна вывести число метров, которое нужно проплыть Яше до бортика.
"""


def yasha(N, M, x, y):
    # array (list) deconstruction.
    # the same as doing something like
    #sortedArray = sorted([N, M])
    #shortSide = sortedArray[0]
    #longSide = sortedArray[1]
    [shortSide, longSide] = sorted([N, M])
    if y > shortSide or x > longSide:
        print('Яша десь поза басейном о_О')
        return
    if closest_distance_to_side(shortSide, y) < closest_distance_to_side(longSide, x):
        print(closest_distance_to_side(shortSide, y))
    else:
        print(closest_distance_to_side(longSide, x))


def closest_distance_to_side(length, coordinate):
  # figuring out if the given coordinate/distance from the side is the closer distance
    if length - coordinate < coordinate:
        return length - coordinate
    return coordinate


yasha(20, 30, 3, 5)  # should print 3
yasha(20, 30, 15, 10)  # should print 10
yasha(20, 30, 15, 5)  # should print 5
yasha(20, 30, 40, 5)  # should show error

yasha(25, 20, 19, 10)  # should print 6 as 25-19 is 6
