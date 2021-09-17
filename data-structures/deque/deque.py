from doubly_linked_list import DoublyLinkedList


class Deque(DoublyLinkedList):
    def __init__(self, iterable=None):
        super().__init__(iterable)

    def __len__(self):
        return self.size

    def __str__(self):
        items = self.items()
        s = ""

        for i in range(len(items)):
            print("i: ", i)
            if i == 0:
                s += f'HEAD {items[i]} <--> '
            elif i == len(items)-1:
                s += f'{items[i]} TAIL'
            else:
                s += f'{items[i]} <--> '

        return s

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node.val
            node = node.next

    def __getitem__(self, index):
        node = self.head
        counter = 0

        while counter < index:
            node = node.next
            counter += 1

        return node.val

    def append(self, val):
        self.append(val)

    def prepend(self, val):
        self.prepend(val)

    def pop(self):
        node = self.remove(self.tail)

        return node.val

    def popleft(self):
        node = self.remove(self.head)

        return node.val

    def extend(self, iterable):
        for val in iterable:
            self.append(val)

    def extendleft(self, iterable):
        for val in iterable:
            self.prepend(val)
