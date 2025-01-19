import unittest

from textnode import TextNode, TextType
import split_nodes_delimiter as snd

class testsnd(unittest.TestCase):
    def testit(self):
        node = TextNode("This is a text `CODE BLOCK` node", TextType.BOLD_TEXT)
        new_nodes = snd.split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes, [TextNode("This is a text ", TextType.NORMAL_TEXT), TextNode("CODE BLOCK", TextType.CODE_TEXT), TextNode(" node", TextType.NORMAL_TEXT)])

        node1 = TextNode("This is a text `CODE BLOCK`", TextType.BOLD_TEXT)
        new_nodes1 = snd.split_nodes_delimiter([node1], "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes1, [TextNode("This is a text ", TextType.NORMAL_TEXT), TextNode("CODE BLOCK", TextType.CODE_TEXT)])

        node2 = TextNode("`CODE BLOCK`", TextType.BOLD_TEXT)
        new_nodes2 = snd.split_nodes_delimiter([node2], "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes2, [TextNode("CODE BLOCK", TextType.CODE_TEXT)])

        node3 = TextNode("sadfdsfasdf `Mihir` adsfadsf `Desai`", TextType.BOLD_TEXT)
        new_nodes3 = snd.split_nodes_delimiter([node3], "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes3, [TextNode("sadfdsfasdf ", TextType.NORMAL_TEXT), TextNode("Mihir", TextType.CODE_TEXT), TextNode(" adsfadsf ", TextType.NORMAL_TEXT), TextNode("Desai", TextType.CODE_TEXT)])
