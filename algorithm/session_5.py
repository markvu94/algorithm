def first_capital(str):
    if len(str) == 0:
        return "There is no capital letter in this string"
    else:
        if str[0].isupper():
            return str[0]
        else:
            return first_capital(str[1:])


def count_substr(input_str):
    if len(input_str) == 0:
        return 0

    else:
        valid_substring = count_substr(input_str[1:]) + count_substr(input_str[:-1]) - count_substr(input_str[1:-1])
        if input_str[0] == input_str[-1]:
            valid_substring += 1

        return valid_substring


'''
Cho một hình chữ nhật có kích thước N * M. Bạn có số lượng vô hạn các miếng hình vuông có độ dài cạnh là 2 mũ i (với i chạy từ 0,1,2,3......., nói cách khác hình vuông có cạnh 1,2,4,8,16 ....). Câu hỏi đặt ra là cần tối thiểu bao nhiêu hình vuông để lấp đầy hình chữ nhật trên?
Ví dụ: với hình vuông 5*6 thì sẽ cần tối thiểu 9 hình vuông để lấp đầy (6 hình 1*1, 1 hình 4*4 và 2 hình 2*2).
'''


def minTiles(n, m):
    # base case, when area is 0. 
    if n == 0 or m == 0:
        return 0

    # If n and m both are even, calculate tiles for n/2 x m/2 
    # Halfing both dimensions doesn't change the number of tiles 
    elif n % 2 == 0 and m % 2 == 0:
        return minTiles(int(n / 2), int(m / 2))

        # If n is even and m is odd, Use a row of 1x1 tiles
    elif n % 2 == 0 and m % 2 == 1:
        return (n + minTiles(int(n / 2), int(m / 2)))

        # If n is odd and m is even, Use a column of 1x1 tiles
    elif n % 2 == 1 and m % 2 == 0:
        return (m + minTiles(int(n / 2), int(m / 2)))

        # If n and m are odd, add row + column number of tiles
    else:
        return (n + m - 1 + minTiles(int(n / 2), int(m / 2)))


'''
cho 3 dữ liệu đầu vào là số tiền, giá tiền mỗi chiếc kẹo, và số vỏ kẹo có thể đổi để lấy kẹo mới, tìm số kẹo tối đa có thể ăn được
ví dụ: với 16 money, 2 price, 2 wrap thì sẽ ăn dc 8 + 4 + 2 + 1 kẹo
'''


def count_rec(choc, wrap):
    if (choc < wrap):
        return 0

    new_choc = choc // wrap

    return new_choc + count_rec(new_choc + choc %
                                wrap, wrap)


def count_max_choco(money, price, wrap):
    choc = money // price

    return choc + count_rec(choc, wrap)


'''
------------------------------------------------------------------------------
Back Track
'''

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, [row, col]):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and [i, j] != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -  ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return row, col

    return None


print_board(board)
solve(board)
print("_______________________")
print_board(board)
