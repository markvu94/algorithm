def hanoi_tower_recursion(n):
    '''algorithm to resolve hanoi_tower problem
      - n: number of disk
      - result: count number of disk movement to solve the problem'''
    if n == 1:
        result = 1
    else:
        result = 2*(hanoi_tower_recursion(n-1)) + 1
    return result

def hanoi_tower_pow(n):
    '''khi dạy phần này cần chứng minh kết quả = 2^n - 1 bằng pp quy nạp'''
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
        result = n * factorial(n-1)
    return result

def sum_first_numbers(n):
    '''algorithm to sum first n number'''
    if n == 0:
        return 0
    else:
        return n + sum_first_numbers(n-1)

def fibonaci(n):
    '''fibonaci: 0,1,1,2,3,5,8 ...'''
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonaci(n-1) + fibonaci(n-2)
    return result


def greatest_division(a,b):
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
        previous_line = pascal_triangle(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line




