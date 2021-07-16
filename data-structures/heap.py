# a heap is an array representing a binary tree
# root is min of array for a min heap

# bfs of the "tree" is the order of the array, this allows us to index for parent & children (LEFT - 2(n) + 1, RIGHT - 2(n) + 2)

# Bubble up - happens if invariant is not satisfied when an item is added to the heap. Swap with parents
# Bubble down - happens if invariant is not satisfied when root (min item) is removed and replaced with last element in heap (array)
    # swap with the smallest child - 


class MinHeap:
    def __init__(self, items=None):
        """Initialize this heap and insert the given items, if any."""
        # Initialize an empty list to store the items
        self.items = []
        if items:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this heap."""
        return 'BinaryMinHeap({})'.format(self.items)

    def is_empty(self):
        """Return True if this heap is empty, or False otherwise."""
        return self.items is not None

    def size(self):
        """Return the number of items in this heap."""
        return len(self.items)
    
    def insert(self, item):
        """
        Insert the given item into this heap.

        runtime: O(log n) - swaps need to happen

        """

        # Insert the item at the end
        self.items.append(item)

        # bubble up to the root
        self.bubble_up(self.last_index())
    
    def peek(self):
        """Return the minimum item at the root of this heap.
        Best and worst case running time: O(1) because min item is the root."""

        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        assert self.size() > 0
        return self.items[0]
    
    def delete_min(self):
        """Remove and return the minimum item at the root of this heap.

        Runtime: O(log n)
        """

        if len(self.items) == 0: return "Empty heap"

        if len(self.items) == 1: return self.items.pop()

        min_item = self.items[0]

        last_item = self.items.pop()
        self.items[0] = last_item

        # swaps
        if self.size() > 1:
            self.bubble_down(0)
        
        return min_item
    
    def bubble_up(self, index):
        """Ensure the heap ordering property is true above the given index,
        swapping out of order items, or until the root node is reached.
        
        Best case running time: O(1) if parent item is smaller than this item.
        Worst case running time: O(log n) if items on path up to root node are
        out of order. Maximum path length in complete binary tree is log n."""
        # base case: root index
        if index == 0: return

        child_item = self.items[index]

        parent_index = self.parent_index(index)
        parent_item = self.items[parent_index]

        # all children must be less than parent to satisfy min heap invariant
        if child_item < parent_item:
            # swap in place
            self.items[index], self.items[parent_index] = self.items[parent_index], self.items[index]
            # recurse
            self.bubble_up(parent_index)
    
    def bubble_down(self, parent_index):
        left_child_index = self.left_child_index(parent_index)
        right_child_index = self.right_child_index(parent_index)

        indices = [parent_index, left_child_index, right_child_index]

  
        min_item_index = None
        min_val = float("inf")
        
        for index in indices:
            if index < self.size and self.items[index] < min_val:
                min_val = self.items[index]
                min_item_index = index

        if min_item_index == parent_index:
            return
        
        self.items[min_item_index], self.items[parent_index] = self.items[parent_index], self.items[min_item_index]
        
        self.bubble_down(min_item_index)
            
    def last_index(self):
        """Return the last valid index in the underlying array of items."""
        return len(self.items) - 1

    def parent_index(self, index):
        """Return the parent index of the item at the given index."""
        if index <= 0:
            raise IndexError('Heap index {} has no parent index'.format(index))
        # (n-1) // 2
        return (index-1) // 2

    def left_child_index(self, index):
        """Return the left child index of the item at the given index."""
        # 2(n) + 1
        return (2 * index) + 1

    def right_child_index(self, index):
        """Return the right child index of the item at the given index."""
        # 2(n) + 2
        return (2 * index) + 2



def test_binary_min_heap():
    # Create a binary min heap of 7 items
    items = [9, 25, 86, 3, 29, 5, 55]
    heap = MinHeap()
    print('heap: {}'.format(heap))

    print('\nInserting items:')
    for index, item in enumerate(items):
        heap.insert(item)
        print('insert({})'.format(item))
        print('heap: {}'.format(heap))
        print('size: {}'.format(heap.size()))
        heap_min = heap.peek()
        real_min = min(items[: index + 1])
        correct = heap_min == real_min
        print('peek: {}, correct: {}'.format(heap_min, correct))

    print('\nDeleting items:')
    for item in sorted(items):
        heap_min = heap.delete_min()
        print('delete_min: {}'.format(heap_min))
        print('heap: {}'.format(heap))
        print('size: {}'.format(heap.size()))

if __name__ == '__main__':
    test_binary_min_heap()

def min_index_value(indices, arr):
    """
    return the index with the min value in arr
    """
    min_index = None
    min_val = float("inf")
    
    for index in indices:
        if index < len(arr) and arr[index] < min_val:
            min_val = arr[index]
            min_index = index
    
    return min_index

    # lambda equivalent
    # return min(
    #     (i for i in indices if i < len(arr)),  
    #     key = lambda i: arr[i]
    # )

