from markdown_to_html import markdown_to_html_node
from extract_markdown import extract_title
import os

def generate_pages_recursive(dir_path_content, template, dest_dir_path):
    dir_item_list = os.listdir(dir_path_content)
    for item in dir_item_list:
        item_path = os.path.join(dir_path_content, item)
        if item.endswith(".md"):
            with open(item_path, "r") as f:
                md = f.read()
            title = extract_title(md)
            html_string = markdown_to_html_node(md).to_html()
            page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
            output_file_path = os.path.join(dest_dir_path, item.replace(".md", ".html"))
            with open(output_file_path, "w") as f:
                f.write(page)
        else:
            if os.path.isdir(item_path):
                os.makedirs(os.path.join(dest_dir_path, item), exist_ok=True)
                generate_pages_recursive(item_path, template, os.path.join(dest_dir_path, item))
