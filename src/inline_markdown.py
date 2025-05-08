import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    #nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        elif delimiter not in node.text:
            result.append(node)
        else:
            #nodes.append(node)
            for x in node.text.split(delimiter):
                if x.startswith(" ") or x.endswith(" "):
                    result.append(TextNode(x, TextType.TEXT))
                else:
                    if x != "":
                        result.append(TextNode(x, text_type))

#    lst = [x for node in nodes for x in node.text.split(delimiter)]
#
#    for x in lst:
#        if x.startswith(" ") or x.endswith(" "):
#            result.append(TextNode(x, TextType.TEXT))
#        else:
#            if x != "":
#                result.append(TextNode(x, text_type))
    return result

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    result = []
#    nodes = []
#    for node in old_nodes:
#        if node.text_type != TextType.TEXT:
#            result.append(node)
#        else:
#            nodes.append(node)    

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            lst = re.split(r"(!\[.*?\]\(.*?\))", node.text)
            #print(len(lst))
            #print(lst)
            #if len(lst) >= 3:
            for x in lst:
                if x.startswith(" ") or x.endswith(" "):
                    result.append(TextNode(x, TextType.TEXT))
                else:
                    #print(x)
                    if x != "":
                        match = extract_markdown_images(x)
                        #print("match", match)
                        if match == []:
                            result.append(node)
                        else:
                            result.append(TextNode(match[0][0], TextType.IMAGE, match[0][1]))
    return result

def split_nodes_link(old_nodes):
    result = []
#    nodes = []
#    for node in old_nodes:
#        if node.text_type != TextType.TEXT:
#            result.append(node)
#        else:
#            nodes.append(node)    

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            #nodes.append(node)    
            lst = re.split(r"(\[.*?\]\(.*?\))", node.text)
            for x in lst:
                if x.startswith(" ") or x.endswith(" "):
                    result.append(TextNode(x, TextType.TEXT))
                else:
                    if x != "":
                        match = extract_markdown_links(x)
                        if match == []:
                            result.append(node)
                        else:
                            result.append(TextNode(match[0][0], TextType.LINK, match[0][1]))
    return result

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    bold_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD) 
    ital_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(ital_nodes, "`", TextType.CODE)
    imag_nodes = split_nodes_image(code_nodes)
    link_nodes = split_nodes_link(imag_nodes)
    #print(link_nodes)

#    non_text_nodes = []; text_nodes = []; result = []
#    for node in link_nodes:
#        if node.text_type != TextType.TEXT: non_text_nodes.append(node)
#        else: text_nodes.append(node)
#    for node1, node2 in zip(text_nodes, non_text_nodes):
#        result.append(node1)
#        result.append(node2)

    return link_nodes 

def text_to_textnodes2(text):
    nodes = [TextNode(text, TextType.TEXT)]
    bold_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD) 
    ital_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(ital_nodes, "`", TextType.CODE)
    imag_nodes = split_nodes_image(code_nodes)
    link_nodes = split_nodes_link(imag_nodes)
    return link_nodes
