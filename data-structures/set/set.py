from dictionary import Dictionary


class Set:
    def __init__(self, iterable=None):
        self.items = Dictionary()
        self.size = 0

        if iterable:
            for item in iterable:
                self.add(item)

    def __repr__(self):
        return "{}".format(self.items)

    def __iter__(self):
        for item in self.items.keys():
            yield item

    def __bool__(self):
        return len(self.items) > 0

    def __contains__(self, item):
        return self.items.contains(item)

    def __getitem__(self, item):
        return self.items.get(item)

    def get_items(self):
        return self.items.keys()

    def add(self, item):
        if item not in self.items:
            self.items.insert_or_update(item, True)
            self.size += 1

    def remove(self, item):
        self.items.delete(item)
        self.size -= 1

    def contains(self, item):
        return self.items.contains(item)

    def union(self, set_):
        new_set = Set()

        for item in set_:
            if item not in new_set:
                new_set.add(item)

        for item in self.items.keys():
            if item not in new_set:
                new_set.add(item)

        return new_set

    def intersection(self, set_):
        new_set = Set()

        for item in self.items:
            if item in set_:
                new_set.add(item)

        return new_set

    def difference(self, set_):
        new_set = Set()
        intersections = self.intersection(set_)

        for item in self.items:
            if not intersections.contains(item):
                new_set.add(item)

        return new_set

    def is_subset(self, set_):
        for item in self.items:
            if item not in set_:
                return False

        return True


def test():
    test_add_remove()
    test_union()
    test_intersection()
    test_difference()
    test_is_subset()


def test_add_remove():
    test_set = Set([1, 2, 3, 4])
    assert test_set.contains(1) is True
    assert test_set.contains(4) is True
    assert test_set.contains(6) is False

    test_set.add(6)
    assert test_set.contains(6) is True

    test_set.remove(4)
    assert test_set.contains(4) is False


def test_union():
    test_set1 = Set([1, 2, 3, 4])
    test_set2 = Set([5, 6, 7, 8])
    union = test_set1.union(test_set2)
    print(f"Union test, expecting [1,2,3,4,5,6,7,8], we get: {union.get_items()}")


def test_intersection():
    test_set1 = Set([1, 2, 3, 4, 5])
    test_set2 = Set([4, 5, 6, 7, 8])

    intersection = test_set1.intersection(test_set2)
    print(f"Intersection test, expecting [4,5], we get: {intersection.get_items()}")


def test_difference():
    test_set1 = Set([1, 2, 3, 4, 5])
    test_set2 = Set([4, 5, 6, 7, 8])

    diff1 = test_set1.difference(test_set2)
    diff2 = test_set2.difference(test_set1)
    print(f"Difference test, expecting [1,2,3], we get {diff1.get_items()}")
    print(f"Difference test, expecting [6,7,8], we get {diff2.get_items()}")


def test_is_subset():
    test_set1 = Set([1, 4, 5])
    assert test_set1.is_subset(Set([1, 2, 3, 4, 5])) is True
    assert test_set1.is_subset(Set([1, 2, 4, 6])) is False


test()
