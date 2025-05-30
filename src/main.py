from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, split_nodes_image, text_to_textnodes, text_to_textnodes2
from markdown_html import markdown_to_html_node 
import os
import shutil
import sys

# directories
current_directory = os.getcwd()
public_directory = current_directory + "/docs" #current_directory + "/public"
os.makedirs(public_directory, exist_ok=True)
static_directory = current_directory + "/static"
from_path = current_directory + "/content/"
template_path = current_directory + "/template.html"
dest_path = public_directory

def static_to_public():
    # deleting contents of public directory 
    files = os.listdir(public_directory)
    for file in files:
        file_path = os.path.join(public_directory, file)
        if os.path.isfile(file_path): os.remove(file_path)
        else: shutil.rmtree(file_path)

    print(public_directory) 
    files = os.listdir(public_directory)
    print(files)

    # copying from static to public 
    files = os.listdir(static_directory)
    for file in files:
        file_path = os.path.join(static_directory, file)
        if os.path.isfile(file_path): os.system(f"cp {file_path} {public_directory}")
        else: os.system(f"cp -r {file_path} {public_directory}")

    print(public_directory) 
    files = os.listdir(public_directory)
    print(files)

def extract_title(markdown_line):
    if not "# " in markdown_line: raise Exception("title not found")
    else: return markdown_line[2:].strip()       

def generate_page(basepath, from_path, template_path, dest_path): 
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    files = os.listdir(from_path)
    for file in files:
        file_path = os.path.join(from_path, file)
        if os.path.isfile(file_path):   
            with open(file_path) as file: content = file.read()
            with open(template_path) as file: template = file.read()
            title = extract_title(content.split("\n")[0])
            hc = markdown_to_html_node(content).to_html()
            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", hc)

            # basepath
            template = template.replace('href="/', f'href="{basepath}')
            template = template.replace('src="/', f'src="{basepath}')

            with open(dest_path + "/index.html", "w") as file: file.write(template)
        else:
            new_dir = os.path.join(dest_path, file)
            os.makedirs(new_dir, exist_ok=True)
            generate_page(basepath, file_path, template_path, new_dir)    

#    with open(from_path) as file: content = file.read()
#    with open(template_path) as file: template = file.read()
#
#    title = extract_title(content.split("\n")[0])
#    print(title)
#    h_content = markdown_to_html_node(content)
#    print(h_content)
#    hc = h_content.to_html()
#
#    template = template.replace("{{ Title }}", title)
#    template = template.replace("{{ Content }}", hc)
#
#    with open(dest_path + "/index.html", "w") as file: file.write(template)

def main(basepath):  
#    print("###################################")
#    print()
#    md = "This series, a cornerstone of what I, in my many years as an **Archmage**, have come to recognize as the pinnacle of imaginative creation, stands unrivaled in its depth, complexity, and the sheer scope of its _legendarium_. As we embark on this exploration, let us delve into the reasons why this monumental work is celebrated as the finest in the world."
#    node = markdown_to_html_node(md)
#    print(node)
#    print()
#    print(node.to_html())
#    print()
#    print("########################################")

    static_to_public()
    generate_page(basepath, from_path, template_path, dest_path) 

basepath = sys.argv[1] if len(sys.argv) > 1  else "/"
main(basepath)  


#def main():
#    text_node_obj = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
#    print(text_node_obj)    
#    
#    leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "color": "green"})
#    print(leaf_node)
#    print(leaf_node.__repr__())
#    print(leaf_node.to_html())
#    print()
#    
#    child_node = LeafNode("span", "child")
#    parent_node = ParentNode("div", [child_node])
#    print(parent_node.to_html())
#    print()
#    
#    node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
#    new_nodes1 = split_nodes_delimiter([node1], "`", TextType.CODE)
#    print(new_nodes1)
#    print()
#
#    node2 = TextNode("This is text with a **bolded** word", TextType.TEXT)
#    new_nodes2 = split_nodes_delimiter([node2], "**", TextType.BOLD)
#    print(new_nodes2)
#    print()
#    
#    node3 = TextNode("This is text with a **bolded** word and **another**", TextType.TEXT)
#    new_nodes3 = split_nodes_delimiter([node3], "**", TextType.BOLD)
#    print(new_nodes3)
#    print()
#
#    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
#    print(extract_markdown_images(text))
#    print('[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]')
#    print()
#
#    
#    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
#    node = TextNode(text, TextType.TEXT)
#    new_nodes = split_nodes_image([node])
#    print(new_nodes)
#    print()
#    
#    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
#    new_nodes = text_to_textnodes(text)
#    print(new_nodes)
#    print()
#
#    print("#############################")
#
#    md = """
#This is **bolded** paragraph
#text in a p
#tag here 
#
#This is another paragraph with _italic_ text and `code` here
#
#"""
#    # md = "This is another paragraph with _italic_ text and `code` here"
#    node = markdown_to_html_node(md)
#    print(node)
#    print()
#    print(node.to_html())
#
#    print("#########################################")
#
#    md = """
## this is an h1
#
#this is paragraph text
#
### this is an h2
#"""
#
#    node = markdown_to_html_node(md)
#    print(node)
#    print()
#    print(node.to_html())
#    print()
#    print("###########################################################")
#    print()
#
#    
#    md = """
#- This is a list
#- with items
#- and _more_ items
#
#1. This is an `ordered` list
#2. with items
#3. and more items
#
#"""
#    node = markdown_to_html_node(md)
#    print(node)
#    print()
#    print(node.to_html())
#    print()
#
#main()
