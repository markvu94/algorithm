# Try Exception
'''
example_1: handle ValueError
'''
'''
loop = True
number = 10
while loop:
    x = input('insert a number: ')
    try:
        n = int(x)
        result = 10/n
        print('result is {}'.format(result))
        loop = False
    except ValueError:
        print('wrong input')
    except ZeroDivisionError:
        print('cannot divide to zero')
'''

# List review
'''
NOTE: index
menu = ['com','canh','thit']
print(menu[0])          -> 'com'
print(menu[-1])         -> 'thit'

NOTE: loop items
for item in menu:
    print (item)

NOTE: loop index
for index in range(len(menu)):
    print (index)

NOTE: loop items and index
for index, item in enumerate(menu):
    print (index,item)

NOTE: update
menu[0] = "pho"
menu[1], menu[2] = menu[2], menu[1]

NOTE: delete
del menu[1]
'''

# prob_1
'''
cho một list đầu vào có 10 số random. ví dụ [4,5,1,8,9,10,5,6,4,3]
a. in ra list mới gồm 3 số đầu tiên --> [4,5,1]
b. in ra list mới gồm 3 số cuối cùng  --> [6,4,3]
c. sắp xếp list này thứ tự tăng dần
d. sắp xếp list này thứ tự giảm dần

from random import randint
input_list = []
for i in range(10):
    input_list.append(randint(1,10))
print(input_list)
'''
from random import randint

input_list = []
for i in range(10):
    input_list.append(randint(1, 10))
print(input_list)

list_a = input_list[-3:]
print(list_a)

# a
'''
list slicing
'''
'''
nums = [5,6,1,3,9]
swapped = True 
while swapped:
    swapped = False
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i],nums[i+1] = nums[i+1], nums[i]
            swapped = True

print(nums)
'''
'''
NOTE: 
nums = [5,1,3,4,2]

for i in range(len(nums)):
    # We assume that the first item of the unsorted segment is the smallest
    lowest_value_index = i
    # This loop iterates over the unsorted items
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[lowest_value_index]:
            lowest_value_index = j
    # Swap values of the lowest unsorted element with the first unsorted
    # element
    nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
'''

# dictionary concept
'''
person = {
   "name": "Duc",
   "age": 21,
   "university": ["FTU",'NEU'],
   "ex": 3,  
}

NOTE: loop by key
for key in person:
    print(key)

NOTE: loop by value
for value in person.values():               
    print(value)

NOTE: loop by items
for key,value in person.items():
    print(key,value)

NOTE: Create or Update
# person["gender"] = "male"
# person["ex"] = 5
# print(person)

NOTE: Delete
# del person["age"]
# print(person)

NOTE: change a key to other key
person['sex'] = person.pop('gender')
print(person)
'''

# dictionary prob
'''
viết chương trình in ra các cặp số có tích bằng 256 trong 1 dãy số ngẫu nhiên cho trước kèm theo vị trí của chúng
Exp:
	[1,3,4,16,32,8,64,4,128,2,256,32]
    [16, 2, 4, 2, 128, 64, 16, 7, 1, 64, 32, 16, 5, 8]
các cặp số có tích bằng 256 là: 
1 và 256 ở vị trí số 1 và 11
…
…
*note: không in kiểu 2x128 và 128x2 > chọn 1
nếu trong list có nhiều cặp giống nhau (VD: 2 cặp 2x128) thì chỉ in 1 cặp
'''

# function intro
'''
prob_1: quadro(a,b,c)
'''
