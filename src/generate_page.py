import re, os, pathlib
from markdown_to_html_node import markdown_to_htmlnode  

def extract_title(markdown):
    regex = re.compile(r"^#\s*(?!#)(.+)", re.MULTILINE)
    matches = regex.match(markdown)
    return matches.group()[2:]

def generate_page(from_path, template_path, dest_path):
    print(f"Generating path from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        markdown_content = file.read()
    with open(template_path, "r") as file:
        template_content = file.read() 


    node = markdown_to_htmlnode(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    depth = from_path.count(os.sep)
    css_path = "../" * max(0,depth-1)+ "index.css"
    template_content = template_content.replace("{{ css_path }}", css_path)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template_content)


def generate_page_recursively(dir_path_content, template, dest_dir_path):
    content_path = pathlib.Path(dir_path_content)
    for item in content_path.iterdir():
        if os.path.isfile(item):
            if item.suffix.lower() == ".md":
                relative_path = item.relative_to(content_path)
                dest_file = pathlib.Path(dest_dir_path) / relative_path.with_suffix(".html")
                generate_page(str(item), template, str(dest_file))
        else:
            new_dest_dir = pathlib.Path(dest_dir_path) / item.name
            new_dest_dir.mkdir(exist_ok=True)

            generate_page_recursively(str(item), template, str(new_dest_dir))




