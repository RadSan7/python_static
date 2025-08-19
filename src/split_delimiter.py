from .textnode import TextType, TextNode
import re

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if text_type == TextType.TEXT:
        return old_nodes

    delimiters = ['`', '**', '_']
    new_nodes = []

    for node in old_nodes:
        # jeśli już ma przypisany typ (np. CODE, LINK), to zostawiamy jak jest
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        
        delimiter_count = node.text.count(delimiter)
        
        
        if delimiter_count % 2 != 0:
            raise ValueError("The total number of characters in the nodes must be even.")
        
        split_text = node.text.split(delimiter)
        if node.text[0] == delimiter: formatted = True
        else: formatted = False

        new_node = []
        for line in split_text:
            if line == "": continue
            if formatted == False:
                new_node.append(TextNode(line, TextType.TEXT))
                formatted = True
            else:
                new_node.append(TextNode(line, text_type))
                formatted = False
        new_nodes.append(new_node)
    return new_nodes

def split_nodes_image(old_nodes):
    
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        matches = extract_markdown_images(node.text)
        original_text = node.text

        for match in matches:
            alt_text, url = match
            new_text = original_text.split(f"![{alt_text}]({url})")
            if new_text[0]:
                new_nodes.append(TextNode(new_text[0], TextType.TEXT))
            if alt_text:
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            original_text = new_text[1]
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.TEXT))    
    return new_nodes

def split_nodes_link(old_nodes):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        matches = extract_markdown_links(node.text)
        original_text = node.text

        for match in matches:
            alt_text, url = match
            new_text = original_text.split(f"[{alt_text}]({url})")
            if new_text[0]:
                new_nodes.append(TextNode(new_text[0], TextType.TEXT))
            if alt_text:
                new_nodes.append(TextNode(alt_text, TextType.LINK, url))
            original_text = new_text[1]
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.TEXT))
        
    return new_nodes

def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT, None)]

    for part in node:  
        if ('**') in part.text: 
            node = split_nodes_delimiter(node, '**', TextType.BOLD)
    node = flatten(node)
    for part in node:    
        if ('`') in part.text: 
            node = split_nodes_delimiter(node, '`', TextType.CODE)
    node = flatten(node)
    for part in node:
        if ('_') in part.text:
            node = split_nodes_delimiter(node, '_', TextType.ITALIC)
    node = flatten(node)

    for part in node:    
        matches = extract_markdown_images(part.text)
        if matches:
            node = split_nodes_image(node)
            break   # przerwij, żeby nie robić tego kilka razy

    for part in node:    
        matches = extract_markdown_links(part.text)
        if matches:
            node = split_nodes_link(node)
            break

    return node




def flatten(nodes):
    flat = []
    for n in nodes:
        if isinstance(n, list):
            flat.extend(flatten(n))
        else:
            flat.append(n)
    return flat