class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.head = None

class DoublyLinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0

        if iterable:
            for item in iterable:
                self.append_right(item)
    

    def is_empty(self):
        return self.head is None
    
    def items(self):
        items = []

        if self.head is None: return items

        node = self.head

        while node is not None:
            items.append(node.val)
            node = node.next 
        
        return items

    def append(self, val):
        node = DoublyNode(val)

        if self.is_empty():
            self.head = node
        
        else:
            node.prev = self.tail
            self.tail.next = node
        
        self.tail = node
        self.size += 1

    def prepend(self, val):
        node = DoublyNode(val)

        if self.is_empty():
            self.head = node

        else:
            node.next = self.head
            self.head.prev = node
        
        self.head = node
        self.size += 1

    def pop_left(self):
        val = self.head.val

        next_ = self.head.next
        self.head.next = None
        next_.prev = None
        self.head = next_

        return val

    def pop_right(self):
        val = self.tail.prev

        prev = self.tail.prev
        prev.next = None
        self.tail.prev = None
        self.tail = prev

        return val


def test_linked_list():
    ll = DoublyLinkedList([1,2,3,4,5])
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()

