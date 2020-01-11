def factorial(n):
    '''algorithm to find factorial of a number n
    example: factorial(3) = 3! = 1 * 2 * 3 = 6
    '''
    if n == 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result


def fibonaci(n):
    '''fibonaci: 0,1,1,2,3,5,8 ...
    Hàm trả về số vị trí n trong dãy Fibonaci bên trên
    '''
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonaci(n - 1) + fibonaci(n - 2)
    return result


def pascal_triangle(n):
    '''algorithm to represent the line number n of a pascal triangle
    hình dạng tam giác pascal
                    1                       n = 1
                1       1                   n = 2
            1       2       1               n = 3   
        1       3       3       1           n = 4
    1       4       6       4       1       n = 5
    '''
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal_triangle(n - 1)
        for i in range(len(previous_line) - 1):
            line.append(previous_line[i] + previous_line[i + 1])
        line += [1]
    return line


def greatest_division(a, b):
    '''algorithm to find the greates division of two number a and b
    '''
    if a == b:
        result = a
    elif a > b:
        result = greatest_division(b, a - b)
    else:
        result = greatest_division(a, b - a)
    return result


# Merge Sort

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = 0
    right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list, add the elements
        # from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # If the list is a single element, return it
    if len(nums) <= 1:
        return nums

    # Use floor division to get midpoint, indices must be integers
    mid = len(nums) // 2

    # Sort and merge each half
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)


# Quick Sort
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)
