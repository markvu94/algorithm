class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return (self.items == [])

    def size(self):
        return len(self.items)


class StringProcessor(Stack):
    def reverse(self, string_sample):
        for i in range(len(string_sample)):
            self.push(string_sample[i])

        reversed_string = ''

        for i in range(len(string_sample)):
            reversed_string += self.pop()

        return reversed_string

    def get_binary_number(self, number):
        loop = True
        binary_string = ''
        while loop:
            modulus = number % 2
            self.push(modulus)
            number = number // 2
            if number == 0:
                loop = False

        for _ in range(self.size()):
            binary_string += str(self.pop())

        binary_number = int(binary_string)
        return binary_number

    def is_balanced(self, expression_string):
        open_list = ['{', '(', '[']
        close_list = ['}', ')', ']']

        for i in expression_string:
            if i in open_list:
                self.push(i)
            elif i in close_list:
                pos = close_list.index(i)
                if not self.is_empty() and self.items[-1] == open_list[pos]:
                    self.pop()
                else:
                    return False
            else:
                pass

        if self.size() == 0:
            return True
        else:
            return False


''' stack class using node linked_list'''


class Node:
    def __init__(self, cargo=None, last=None):
        self.cargo = cargo
        self.last = last

    def __str__(self):
        return '{}'.format(self.cargo)


class NodeStack:
    def __init__(self):
        self.length = 0
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):

        if self.last is None:
            node = Node(cargo)

        else:
            node = Node(cargo=cargo, last=self.last)

        self.last = node
        # Change the length of stack   
        self.length += 1

    def remove(self):
        if not self.is_empty():
            cargo = self.last.cargo
            self.last = self.last.last
            self.length -= 1
            return cargo
        else:
            return None


node_stack = NodeStack()
node_stack.insert('cargo_1')
node_stack.insert('cargo_2')
node_stack.insert('cargo_3')
print(node_stack.last)
node_stack.remove()
print(node_stack.last)
node_stack.remove()
print(node_stack.last)
