import re

def markdown_to_blocks(markdown):
    lines = markdown.splitlines()
    blocks = []
    list_adder = ""
    code = False

    def flush_list_buffer():
            nonlocal list_adder
            nonlocal code   
            if list_adder:  
                list_adder = list_adder.strip()
                blocks.append(list_adder)
                list_adder = ""
                code = False

    for line in lines:
        line = line.strip()

        if not line:
            flush_list_buffer()
            continue

        if line.startswith("*" or "- "):
            list_adder += line + "\n"
        elif re.match(r"^\d\.\s", line):
            list_adder += line + "\n"
        elif line.startswith("```") or code == True:
            list_adder += line + "\n"
            code = True
        else:
            flush_list_buffer()
            blocks.append(line)


    flush_list_buffer()

    blocks = [block for block in blocks if block]
    
    return blocks








        



