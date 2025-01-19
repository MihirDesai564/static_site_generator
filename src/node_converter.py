from leafnode import LeafNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.BOLD_TEXT:
        node = LeafNode(text_node.text, "b")
        return node
    elif text_node.text_type == TextType.ITALIC_TEXT:
        node = LeafNode(text_node.text, "i")
        return node
    elif text_node.text_type == TextType.CODE_TEXT:
        node = LeafNode(text_node.text, "code")
        return node
    elif text_node.text_type == TextType.LINKS:
        node = LeafNode(text_node.text, "a", {"href": text_node.url})
        return node
    elif text_node.text_type == TextType.IMAGES:
        node = LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})
        return node
    elif text_node.text_type == TextType.NORMAL_TEXT:
        node = LeafNode(text_node.text, None)
        return node
    else: 
        raise ValueError("Unknown text type")
    

    