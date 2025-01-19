import unittest

from node_converter import text_node_to_html_node
from textnode import TextNode, TextType


class TestNodeConverter(unittest.TestCase):
    def test_text_node_to_html_node(self):
        text_node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node = text_node_to_html_node(text_node)
        self.assertEqual(node, "<b>This is a text node</b>")
        
        text_node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        node = text_node_to_html_node(text_node)
        self.assertEqual(node, "<i>This is a text node</i>")
        
        text_node = TextNode("This is a text node", TextType.CODE_TEXT)
        node = text_node_to_html_node(text_node)
        self.assertEqual(node, "<code>This is a text node</code>")
        
        text_node = TextNode("This is a text node", TextType.LINKS, "https://www.google.com")
        node = text_node_to_html_node(text_node)
        self.assertEqual(node, "<a href=\"https://www.google.com\">This is a text node</a>")
        
        text_node = TextNode("This is a text node", TextType.IMAGES, "https://www.google.com")
        node = text_node_to_html_node(text_node)
        self.assertEqual(node, "<img src=\"https://www.google.com\" alt=\"This is a text node\">")
        
        text_node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        node = text_node_to_html_node(text_node)
        self.assertEqual(node, "This is a text node")
        
    