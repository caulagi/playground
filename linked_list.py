# -*- coding: utf-8 -*-

"""
A linked list module with the interfaces you expect.

>>> str(LinkedList("a", "b", "c"))
'a,b,c'
>>> l = LinkedList("a", "b", "c")
>>> l.prepend("d")
>>> str(l)
'd,a,b,c'
>>> l.append("e")
>>> str(l)
'd,a,b,c,e'
"""

class LinkedList(object):
    """A linked list data structure allows dynamic addition of
    nodes and sequential access to the data.  It has the following
    guarantees

    insert at beginning/end - O(1)
    search/find an element in the list - O(N)
    deletion at beginning/end - O(1)
    """

    class _Node(object):
        
        def __init__(self, data, after=None):
            self._data = data
            self._after= after

        def __str__(self):
            return str(self._data)

        @property
        def after(self):
            return self._after
          
        @after.setter
        def after(self, node):
            self._after = node

        @property
        def data(self):
            return self._data

    def __init__(self, *args, **kwargs):
        if not args:
            return
        node = self._Node(args[0])
        self._end = self._start = node
        self._len = 1
        for arg in args[1:]:
            self.append(arg)

    def append(self, data):
        """Add at the end of the list"""

        node = self._Node(data)
        self._end.after = node
        self._end = node
        self._len += 1

    def prepend(self, data):
        """Add at the beginning of the list"""

        node = self._Node(data, self._start)
        self._start = node
        self._len += 1

    def __getitem__(self, key):
        node  = self._start
        # handle negative indexes
        quo, mod = divmod(key, self._len)
        for index in xrange(0, mod):
            if not node.after:
                raise IndexError("Invalid index: %s" % key)
            node = node.after
        return node

    def __len__(self):
        return self._len

    def __iter__(self):
        """Lazily iterate over the list"""

        node = self._start
        yield node
        while node.after:
            node = node.after
            yield node
        raise StopIteration

    def __str__(self):
        return (','.join(str(node) for node in self))

    @property
    def start(self):
        """Get the start of the list"""
        return self._start

    @property
    def end(self):
        """Get the end of the list"""
        return self._end

    def __reversed__(self):
        """Return the list reversed"""
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
