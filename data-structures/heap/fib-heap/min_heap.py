"""
Lazy but smarter way of "cleaning" up our heap. Heap consolidation only
happens after a pop. Replace will be implemented by splicing the
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

potential function - https://www.youtube.com/watch?v=6_BBQWQ2HQQ

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
        self.parent = None
        self.children = {}
        self.loser = False
        self.degrees = len(self.children)

    def add_child(self, child_node):
        if child_node.val not in self.children:
            self.children[child_node.val] = child_node
            child_node.parent = self


class FibHeap:
    def __init__(self, iterable=None):
        self.roots = {}  # map of all root nodes
        self.node_map = {}  # map of all nodes
        self.min_root = None

        if iterable:
            for item in iterable:
                self.push(item)

    def peek(self):
        if self.min_root is not None:
            return self.min_root.val
        else:
            raise AssertionError

    def pop(self):
        # TODO: Why can we only clean up roots with the same degrees?
        # This is avoid a heap-tree structure that is shallow and wide.

        # dereference child pointers of min_root & promote orphans
        if self.min_root is not None:
            min_val = self.min_root.val

            for child_key in self.min_root.keys():
                # mark promoted orphans an non losers
                self.min_root[child_key].loser = False
                self.roots[self.min_root[child_key]]
                # dereference pointers to all children/parent
                del self.min_root[child_key]
                self.node_map[child_key].parent = None

            del self.node_map[self.min_root.val]  # del min root node
            self._clean()  # merge roots with the same degrees
            self._update_min_root()  # find new min root
            return min_val  # return min val in fib heap
        else:
            raise AssertionError

    def push(self, val):
        new_node = Node(val)
        self.roots[new_node.val] = new_node
        self.node_map[val] = new_node

        # update min root if necessary
        if val < self.min_root.val:
            self.min_root = new_node

    def replace(self, new_val, old_val):
        """This is a log n operation. """
        # TODO: check losers

        # get node
        replace_node = self.node_map[old_val]
        # update the val
        replace_node.val = new_val

        while replace_node.loser is True:
            # check if there is a heap violation
            if self._is_violated(replace_node.parent, replace_node):
                # if there is, remove the child and append it as a new root
                parent = replace_node.parent
                del parent[replace_node.val]
                self.roots[replace_node.val] = replace_node
                # reassign node to parent
                replace_node = replace_node.parent

    def merge(self, node1, node2):
        if node1.val < node2.val:
            node2.add_child(node1)
        else:
            node1.add_child(node2)

    def _update_loser(self):
        pass

    def _is_violated(self, parent, child):
        return parent.val > child.val

    def _update_min_root(self):
        min_val = float("inf")

        for root in self.roots.values():
            min_val = min(min_val, root.val)

        self.min_root = self.node_map[min_val]

    def _clean(self):
        """merge root nodes with the same degree. Order of degree's is
        arbitrary, we will be going from left to right"""

        for root_node in self.roots.values():
            for other_root in self.roots.values():
                if root_node.degrees == other_root.degrees and root_node != other_root:
                    self.merge(root_node, other_root)
                    self._clean()
