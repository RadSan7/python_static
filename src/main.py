from textnode import *
from htmlnode import *

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)


main()
