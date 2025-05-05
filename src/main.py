from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, split_nodes_image, text_to_textnodes

def main():
    text_node_obj = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node_obj)    
    
    leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "color": "green"})
    print(leaf_node)
    print(leaf_node.__repr__())
    print(leaf_node.to_html())
    print()
    
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())
    print()
    
    node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes1 = split_nodes_delimiter([node1], "`", TextType.CODE)
    print(new_nodes1)
    print()

    node2 = TextNode("This is text with a **bolded** word", TextType.TEXT)
    new_nodes2 = split_nodes_delimiter([node2], "**", TextType.BOLD)
    print(new_nodes2)
    print()
    
    node3 = TextNode("This is text with a **bolded** word and **another**", TextType.TEXT)
    new_nodes3 = split_nodes_delimiter([node3], "**", TextType.BOLD)
    print(new_nodes3)
    print()

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    print('[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]')
    print()

    
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_image([node])
    print(new_nodes)
    print()
    
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    node = TextNode(text, TextType.TEXT)
    new_nodes = text_to_textnodes(node)
    print(new_nodes)

main()
