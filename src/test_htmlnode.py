import unittest

from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLnode("p", "This is a text node")
        node2 = HTMLnode("p", "This is a text node")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLnode("p", "This is a text node")
        self.assertEqual(repr(node), "HTMLnode(p, This is a text node, None, None)")

    def test_eq_fail(self):
        node = HTMLnode("p", "This is a text node")
        node2 = HTMLnode("div", "This is a text node")
        self.assertNotEqual(node, node2)
    
if __name__ == "__main__":
    unittest.main()