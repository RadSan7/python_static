import re

def extract_markdown_images(text):
    markdown_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    print(markdown_text)        
    return markdown_text

def extract_markdown_links(text):
    markdown_text = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    print(markdown_text)
    return markdown_text