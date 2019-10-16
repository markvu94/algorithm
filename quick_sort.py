def quick_sort(array=[]):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) <= 1:
        return array

    else:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        
        return quick_sort(less) + equal + quick_sort(greater)  
   
    

print(quick_sort([12,4,5,6,5,3,1,15]))