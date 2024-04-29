import os
import sys
import shutil
from block_markdown import generate_page
from pathlib import Path

public_path = f"{os.getcwd()}/public/"
static_path = f"{os.getcwd()}/static/"
content_path = f"{os.getcwd()}/content/"
template_path = f"{os.getcwd()}/template.html"

def main():
    copy_contents()
    generate_pages_recursive(content_path, template_path, public_path)

def copy_contents():

    if not os.path.exists(public_path):
        os.mkdir(public_path)

    # Clear public directory
    contents = os.listdir(public_path)
    for content in contents:
        if os.path.isfile(public_path + content):
            os.remove(public_path + content)
        else:
            shutil.rmtree(public_path + content)

    # Paste from static to public
    if not os.path.exists(static_path):
        raise Exception("static directory does not exist")
        sys.exit()

    contents = os.listdir(static_path)
    for content in contents:
        if os.path.isfile(static_path + content):
            shutil.copy(static_path + content, public_path)
            print(f"Copied {static_path + content} to public")
        else:
            dir_path = static_path + content + "/"
            public_dir = public_path + content + "/"
            os.mkdir(public_dir)
            copy_dir(dir_path, public_dir)

def copy_dir(src, dest):
    dir_contents = os.listdir(src)
    for dir_content in dir_contents:
        if os.path.isfile(src + dir_content):
            shutil.copy(src + dir_content, dest)
            print(f"Copied {src + dir_content} to public")
        else:
            dir_path = src + dir_content + "/"
            public_dir = dest + dir_content + "/"
            os.mkdir(public_dir)
            copy_dir(dir_path, public_dir)



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    if not os.path.exists(dir_path_content):
        raise Exception(f"{dir_path_content} does not exist")
        sys.exit()

    content_dir_files = os.listdir(dir_path_content)

    for content_dir_file in content_dir_files:
        if os.path.isfile(dir_path_content + content_dir_file):
            if Path(content_dir_file).suffix == ".md":
                html_page_name = os.path.splitext(content_dir_file)[0] + ".html"
                generate_page(dir_path_content + content_dir_file, template_path, dest_dir_path + html_page_name)
        else:
            os.mkdir(os.path.join(dest_dir_path, content_dir_file))
            generate_pages_recursive(dir_path_content + content_dir_file + "/", template_path, dest_dir_path + content_dir_file + "/")

main()
