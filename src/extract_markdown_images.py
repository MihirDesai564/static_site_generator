import re
from textnode import TextType, TextNode

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_link(old_nodes):
    regex =  re.compile(r'\[([^]]+)\]\(([^)]+)\)')
    new_nodes = []
    for node in old_nodes:
        
        text = node.text
        pos = 0
        while True:
            match = regex.search(text, pos)
            if not match:
                if pos < len(text):
                    new_nodes.append(TextNode(text[pos:], node.text_type, node.url))
                break
            if match.start(1) > pos:
                new_nodes.append(TextNode(text[pos:match.start()], node.text_type))
            new_nodes.append(TextNode(match.group(1), TextType.LINKS, match.group(2)))
            pos = match.end() 
    return new_nodes

def split_nodes_images(old_nodes):
    regex = re.compile(r'!\[([^]]+)\]\(([^)]+)\)')
    new_nodes = []
    for node in old_nodes:
        text = node.text
        pos = 0
        while True:
            match = regex.search(text, pos)
            if not match:
                if pos < len(text):
                    new_nodes.append(TextNode(text[pos:], node.text_type))
                break
            if match.start(1) > pos:
                new_nodes.append(TextNode(text[pos:match.start()], node.text_type))
            new_nodes.append(TextNode(match.group(1), TextType.IMAGES, match.group(2)))
            pos = match.end()
    return new_nodes
