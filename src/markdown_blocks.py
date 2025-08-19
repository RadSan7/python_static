from enum import Enum

class BlockType(Enum):
   PARAGRAPH = "paragraph"
   HEADING = 'heading'
   CODE = 'code'
   QUOTE = 'quote'
   UNORDERED_LIST = 'unordered_list'
   ORDERED_LIST = 'ordered_list'

def markdown_to_blocks(markdown):
    new_markdown = []
    markdown = markdown.split('\n\n')
    for line in markdown:
        line = line.strip()
        if line:  # tylko jeśli niepusty
            cleaned = "\n".join(line.lstrip("\t").strip() for line in line.splitlines()).strip()
            if cleaned:   # upewnij się, że po czyszczeniu coś zostało
                new_markdown.append(cleaned)

    return new_markdown

    return new_markdown

def block_to_block_type(block):

    if block.startswith("```"):
        if block.endswith("```"):
            return BlockType.CODE
        
    for i in range(1,6):
        text = ('#' * i) + ' '
        if block.startswith(text):
            return BlockType.HEADING
    
    if block[0] in ('>','-') or (block[0].isdigit() and block[1] == "."):
        block_split = block.split('\n')
        check = True
        if block[0] == '>':
            for line in block_split:
                if line [0] != '>':
                    check = False
            if check:
                return BlockType.QUOTE
        
        if block[0] == '-':
            for line in block_split:
                if line [0] != '-':
                    check = False
            if check:
                return BlockType.UNORDERED_LIST
        
        if block[0].isdigit():
            for i, line in enumerate(block_split):
                if line[1] != "." or int(line[0]) != i + 1:
                    check = False
            if check:
                return BlockType.ORDERED_LIST
        
    return BlockType.PARAGRAPH


