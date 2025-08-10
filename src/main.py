import os
import shutil
from gencontent import generate_page


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
    main_copy_func("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()

