from binary_min_heap import heapify, heappush, heappop

"""
                0
        1               2
      3   4           5   6

"""


def test_heap_array():
    test_array_heapify()
    test_array_heappop()
    test_array_heappush()


def test_heap_tree():
    pass


def test_array_heapify():
    array = [6, 5, 4, 3, 2, 1, 0]
    heapify(array)
    assert array[0] == 0


def test_array_heappop():
    array = [0, 5, 4, 3, 2, 1, 6]
    heapify(array)

    assert heappop(array) == 0
    assert heappop(array) == 1
    assert heappop(array) == 2
    assert heappop(array) == 3
    assert heappop(array) == 4
    assert heappop(array) == 5
    assert heappop(array) == 6
    assert heappop(array) is ValueError


def test_array_heappush():
    array = [5, 6, 0, 1, 2, 3, 4]
    heapify(array)

    heappush(array, 7)
    assert array[0] == 0


if __name__ == "__main__":
    test_heap_array()
    # test_heap_tree()
