#!/usr/bin/env python3
print("hello world")
import os
from textnode import *
from leafnode import LeafNode
from htmlnode import HTMLnode
from parentnode import ParentNode
import split_nodes_delimiter as snd
import extract_markdown_images as emi
from text_to_textnode import TextToTextNode
from markdown_to_html_node import markdown_to_htmlnode
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

