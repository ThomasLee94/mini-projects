from deque import Deque


def test_deque_init():
    deque = Deque([1, 2, 3, 4, 5])
    assert len(deque) == 5

    # assert deque.head.val == 1
    # assert deque.head.prev is None
    # assert deque.head.next.val == 2

    # assert deque.tail.val == 5
    # assert deque.tail.next is None
    # assert deque.tail.prev.val == 4


if __name__ == '__main__':
    test_deque_init()
