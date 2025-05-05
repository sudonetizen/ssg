import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from functions import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)
    def test_false1(self):
        node3 = TextNode("this is a text node", TextType.BOLD)
        node4 = TextNode("this is a text node", TextType.LINK)
        self.assertNotEqual(node3, node4)
    def test_false2(self):
        node5 = TextNode("this is a text node", TextType.BOLD)
        node6 = TextNode("this is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node5, node6)
    def test_false3(self):
        node7 = TextNode("this is a text node", TextType.BOLD, "https://www.google.com")
        node8 = TextNode("this is a cool text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node7, node8)
    def test_eq_url(self):
        node1 = TextNode("this is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("this is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(node1, node2)
    def test_repr(self):
        node9 = TextNode("this is a text node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual("TextNode(this is a text node, link, https://www.boot.dev)", repr(node9))

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("this is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "this is a text node") 
    def test_image(self):
        node = TextNode("this is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "this is an image"})
    def test_bold(self):
        node = TextNode("this is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "this is bold")

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(new_nodes, [TextNode("This is text with a", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode("word", TextType.TEXT)]) 

if __name__ == "__main__":
    unittest.main()
