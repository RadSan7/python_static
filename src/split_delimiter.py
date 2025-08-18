from .textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if text_type == TextType.TEXT:
        return old_nodes

    delimiters = ['`', '**', '_']
    delimiters.remove(delimiter)
    new_nodes = []

    for node in old_nodes:
        
        delimiter_count = node.text.count(delimiter)
        
        for d in delimiters:
            if d in node.text:
                raise SyntaxError(f"Cannot split text with {d} when using {delimiter} as a delimiter.")
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