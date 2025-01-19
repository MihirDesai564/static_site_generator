from htmlnode import HTMLnode
from leafnode import LeafNode

class ParentNode(HTMLnode):
    def __init__(self, tag, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag must be provided")
        children_html = ""
        for child in self.children:
            if self.tag is None:
                raise ValueError("Invalid HTML no tag")
            elif self.children is None:
                raise ValueError("Invalid HTML no children")
            children_html += child.to_html()
        if self.props != None:
            return f"<{self.tag} {self.props_to_html()}>{children_html}</{self.tag}>"
        return f"<{self.tag}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"