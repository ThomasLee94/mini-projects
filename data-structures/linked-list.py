class Node(object):
    def __init__(self, val):
        """Initialize this node with the given val."""
        self.val = val
        self.next = None

class LinkedList(object):
    def __init__(self, iterable=None):
        self.head = None  
        self.tail = None 
        self.size = 0  

        if iterable is not None:
            for item in iterable:
                self.append(item)

    def items(self):
        result = []  
        node = self.head  
       
        while node is not None:  
            result.append(node.val)  
            node = node.next  
        
        return result  

    def is_empty(self):
        return self.head is None

    def length(self):
        return self.size
    
    def find(self, quality):
        node = self.head

        while node is not None:
            if quality(node.val):
                return node.val
            node = node.next
        
        return None

    def append(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.size += 1

    def delete(self, item):
        node = self.head
        previous = None
        found = False

        while not found and node is not None:
            if node.val == item:
                found = True
            else:
                previous = node
                node = node.next

        if found:
            if node is not self.head and node is not self.tail:
                previous.next = node.next
                node.next = None
            if node is self.head:
                self.head = node.next
                node.next = None
            if node is self.tail:
                if previous is not None:
                    previous.next = None
                self.tail = previous
            self.size -= 1
            
if __name__ =="__main__":
    ll = LinkedList([1,2,3])
    assert ll.size == 3
    assert ll.head.val == 1
    assert ll.tail.val == 3
    assert ll.items() == [1,2,3]

    ll.delete(1)
    assert ll.size == 2
    assert ll.items() == [2, 3]
    assert ll.head.val == 2
    assert ll.tail.val == 3
                