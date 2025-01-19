import re

def block_to_block_type(block):
    if re.match(r"^#{1,6}\s", block):
        return "heading"
    elif block[:3] == "```" and block[-3:] == "```":
        return "code"
    elif block.startswith("* " or"- "):
        return "unordered_list"
    elif block.startswith(">"):
        return "quote"
    elif re.match(r"^\d+\.\s", block):
        return "ordered_list"
    else:
        return "paragraph"    
    

