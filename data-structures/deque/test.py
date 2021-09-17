from deque import Deque


def test_deque_init():
    deque = Deque([1, 2, 3, 4, 5])
    assert len(deque) == 5

    assert deque.head.val == 1
    assert deque.head.prev is None
    assert deque.head.next.val == 2

    assert deque.tail.val == 5
    assert deque.tail.next is None
    assert deque.tail.prev.val == 4


def test_index():
    deque = Deque([1, 2, 3, 4, 5])
    assert deque[1] == 2


def test_iter():
    deque = Deque([1, 2, 3, 4, 5])
    counter = 1

    for val in deque:
        assert val == counter
        counter += 1


def test_pop():
    deque = Deque([1, 2, 3, 4, 5])

    popped_1 = deque.popleft()
    assert popped_1.val == 1
    assert deque.head.val == 2

    popped_2 = deque.pop()
    assert popped_2.val == 5
    assert deque.tail.val == 4


def test_append():
    deque = Deque([1, 2, 3, 4, 5])

    deque.append(6)
    assert deque.tail.val == 6
    assert len(deque) == 6

    deque.prepend(0)
    assert deque.head.val == 0
    assert len(deque) == 7


def test_extend():
    deque = Deque([1, 2, 3, 4, 5])

    deque.extend([6, 7, 8])
    assert deque.tail.val == 8
    assert len(deque) == 8

    deque.extendleft([0, -1, -2])
    assert deque.head.val == -2
    assert len(deque) == 11


if __name__ == '__main__':
    test_deque_init()
    test_pop()
    test_append()
    test_extend()
    test_index()
    test_iter()
