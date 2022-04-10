import math

#винзолирование
def vinz(array):
    for i in range(len(array)): recover(i, array)
    return array

#восстановление числа по индексу
def recover(index, array):
    dop_index = 0
    while array[index] == None:
        if index - dop_index > 0 and array[index - dop_index] != None: array[index] = array[index - dop_index]
        if index + dop_index < len(array) and array[index + dop_index] != None:  array[index] = array[index + dop_index]
        dop_index += 1

#корреляция
def correlation(list_1, list_2):
    average_one = sum(list_1) / len(list_1)
    average_two = sum(list_2) / len(list_2)
    disp_1 = 0
    disp_2 = 0
    disp_3 = 0

    for i in range(len(list_1)):
        disp_1 += math.pow(list_1[i] - average_one, 2)
        disp_2 += math.pow(list_2[i] - average_two, 2)
        disp_3 += (list_2[i] - average_two) * (list_1[i] - average_one)

    return disp_3 / (math.sqrt(disp_1 * disp_2))

#сглаживание динамическим окном
def smoothing(array, k):
    res = []
    for i in range(len(array)): res.append(smoothing_for_element(array[:i + 1], k))
    return res

#сглаживание для 1 элемента
def smoothing_for_element(window, k):
    while math.fabs(window[-1] - (sum(window) / len(window))) / window[-1] > k: window.pop(0)
    return sum(window) / len(window)

#сглаживание методом скользящего среднего
def  smoothing_average(array, window):
    res = []
    for i in range(len(array)):
        j = 0
        while ((i - j > -1) and
              (i + j < len(array)) and
              (2 * j < window)): j += 1
        res.append(sum(array[i - j + 1: i + j]) / (2 * j - 1))
    return res

#линейная аппроксимация
def approximation(list):
    print(len(list))
    for i in range(len(list)):
        if list[i] == None:
            approximation_for_element(list, i)
    return list

def approximation_for_element(list, index):
    if middle_search(list, index): return
    if left_search(list, index): return
    if right_search(list, index): return

def middle_search(list, index):
    j = 1
    left_point = None
    right_point = None
    while ((left_point == None or right_point == None) and
          (index - j >= 0 and index + j < len(list))):

        if list[index - j] != None and index - j >= 0 and left_point == None:
           left_point = [list[index - j], index - j]

        if list[index + j] != None and index + j < len(list) and right_point == None:
           right_point = [list[index + j], index + j]

        j += 1

    if left_point != None and right_point != None:
        k = (right_point[0] - left_point[0]) / (right_point[1] - left_point[1])
        b = right_point[0] - k * right_point[1]
        for i in range(left_point[1], right_point[1] + 1):
            list[i] = i * k + b
        return True
    else: return False

def right_search(list, index):
    j = 1
    points = []
    while j + index < len(list) and len(points) < 2:
        if list[j + index] != None:
            points.append([list[j + index], j + index])
        j += 1
    if len(points) < 2: return False
    else:
        k = (points[0][0] - points[1][0]) / (points[0][1] - points[1][1])
        b = points[0][0] - points[0][1] * k
        for i in range(index, points[1][1] + 1):
            list[i] = i * k + b
        return True

def left_search(list, index):
    j = 1
    points = []
    while index - j >= 0 and len(points) < 2:
        if list[index - j] != None:
            points.append([list[index - j], index - j])
        j += 1
    if len(points) < 2: return False
    else:
        points = points[::-1]
        k = (points[0][0] - points[1][0]) / (points[0][1] - points[1][1])
        b = points[0][0] - points[0][1] * k
        for i in range(points[1][1], index + 1):
            list[i] = i * k + b
        return True
        




