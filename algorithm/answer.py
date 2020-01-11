# Question 2
def sum_of_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digit(int(n / 10))


# Question 6 
def checkRecursive(x, n, curr_num=1, curr_sum=0):
    # Initialize number of ways to express 
    # x as n-th powers of different natural 
    # numbers 
    results = 0

    # Calling power of 'i' raised to 'n' 
    p = pow(curr_num, n)
    while (p + curr_sum < x):
        # Recursively check all greater values of i 
        results += checkRecursive(x, n, curr_num + 1, p + curr_sum)
        curr_num = curr_num + 1
        p = pow(curr_num, n)

        # If sum of powers is equal to x
    # then increase the value of result. 
    if (p + curr_sum == x):
        results = results + 1

    # Return the final result 
    return results


# question_4
def printSolution(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")


N = 4


def isSafe(maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False


def solveMaze(maze):
    # Creating a 4 * 4 2-D list 
    sol = [[0 for j in range(4)] for i in range(4)]

    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution doesn't exist")
        return False

    printSolution(sol)
    return True


# A recursive utility function to solve Maze problem 
def solveMazeUtil(maze, x, y, sol):
    # if (x, y is goal) return True 
    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True

    # Check if maze[x][y] is valid 
    if isSafe(maze, x, y) == True:
        # mark x, y as part of solution path 
        sol[x][y] = 1

        # Move forward in x direction 
        if solveMazeUtil(maze, x + 1, y, sol) == True:
            return True

        # If moving in x direction doesn't give solution  
        # then Move down in y direction 
        if solveMazeUtil(maze, x, y + 1, sol) == True:
            return True

        # If none of the above movements work then  
        # BACKTRACK: unmark x, y as part of solution path 
        sol[x][y] = 0
        return False


# question_5
def isReachable(sx, sy, dx, dy):
    # base case 
    if (sx > dx or sy > dy):
        return False

    # current point is equal to destination 
    if (sx == dx and sy == dy):
        return True

    # check for other 2 possibilities 
    return (isReachable(sx + sy, sy, dx, dy) or
            isReachable(sx, sy + sx, dx, dy))


# question_7
# solution 1 use recursive
def steps(source, step, dest):
    # base cases
    if (abs(source) > (dest)):
        return 2 * abs(dest) - 1

    if (source == dest):
        return step

        # at each point we can go either way

    # if we go on positive side 
    pos = steps(source + step + 1,
                step + 1, dest)

    # if we go on negative side 
    neg = steps(source - step - 1,
                step + 1, dest)

    # minimum of both cases 
    return min(pos, neg)


# solution 2 not use recursive (RECOMMENDED)
def reachTarget(target):
    # Handling negatives by symmetry 
    target = abs(target)

    # Keep moving while sum is  
    # smaller or difference is odd. 
    sum = 0
    step = 0
    while (sum < target or (sum - target) %
           2 != 0):
        step = step + 1
        sum = sum + step

    return step
