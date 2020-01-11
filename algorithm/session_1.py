'''
cho người dùng nghĩ 1 số trong đầu vào 1 số từ 1-100
máy tính sẽ đưa ra một câu hỏi:
- cái số x này có đúng không? (1-100)
    - c: correct
    - l: larger
    - s: smaller
'''

# from random import randint
# x = randint(1,100)

# while loop
'''
* 3 cách dùng vòng lặp while:
- Cach 1:
count = 0
while True:
    print("hi")
    count +=1
    if count == 3:
        break
        print("done")     NOTE: không chạy được câu lệnh sau break

- Cach 2:
count = 0
loop = True
while loop:
    print ("Hi")
    count +=1
    if count == 3:
        loop = False
        print("done")   NOTE: vẫn chạy được câu lệnh print ở đây

- Cach 3:
count = 0
while count <3:
    print("hi")
    count +=1

'''

# basic operation
'''
x = 100
floor_division = 100//7
print(floor_division)
modulus = 100 % 7
print(modulus)
'''
'''
low = 1
high = 100
loop = True 

while loop:
    mid = (low + high) // 2
    answer = input('so {} co dung khong '.format(mid))
    if answer == 'c':
        print('dap an la {}'.format(mid))
        loop = False
    elif answer == 'l':
        low = mid
    elif answer == 's':
        high = mid
'''

# math_2
'''
number = int(input('nhap 1 so: '))

for i in range(2,number+1,2):
    print(i)

'''

# math_3
'''
number = int(input('nhap 1 so: '))
# if number % 2 == 0:
#     for i in range(number,0,-2):
#         print(i)
# else:
#     for i in range(number - 1, 0, -2):
#         print(i)

number -= number % 2          # number = number - number % 2
for i in range(number, 0, -2 ):
    print(i)
'''
from math import sqrt

number = int(input('nhap 1 so: '))
count = 0
if number == 1:
    print('day k phai snt')
else:
    for i in range(2, number):
        if number % i == 0:
            count += 1

    if count == 0:
        print('day la so nt')
    elif count >= 1:
        print('day k phai snt')
