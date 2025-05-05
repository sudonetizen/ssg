import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_prosper_to_html1(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
    def test_prosper_to_html2(self):
        node = HTMLNode(props={"href": "https://www.bootdev.com", "target": "_self"})
        self.assertEqual(node.props_to_html(), 'href="https://www.bootdev.com" target="_self"')
    def test_prosper_to_html3(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node.props_to_html(), 'href="https://www.duckduckgo.com" target="_blank"')
    def test_tag_value(self):
        node = HTMLNode("div", "humans can fly")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "humans can fly")
    def test_children_props(self):
        node = HTMLNode("div", "humans can fly")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    def test_repr(self):
        node = HTMLNode("div", "humans can fly", None, {"color": "green"})
        self.assertEqual(node.__repr__(), "HTMLNode(div, humans can fly, None, {'color': 'green'})")
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "humans can fly")
        self.assertEqual(node.to_html(), "humans can fly")
    def test_to_html_wit_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>") 
    def test_html_many_children(self):
        node = ParentNode("p", [LeafNode("b", "bold text"), LeafNode(None, "normal text"), LeafNode("i", "italic text"), LeafNode(None, "normal text")])
        self.assertEqual(node.to_html(), "<p><b>bold text</b>normal text<i>italic text</i>normal text</p>")
    def test_headings(self):
        node = ParentNode("h2", [LeafNode("b", "bold text"), LeafNode(None, "normal text"), LeafNode("i", "italic text"), LeafNode(None, "normal text")])
        self.assertEqual(node.to_html(), "<h2><b>bold text</b>normal text<i>italic text</i>normal text</h2>")
    
if __name__ == "__main__":
    unittest.main() 
