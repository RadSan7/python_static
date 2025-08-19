from .copy_static import copy_static
from .markdown_to_html_node import *

def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# "):   # tylko H1
            return line[2:].strip()  # obetnij "# " i białe znaki
    raise Exception("No H1 header found in markdown")

def generate_page(from_path, template_path, dest_path):

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


    final_content = final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html)

    # Write the final HTML to the destination file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print("updated")


    

def main():
    print("running copy")
    copy_static()
    index = "/Users/a12345678/Pliki/Boot.dev/python_static/python_static/content/index.md"
    template = "/Users/a12345678/Pliki/Boot.dev/python_static/python_static/template.html"
    dest = "/Users/a12345678/Pliki/Boot.dev/python_static/python_static/public/index.html"
    generate_page(index, template, dest)


main()
