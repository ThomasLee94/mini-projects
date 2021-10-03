from min_heap import FibHeap
import unittest


class FibHeapTest(unittest.TestCase):
    def test_fib_heap_init(self):
        fib_heap = FibHeap([6, 5, 4, 3, 2, 1, 0])
        print(fib_heap.min_root.val)
        assert fib_heap.peek() == 0

    def test_fib_heappop(self):
        fib_heap = FibHeap([6, 5, 4, 3, 2, 1, 0])
        assert fib_heap.pop() == 0
        assert fib_heap.pop() == 1
        assert fib_heap.pop() == 2
        assert fib_heap.pop() == 3

    def test_fib_heappush(self):
        fib_heap = FibHeap()
        fib_heap.push(0)
        assert fib_heap.peek() == 0
        fib_heap.push(3)
        assert fib_heap.peek == 0
        fib_heap.pop()
        assert fib_heap.peek() == 3
        fib_heap.push(1)
        assert fib_heap.peek() == 1


if __name__ == "__main__":
    unittest.main()
