import os
import shutil
from gencontent import generate_pages_recursive
import sys


def main_copy_func(source, target):
    if os.path.exists(target):
        shutil.rmtree(target)
        os.mkdir(target)
    else:
        os.mkdir(target)
    recursive_copy(source, target)

def recursive_copy(source, target):
    items_to_copy = os.listdir(source)
    for item in items_to_copy:
        item_path = os.path.join(source, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, os.path.join(target, item))
        elif os.path.isdir(item_path):
            new_target = os.path.join(target, item)
            new_source = os.path.join(source, item)
            os.mkdir(new_target)
            recursive_copy(new_source, new_target)


                
def main():
    print("Starting main function...")
    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    main_copy_func("static", "docs")
    with open("template.html", "r") as f:
        template = f.read()
    generate_pages_recursive("content", template, "docs", basepath)

if __name__ == "__main__":
    main()

