# initial_queue class
class Queue:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return (self.items == [])

    def enqueue(self, item):
        if not self.is_full():
            self.items.insert(0, item)
        else:
            drop_item = item
            return drop_item

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def size(self):
        return len(self.items)

    def is_full(self):
        return self.size() == self.capacity


# queue = Queue(10)
# print(queue)

# for i in range(14):
#     queue.enqueue(i)

# print(queue)
# queue.dequeue()
# print(queue)

''' queue class using node linked_list'''


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return '{}'.format(self.cargo)


class NodeQueue:
    def __init__(self, capacity):
        self.length = 0
        self.head = None
        self.capacity = capacity

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.capacity

    def insert(self, cargo):
        node = Node(cargo)
        if not self.is_full():
            if self.head is None:
                # If list is empty the new node goes first
                self.head = node
            else:
                # Find the last node in the queue
                last = self.head
                while last.next:
                    last = last.next

                # Append the new node
                last.next = node
                # Change the length of queue
            self.length += 1

        else:
            drop_item = node
            return drop_item

    def remove(self):
        if not self.is_empty():
            cargo = self.head.cargo
            self.head = self.head.next
            self.length -= 1
            return cargo
        else:
            return None

# node_queue = NodeQueue(2)
# node_queue.insert('cargo_1')
# node_queue.insert('cargo_2')
# node_queue.insert('cargo_3')
# print(node_queue.head)
# node_queue.insert('cargo_4')
# node_queue.remove()
# print(node_queue.head)
