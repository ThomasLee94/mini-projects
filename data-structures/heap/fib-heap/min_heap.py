"""
Lazy but smarter way of "cleaning" up our heap. Heap consolidation only
happens after a heappop. Heapreplace will be implemented by splicing the
heap tree and re-inserting to the end of the vector.

The general consensus seems to be that fib heaps are not meant to be used in
practice and is theoretically only worth it if the priority queue is long - (Page 96):
https://www.cl.cam.ac.uk/teaching/1617/Algorithms/2017-stajano-algs-students-handout.pdf

However, the aggregate runtime of all operations of a fib heap that have
constant* operations for heapify, insert, peek, heappreplace due to the
smarter "cleanup" process (unlike binary heaps where cleanup happens with
every insertion & deletion) increases the performance -
(https://gabormakrai.wordpress.com/2015/02/11/experimenting-with-dijkstras-algorithm/)

This is to say that the fib heap is a smarter implementation for clever
amoratised algorithm design. It pays to let mess build up.

Shallow & wide trees are an issue.

[      root1      ]
child_1  child_2  child_3  child_4  child_5
            |       |
        child_6  child_7

Degree or rank is the same as "number of children" in formal
literature on fibonacci heaps/priority queues.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.degrees = len(self.children)

    def add_child(self, val):
        if val not in self.children:
            self.children[val] = Node(val)


class KTreeHeap:
    def __init__(self, iterable=None):
        self.root = None

        if iterable:
            for item in iterable:
                self.add_node(item)

    def add_node(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            parent = self.get_parent(self.root, val)

            pass


class FibHeap:
    def __init__(self, iterables=None):
        self.roots = []
        self.node_map = {}
        self.min_root = None

        if iterables:
            for iterable in iterables:
                self.add_tree(iterable)

    def heappop(self):
        # dereference child pointers of min_root & promote them
        if self.min_root is not None:
            min_val = self.min_root.val

            for child_key in self.min_root.keys():
                self.roots.append(self.min_root[child_key])
                del self.min_root[child_key]

            self.clean()  # merge roots with the same degrees
            return min_val  # return min val in fib heap
        else:
            raise AssertionError

    def heappush(self, val):
        new_node = Node(val)
        self.roots.append(new_node)
        self.node_map[val] = new_node

        # update min root if necessary
        if val < self.min_root.val:
            self.min_root = new_node

    def heapreplace(self, new_val, old_val):
        """This is a log n operation. """
        pass

    def clean(self):
        """merge root nodes with the same degree. Order of degree's is
        arbitrary, we will be going from left to right"""

        left_root, right_root = 0, len(self.roots)
        while left_root.degrees == right_root.degrees:
            self.merge(left_root, right_root)
            right_root += 1

    def merge(self, node1, node2):
        pass
