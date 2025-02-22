#!/usr/bin/env python3
from textnode import *
from static_public import file_transfer
from generate_page import generate_page_recursively


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    file_transfer()

    print("Generating page.....")
    generate_page_recursively(dir_path_content, template_path, dir_path_public)


if __name__ == "__main__":
    main()

