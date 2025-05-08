from block_markdown import markdown_to_blocks, BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import text_node_to_html_node, TextNode, TextType
from inline_markdown import text_to_textnodes, text_to_textnodes2

def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    nodes = []
    for block in blocks:
        node = block_type_divider(block)
        nodes.append(node)
    return ParentNode("div", nodes)

def block_type_divider(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH: return p_html(block)
        case BlockType.HEADING: return h_html(block)
        case BlockType.CODE: return c_html(block)
        case BlockType.QUOTE: return q_html(block)
        case BlockType.UL: return ul_html(block)
        case BlockType.OL: return ol_html(block)
        case _: raise ValueError("invalid block type")

def p_html(block):
    text = " ".join(block.split("\n"))
    text_nodes = text_to_textnodes(text)
    return ParentNode("p", [text_node_to_html_node(node) for node in text_nodes])

def h_html(block):
    h_size = len(block.split()[0])
    text = " ".join(block.split()[1:])
    text_nodes = text_to_textnodes(text)
    return ParentNode(f"h{h_size}", [text_node_to_html_node(node) for node in text_nodes])

def c_html(block):
    lst = [x for x in block.split("\n") if x != "" and x != "```"]; string = ""
    for x in lst: string += x + "\n"
    child_node = LeafNode("code", string)
    return ParentNode("pre", [child_node])   

def q_html(block):
    text = " ".join([x for x in block.split() if x != ">"])
    text_nodes = text_to_textnodes(text)
    return ParentNode("blockquote", [text_node_to_html_node(node) for node in text_nodes])

def ul_html(block):
    lines = [x[2:] for x in block.split("\n") if x != ""]
    text_nodes = [text_to_textnodes(line) for line  in lines]
    html_nodes = [ [text_node_to_html_node(node) for node in line] for line in text_nodes ]
    parent_nodes = [ ParentNode("li", html_node) for html_node in html_nodes ]
    return ParentNode("ul", parent_nodes)  # hlines

def ol_html(block):
    lines = [x[3:] for x in block.split("\n") if x != ""]
    text_nodes = [text_to_textnodes(line) for line  in lines]
    html_nodes = [ [text_node_to_html_node(node) for node in line] for line in text_nodes ]
    parent_nodes = [ ParentNode("li", html_node) for html_node in html_nodes ]
    return ParentNode("ol", parent_nodes)   

#    html_nodes = []
#    for line in lines:
#        text_nodes = text_to_textnodes(line)
#        html_line = []
#        for node in text_nodes:
#            html_line.append(text_node_to_html_node(node))
#        html_nodes.append(html_line)
#    print(html_nodes) 
#    hlines = []
#    for line in html_nodes:
#        hlines.append(ParentNode("li", line))

#################################################################################
#def markdown_to_html_node(md):
#    blocks = markdown_to_blocks(md)
#   
#    block_nodes = []
#    text_nodes = []
#    s_parent_nodes = []
#
#    block_types = {BlockType.QUOTE: "blockquote", BlockType.UL: "ul", BlockType.OL: "ol", BlockType.CODE: "pre", BlockType.PARAGRAPH: "p"}
#
#    for block in blocks:
#        block_type = block_to_block_type(block)
#        if block_type == BlockType.HEADING:
#            h_size = len(block.split()[0])
#            block_nodes.append(HTMLNode(f"h{h_size}", block))
#        elif block_type == BlockType.CODE:
#            blist = [x for x in md.split("\n") if x != "" and x != "```"]
#            bstring = ""
#            for x in blist: bstring += x + "\n"
#            child_node = LeafNode("code", bstring)
#            parent_node = ParentNode("pre", [child_node])
#            s_parent_nodes.append(parent_node)
#        elif block_type == BlockType.UL:
#            blist = [x for x in md.split("\n") if x != ""]
#            children = []
#            for x in blist:
#                children.append(HTMLNode("li", x))
#            return ParentNode("div", LeafNode("ul", children)) 
#        else:
#            block_nodes.append(HTMLNode(block_types[block_type], block))
#
#    for node in block_nodes:
#        #print(node.value)
#        text_nodes.append(text_to_textnodes(" ".join(node.value.split())))    
#    
#    for bnode, tnodes in zip(block_nodes, text_nodes):
#        s_parent_nodes.append(ParentNode(bnode.tag, [ text_node_to_html_node(node) for node in tnodes  ]))

#    print(block_nodes)
#    print(text_nodes)
#    print(s_parent_nodes)
#    print()
    #return ParentNode("div", s_parent_nodes) 

