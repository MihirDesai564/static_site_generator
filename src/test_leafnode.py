import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("This is a text node", "p")
        node2 = LeafNode("This is a text node", "p")
        self.assertEqual(node, node2)

    def test_to_html(self):
        node = LeafNode("This is a text node", "p")
        self.assertEqual(node.to_html(), "<p>This is a text node</p>")

    def test_eq_fail(self):
        node = LeafNode("This is a text node", "p")
        node2 = LeafNode("This is a text node", "div")
        self.assertNotEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()