class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None: return ""
        return " ".join(list(map(lambda x: f'{x}="{self.props[x]}"', self.props)))     

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
     
    def to_html(self):
        if self.value == None: raise ValueError("value error")
        elif self.tag == None: return self.value
        else: 
            if self.props != None: return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
            else: return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None: raise ValueError("value error")
        elif self.children is None: raise ValueError("children value error")
        else:
            if self.props is not None:
                return f"<{self.tag} {self.props_to_html()}>{"".join(list(map(lambda ch: ch.to_html(), self.children)))}</{self.tag}>"
            else:
                return f"<{self.tag}>{"".join(list(map(lambda ch: ch.to_html(), self.children)))}</{self.tag}>"


    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

