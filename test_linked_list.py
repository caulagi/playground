# -*- coding: utf-8 -*-

import unittest
from linked_list import LinkedList

class TestLinkedLilst(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList("a", "b", "c")

    def tearDown(self):
        pass

    def test_empty_list(self):
        l = LinkedList("a")
        self.assertEquals(l[0].data, 'a')

    def test_access_by_index(self):
        l = self.linked_list
        self.assertEquals(l[0].data, 'a')
        self.assertEquals(l[1].data, 'b')
        self.assertEquals(l[2].data, 'c')

    def test_adding_at_beginning(self): 
        l = self.linked_list
        l.prepend("d")
        self.assertEquals(l[0].data, 'd')
        
    def test_adding_at_end(self): 
        l = self.linked_list
        l.append("e")
        self.assertEquals(l[3].data, 'e')

    def test_negative_indexing(self): 
        l = self.linked_list
        l.append("e")
        self.assertEquals(l[-1].data, 'e')
        self.assertEquals(l[-2].data, 'c')

if __name__ == "__main__":
    unittest.main()
