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

    def pop(self):
        return self.remove(self.tail)

    def popleft(self):
        return self.remove(self.head)

    def extend(self, iterable):
        for val in iterable:
            self.append(val)

    def extendleft(self, iterable):
        for val in iterable:
            self.prepend(val)
