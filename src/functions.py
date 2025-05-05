from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    dmlr = [ x for node in old_nodes for x in node.text.split() if x.startswith(delimiter) or x.endswith(delimiter)]    
    lst = [x for node in old_nodes for x in node.text.split()]
    if len(dmlr) > 1:
        first = lst.index(dmlr[0])
        last = lst.index(dmlr[-1])
    else:
        one = lst.index(dmlr[0])

    result = []
    if len(dmlr) > 1:
        result.append(TextNode(" ".join(lst[0:first]), TextType.TEXT)) 
        result.append(TextNode(" ".join(lst[first:last+1]).strip(delimiter), text_type))
        result.append(TextNode(" ".join(lst[last+1:]), TextType.TEXT))
    else:
        result.append(TextNode(" ".join(lst[0:one]), TextType.TEXT)) 
        result.append(TextNode(" ".join(lst[one]).strip(delimiter), TextType.TEXT)) 
        result.append(TextNode(" ".join(lst[one+1:]), TextType.TEXT)) 

    return result
