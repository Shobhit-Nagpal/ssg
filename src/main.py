import os
import sys
import shutil

public_path = f"{os.getcwd()}/public/"
static_path = f"{os.getcwd()}/static/"

def main():
    copy_contents()

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
        sys.exit(1)

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

main()
