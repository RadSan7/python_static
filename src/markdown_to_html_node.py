from .textnode import *
from .htmlnode import *
from .split_delimiter import *
from .markdown_blocks import *

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes=[]
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
   
    return html_nodes


def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# "):   # tylko H1
            return line[2:].strip()  # obetnij "# " i białe znaki
    raise Exception("No H1 header found in markdown")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children.append(ParentNode("p", text_to_children(block.replace('\n', ' '))))

        elif block_type == BlockType.HEADING:
            level = len(block.split(" ")[0])  # np. "### heading"
            text = block[level+1:]
            children.append(ParentNode(f"h{level}", text_to_children(text)))

        elif block_type == BlockType.CODE:
            code_content = block.strip("`")
            if code_content.startswith("\n"):
                code_content = code_content[1:]
            children.append(
                ParentNode("pre", [ParentNode("code", [LeafNode(None, code_content)])])
            )

        elif block_type == BlockType.QUOTE:
            text = "\n".join(line.lstrip("> ") for line in block.splitlines())
            children.append(ParentNode("blockquote", text_to_children(text)))

        elif block_type == BlockType.UNORDERED_LIST:
            items = [line.lstrip("- ") for line in block.splitlines()]
            li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
            children.append(ParentNode("ul", li_nodes))

        elif block_type == BlockType.ORDERED_LIST:
            items = [line.split(". ", 1)[1] for line in block.splitlines()]
            li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
            children.append(ParentNode("ol", li_nodes))

    return (ParentNode("div", children))