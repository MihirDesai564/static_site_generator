from block_to_block_type import block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_textnode import TextToTextNode
from node_converter import text_node_to_html_node


markdown_filepath = "./content/index.md"
with open(markdown_filepath, "r") as file:
    content = file.read()


def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def text_to_children(text):
    text_nodes = TextToTextNode(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        print("this is htmlnode"*12)
        print(html_node)
        children.append(html_node)
    return children


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == "heading":
        return heading_block_to_htmlnode(block)
    elif block_type == "code":
        return code_block_to_htmlnode(block)
    elif block_type == "unordered_list":
        return unordered_list(block)
    elif block_type == "ordered_list":
        return ordered_list(block)
    elif block_type == "quote":
        return quote_to_htmlnode(block)
    elif block_type == "paragraph":
        return paragraph_to_htmlnode(block)
    else:
        print("-*12")
        print(block)
        raise ValueError("Invalid Block Type")
    

def paragraph_to_htmlnode(block):
    lines = block.split("\n")
    para = " ".join(lines)
    children = text_to_children(para)
    return ParentNode("p", children)
    

def heading_block_to_htmlnode(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    text = block[level+1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_block_to_htmlnode(block):
    print(block)
    if not (block.startswith("```") or block.endswith("```")):
        raise ValueError("Invalid code Block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def unordered_list(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def ordered_list(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def quote_to_htmlnode(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


print(markdown_to_htmlnode(content).to_html())


