import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("p", [LeafNode("Bold text", "b"), LeafNode("Normal text", "span")], {"class": "text"})
        node2 = ParentNode("p", [LeafNode("Bold text", "b"), LeafNode("Normal text", "span")], {"class": "text"})
        self.assertEqual(node, node2)
    def test_repr(self):
        node = ParentNode("p", [LeafNode("Bold text", "b"), LeafNode("Normal text", "span")], {"class": "text"})
        self.assertEqual(repr(node), "ParentNode(p, [LeafNode(Bold text, b, None), LeafNode(Normal text, span, None)], {'class': 'text'})") 
        
    def test_eq_fail(self):
        node = ParentNode("p", [LeafNode("Bold text", "b"), LeafNode("Normal text", "span")], {"class": "text"})
        node2 = ParentNode("p", [LeafNode("Bold text", "b"), LeafNode("Normal text", "span")], {"class": "text2"})
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()