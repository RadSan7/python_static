import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLnode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_no_url(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertIsNone(node.url)

    def test_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://example.com")
        self.assertIsNotNone(node.url, "https://example.com")

    def test_text_type(self):
        node = TextNode("This is a code block", TextType.CODE)
        self.assertEqual(node.text_type, TextType.CODE)

    def test_attr(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://example.com/image.png")
        self.assertEqual(node.text, "This is an image")
        self.assertEqual(node.text_type, TextType.IMAGE)
        self.assertEqual(node.url, "https://example.com/image.png")

    def test_html_atributes(self):
        node = HTMLnode(tag="a", value="Click here", props={"href": "https://www.google.com","target": "_blank",})
        test_string = node.props_to_html()
        self.assertEqual(test_string, ' href="https://www.google.com" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Hello, world")
        self.assertEqual(node.to_html(), "Hello, world")

    def test_leaf_no_value(self):
        node = LeafNode("p", None)
        self.assertRaisesRegex(ValueError, "LeafNode must have a value", node.to_html)

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',)
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node2 = LeafNode("b", "grandchild")
        grandchild_node = LeafNode("b", "grandchild2")
        child_node = ParentNode("span", [grandchild_node, grandchild_node2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild2</b><b>grandchild</b></span></div>",)
        
if __name__ == "__main__":
    unittest.main()