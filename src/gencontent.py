from markdown_to_html import markdown_to_html_node
from extract_markdown import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = open(from_path, "r")
    md = md_file.read()
    md_file.close()
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    html_node = markdown_to_html_node(md)
    html_string = html_node.to_html()
    title = extract_title(md)
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    directories = os.path.dirname(dest_path)
    if directories != "":
        os.makedirs(directories, exist_ok=True)
    output_file = open(dest_path, "w")
    output_file.write(page)
    output_file.close()

