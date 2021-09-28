"""

Min binary heap implementation :) 

                                   0
                  1                                 2
          3               4                5               6
      7       8       9       10      11      12      13      14
    15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30


"""

# heapify: https://www.youtube.com/watch?v=rBRItn-P6n4


def heapify(heap):
    """In the worst case, you'd have to call bubble up on every node once - O(nlogn).

    But using math (or some simulations), you'll find that it's impossible to have 
    a scenario where you'd need to bubble up on every node.

    If you ran multiple tests of heaping on random inputs you'd find the the runtime 
    is actually O(n)."""

    n = len(heap)
    for i in range(n-1, -1, -1):
        _bubble_up(heap, i)


def heappushpop(heap, val):
    pass


def n_largest(heap, n):
    pass


def n_smallest(heap, n):
    pass


def heappush(heap, val):
    heap.append(val)
    _bubble_up(heap, len(heap)-1)


def heappop(heap):
    if len(heap) > 0:
        min_item = heap[0]

        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop()
        _bubble_down(heap, len(heap)-1)

        return min_item
    else:
        raise ValueError


def heapreplace(heap, val):
    pass


def _bubble_down(heap, parent_index):
    """Ensure ordering below index by swapping out of order vals after pop"""
    if parent_index > len(heap):
        return

    left_index = _left_child_index(heap, parent_index)
    right_index = _right_child_index(heap, parent_index)

    indices = [parent_index, left_index, right_index]

    # find index of smallest child
    min_item = float("inf")
    min_item_index = None
    for index in indices:
        if heap[index] < min_item:
            min_item = heap[index]
            min_item_index = index

    # swap down with smallest child, if item is smaller
    heap[parent_index], heap[min_item_index] = heap[min_item_index], heap[parent_index]
    # recurse down with min child index
    _bubble_down(heap, min_item_index)


def _bubble_up(heap, child_index):
    """Ensure ordering above index by swapping out of order vals after insert
    """

    if child_index == 0:
        return

    parent_index = _parent_index(heap, child_index)

    # swap up if parent is greater than child
    if heap[parent_index] > heap[child_index]:
        heap[parent_index], heap[child_index] = heap[child_index], heap[parent_index]
        # recurse up with parent_index
        _bubble_up(heap, parent_index)


def _left_child_index(heap, parent_index):
    return (2*parent_index)+1


def _right_child_index(heap, parent_index):
    return (2*parent_index)+2


def _parent_index(heap, child_index):
    return (child_index-1) // 2
