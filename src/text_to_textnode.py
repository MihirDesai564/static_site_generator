from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images, split_nodes_link, split_nodes_images
import re

def TextToTextNode(text):
    new_nodes_1 = split_nodes_delimiter([TextNode(text, TextType.NORMAL_TEXT)], "`", TextType.CODE_TEXT)
    print("This is code text splitter", new_nodes_1)

    new_nodes_2 = split_nodes_delimiter(new_nodes_1, "**", TextType.BOLD_TEXT)
    print("This is bold text splitter", new_nodes_2)
    print("")
    new_nodes_3 = split_nodes_delimiter(new_nodes_2, "*", TextType.ITALIC_TEXT)
    print("This is italic text splitter", new_nodes_3)
    print("")

    new_nodes_4 = split_nodes_images(new_nodes_3)
    print("This is image text splitter", new_nodes_4)
    new_nodes_5 = split_nodes_link(new_nodes_4)
    print("This is link text splitter", new_nodes_5)

    return new_nodes_5