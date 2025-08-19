import os
import shutil

def copy_static():
    public = "/Users/a12345678/Pliki/Boot.dev/python_static/python_static/public"
    static = "/Users/a12345678/Pliki/Boot.dev/python_static/python_static/static"

    if os.path.exists(public):
        for item in os.listdir(public):
            item_path = os.path.join(public, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
    else:
        os.makedirs(public)

    for item in os.listdir(static):
        if item == ".DS_Store":
            continue 
        src_path = os.path.join(static, item)
        dst_path = os.path.join(public, item)
        if os.path.isdir(src_path):
            print(f"Kopiowanie folderu: {src_path} -> {dst_path}")
            shutil.copytree(src_path, dst_path)
        else:
            print(f"Kopiowanie pliku: {src_path} -> {dst_path}")
            shutil.copy2(src_path, dst_path)

copy_static()