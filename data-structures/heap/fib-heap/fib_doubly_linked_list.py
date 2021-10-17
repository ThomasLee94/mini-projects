class FibNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

        self.parent = None
        self.children = {}
        self.loser = False
        self.degree = 0

    def add_child(self, child_node):
        if child_node.val not in self.children:
            self.children[child_node.val] = child_node
            child_node.parent = self
            self.degree += 1

    def __eq__(self, node):
        if isinstance(node, FibNode):
            return self.val == node.val and id(self) == id(node)


class DoublyLinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0

        if iterable:
            for item in iterable:
                self.append(item)

    def __len__(self):
        count = 0

        if self.head is not None:
            node = self.head

            while node is not None:
                count += 1
                node = node.next

        return count

    def is_empty(self):
        return self.head is None

    def items(self):
        items = []

        if self.head is None:
            return items

        node = self.head

        while node is not None:
            items.append(node.val)
            node = node.next

        return items

    def append(self, val):
        node = FibNode(val)

        if self.is_empty():
            self.head = node

        else:
            node.prev = self.tail
            self.tail.next = node

        self.tail = node
        self.size += 1

    def prepend(self, val):
        node = FibNode(val)

        if self.is_empty():
            self.head = node

        else:
            node.next = self.head
            self.head.prev = node

        self.head = node
        self.size += 1

    def remove(self, node):
        if node is self.head:
            self.head = node.next
            node.next.prev = None
            node.next = None
        elif node is self.tail:
            self.tail = node.prev
            node.prev.next = None
            node.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next, node.prev = None, None

        self.size -= 1
        return node
