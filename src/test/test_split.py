from src.split_delimiter import split_nodes_delimiter
from src.textnode import TextNode, TextType
import unittest


class TestSplit(unittest.TestCase):

    def test_split_delimiter_code(self):
        node = TextNode("`This is text with a `code block word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0], [
            TextNode("This is text with a ", TextType.CODE),
            TextNode("code block word.", TextType.TEXT),
        ])
        print(new_nodes)

    def test_split_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0], [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word.", TextType.TEXT)
        ])
        print(new_nodes)

    def test_split_delimiter_italic(self):
        node = TextNode("This is text with a _italic block_ word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0], [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word.", TextType.TEXT)
        ])
        print(new_nodes)

    def test_split_delimiter_code_mutliple(self):
        node = TextNode("This is `text` with a `code block` word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0], [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.CODE),
            TextNode(" with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word.", TextType.TEXT)
        ])
        print(new_nodes)

    def test_split_no_delimiter(self):
        node = TextNode("This is text with a code block word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0], [
            TextNode("This is text with a code block word.", TextType.TEXT),
        ])
        print(new_nodes)

    def test_split_uneven_delimiter(self):
        node = TextNode("This is text with `a code block word.", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_split_wrong_delimiter(self):
        node = TextNode("This is text with a _code block` word.", TextType.TEXT)
        with self.assertRaises(SyntaxError):
            split_nodes_delimiter([node], "`", TextType.CODE)


if __name__ == "__main__":
    unittest.main()