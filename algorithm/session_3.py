# Function introduction


def get_sum(number_1, number_2):
    sum_number = number_1 + number_2
    return sum_number


'''
NOTE: Exercise
1. viết function để tính nghiệm của phương trình bậc 2
    - Yêu cầu viết theo 2 hàm số sau:

def get_delta(a, b, c):
    --do something here--
    return delta

def quadro(a, b, c):
    --do something here--
    return root_1, root_2 

2. viết function để tính hệ số góc a,b từ đầu vào 2 điểm trên đồ thị
    - Yêu cầu viết theo hàm số sau:

def get_f(point_1=[], point_2=[]):
    --do something here--
    return a,b

3. viết function để tính khoảng cách từ một điểm tới một đường thẳng
    - Yêu cầu viết theo hàm số sau:

def get_distance(point = [], a, b, c):
    --do something here--
    return distance
'''
from math import sqrt


def delta(a, b, c):
    delta = pow(b, 2) - 4 * a * c
    return delta


def quadro(a, b, c):
    root_1 = (-b + sqrt(delta(a, b, c))) / (2 * a)
    root_2 = (-b - sqrt(delta(a, b, c))) / (2 * a)
    return root_1, root_2


def get_f(point_1=[], point_2=[]):
    delta_y = point_1[1] - point_2[1]
    delta_x = point_1[0] - point_2[0]
    if delta_x == 0:
        return 'đây là đường thẳng vuông góc với trục hoành'
    else:
        a = delta_y / delta_x
        b = point_1[1] - a * point_1[0]
        return a, b


def hanoi_tower_recursion(n):
    '''algorithm to resolve hanoi_tower problem
      - n: number of disk
      - result: count number of disk movement to solve the problem'''
    if n == 1:
        result = 1
    else:
        result = 2 * (hanoi_tower_recursion(n - 1)) + 1
    return result


def hanoi_tower_pow(n):
    result = pow(2, n) - 1
    return result


def find_minimum(l):
    '''algorithm to find the minimum number of list n'''
    if len(l) == 0:
        return 'Cannot find the minimum of an empty list.'
    elif len(l) == 1:
        return l[0]
    else:
        min_number = find_minimum(l[1:])
        min_result = l[0]
        if min_number < min_result:
            min_result = min_number
        return min_result


def factorial(n):
    '''algorithm to find factorial of a number n'''
    if n == 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result


def sum_first_numbers(n):
    '''algorithm to sum first n number'''
    if n == 0:
        return 0
    else:
        return n + sum_first_numbers(n - 1)


def fibonaci(n):
    '''fibonaci: 0,1,1,2,3,5,8 ...'''
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonaci(n - 1) + fibonaci(n - 2)
    return result


def greatest_division(a, b):
    '''algorithm to find the greates division of two number a and b
    NOTE: có thể để sang buổi 2 dạy cùng merge sort'''
    if a == b:
        result = a
    elif a > b:
        result = greatest_division(b, a - b)
    else:
        result = greatest_division(a, b - a)
    return result


def pascal_triangle(n):
    '''algorithm to represent the line number n of a pascal triangle
    NOTE: có thể để sang buổi 2 hoặc 3 dạy cùng quick sort'''
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal_triangle(n - 1)
        for i in range(len(previous_line) - 1):
            line.append(previous_line[i] + previous_line[i + 1])
        line += [1]
    return line
