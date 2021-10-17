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

Shallow & wide trees are an issue.

[      root1      ]
child_1  child_2  child_3  child_4  child_5
            |       |
        child_6  child_7

Degree or rank is the same as "number of children" in formal
literature on fibonacci heaps/priority queues.
"""

from fib_doubly_linked_list import DoublyLinkedList, FibNode


class FibHeap:
    def __init__(self, iterable=None):
        self.roots = DoublyLinkedList()
        self.node_map = {}  # map of all nodes
        self.min_root = FibNode(float("inf"))

        if iterable:
            for item in iterable:
                self.push(item)

    def peek(self):
        if self.min_root is not None and self.min_root.val != float("inf"):
            return self.min_root.val
        else:
            raise AssertionError

    def pop(self):
        # dereference child pointers of min_root & promote orphans
        if self.min_root is not None:
            min_val = self.min_root.val

            children = self.min_root.children.values()

            for child_node in children:
                # promote children to root
                self._promote(child_node)
                # dereferences parent pointer
                self._remove(self.min_root, child_node)

            # del min root
            del self.node_map[self.min_root.val]
            self.min_root = None

            self._clean()  # merge roots with the same degrees
            self._update_min_root()  # find new min root

            return min_val  # return min val in fib heap
        else:
            raise AssertionError

    def push(self, val):
        # add new node to roots & node map
        self.roots.append(val)
        self.node_map[val] = self.roots.tail

        # update min root if necessary
        if val < self.min_root.val:
            self.min_root = self.roots.tail

    def replace(self, new_val, old_val):
        """Replace node with new val, check for heap violations
        Splice node to root if there is a heap violation"""
        # get node
        replace_node = self.node_map[old_val]
        # update the val
        replace_node.val = new_val

        # check if there is a heap violation
        if self._is_violated(replace_node.parent, replace_node):
            self._cut(replace_node.parent, replace_node)
            self._cascading_cut(replace_node.parent)

            if replace_node.parent not in self.roots:
                # double loser
                replace_node.parent.loser = True

    def _cut(self, parent_node, child_node):
        """Remove child from parent & decrement degree. Promote child to root,
        make its parent None & unmark child node to non loser"""
        del parent_node[child_node.val]
        parent_node.degree -= 1
        child_node.loser = False

        # promote child to root
        self.roots.append(child_node)

    def _cascading_cut(self, node):
        """Continue cutting upward on path from the decreased node towards
        the root until we are met with a root or non loser"""
        parent = node.parent

        if parent is not None:
            if parent.loser is False:
                parent.loser = True
            else:
                self._cut(parent, node)
                self._cascading_cut(parent)

    def _merge(self, node1, node2):
        print("NODE 1 ", node1.val, "NODE 2 ", node2.val)
        if node1.val < node2.val:
            node2.add_child(node1)
            self.roots.remove(node1)
        else:
            node1.add_child(node2)
            self.roots.remove(node2)

    def _promote(self, orphan_node):
        # mark promoted orphans an non losers
        orphan_node.loser = False
        self.roots.append(orphan_node)

    def _remove(self, parent_node, child_node):
        # dereference pointers
        child_node.parent = None
        del parent_node.children[child_node.val]
        self.roots.remove(parent_node)

    def _is_violated(self, parent, child):
        return parent.val > child.val

    def _update_min_root(self):
        min_val = float("inf")

        node = self.roots.head
        while node is not None:
            min_val = min(min_val, node.val)
            node = node.next

        self.min_root = self.node_map[min_val]

    def _clean(self):
        """merge root nodes with the same degree. Order of degree's is
        arbitrary, we will be going from left to right"""

        # if there is only node in all the degrees that exist, we know
        # that there are no more nodes with the same degrees in self.roots

        if self._has_unique_degrees_only():
            return

        degrees = {}

        node = self.roots.head
        while node is not None:
            if node.degree in degrees:
                self._merge(node, degrees[node.degree][0])
                self._clean()
            else:
                degrees[node.degree] = [node]

        return

    def _has_unique_degrees_only(self):
        unique_degrees = set()

        node = self.roots.head
        while node is not None:
            unique_degrees.add(node.degree)
            node = node.next

        return len(self.roots) == len(unique_degrees)
