from .copy_static import copy_static
from .markdown_to_html_node import *
import os
import sys


def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# "):   # tylko H1
            return line[2:].strip()  # obetnij "# " i białe znaki
    raise Exception("No H1 header found in markdown")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path}\n to {dest_path}\n using {template_path}")

    # Read markdown content
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    # Read template content
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()
    title = extract_title(markdown_content)
    final_html = (template_content.
                  replace("{{ Title }}", title).
                  replace("{{ Content }}", html).
                  replace('href="/', f'href="{basepath}').
                  replace('src="/', f'src="{basepath}')
                  )

    # Write the final HTML to the destination file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                rel_path = os.path.relpath(from_path, dir_path_content)
                rel_html = os.path.splitext(rel_path)[0] + ".html"
                dest_path = os.path.join(dest_dir_path, rel_html)

                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                generate_page(from_path, template_path, dest_path, basepath)

    

def main():
    print("running copy")
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_static()
    base_dir = os.path.dirname(os.path.dirname(__file__))
    index = os.path.join(base_dir, "content")
    template = os.path.join(base_dir, "template.html")
    dest = os.path.join(base_dir, "docs")

    generate_pages_recursive(index, template, dest, basepath)


main()
