from htmlnode import HTMLnode

class LeafNode(HTMLnode):
    def __init__(self, value,tag, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self): 
        if self.tag is None:
            return self.value
        if self.props != None:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.value}, {self.tag}, {self.props})"