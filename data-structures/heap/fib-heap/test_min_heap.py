from min_heap import FibHeap
from fib_doubly_linked_list import FibNode
import unittest


class FibHeapTest(unittest.TestCase):
    def test_node_init(self):
        node1 = FibNode(1)
        node2 = FibNode(2)

        assert node1 != node2
        assert node1 == node1

    def test_fib_heap_init(self):
        fib_heap = FibHeap([6, 5, 4, 3, 2, 1, 0])
        assert fib_heap.peek() == 0

    def test_fib_heappop(self):
        fib_heap = FibHeap([6, 5, 4, 3, 2, 1, 0])
        print(fib_heap.roots)
        assert fib_heap.pop() == 0
        assert fib_heap.pop() == 1
        assert fib_heap.pop() == 2
        assert fib_heap.pop() == 3
        assert fib_heap.pop() == 4
        assert fib_heap.pop() == 5
        assert fib_heap.pop() == 6
        assert fib_heap.pop() is AssertionError

    def test_fib_heappush(self):
        fib_heap = FibHeap()
        fib_heap.push(0)
        assert fib_heap.peek() == 0
        fib_heap.push(3)
        assert fib_heap.peek() == 0
        fib_heap.pop()
        assert fib_heap.peek() == 3
        fib_heap.push(1)
        assert fib_heap.peek() == 1


if __name__ == "__main__":
    unittest.main()
