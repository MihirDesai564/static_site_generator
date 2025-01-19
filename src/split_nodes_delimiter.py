from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
            text = node.text
            if delimiter == "**":
                current_pos = 0
                while True:
                    start = text.find(delimiter, current_pos)
                    print(f"start: {start} current_pos: {current_pos} text: {text}")
                    if start == -1:
                        if current_pos < len(text):
                                new_nodes.append(TextNode(text[current_pos:], node.text_type))   
                        break
                        
                    if start >= current_pos:
                        new_nodes.append(TextNode(text[current_pos:start], node.text_type))
                    else:
                        print("start-1", start)
                        print("current_pos-1", current_pos) 
                        print(len(text))
                        break

                    end = text.find(delimiter, start + 2)
                    # print("end", end)
                    if end == -1:
                        new_nodes.append(TextNode(text[start+2:], node.text_type))
                        break
                    new_nodes.append(TextNode(text[start+2:end], text_type))
                    current_pos = end + 2    
            else:
                all_positions = [m.start() for m in re.finditer(re.escape(delimiter), text)]
                # print(f"all_positions: {all_positions} node: {node.text}")
                if len(all_positions) <= 1:
                    new_nodes.append(TextNode(text, node.text_type))
                else:
                    pos = 0
                    start = 0 
                    while pos < len(all_positions):
                        if start == all_positions[pos]:
                            new_nodes.append(TextNode(text[all_positions[pos]+1: all_positions[pos+1]], text_type))
                        else:
                            new_nodes.append(TextNode(text[start:all_positions[pos]], node.text_type))
                            new_nodes.append(TextNode(text[all_positions[pos]+1: all_positions[pos+1]], text_type))
                        start = all_positions[pos+1] + 1
                        pos = pos + 2
                        if start > len(text):
                                break
                    if start < len(text):
                        new_nodes.append(TextNode(text[start:], node.text_type))

    return [node for node in new_nodes if node.text != ""]

