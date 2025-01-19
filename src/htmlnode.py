class HTMLnode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method must be implemented")
    
    def props_to_html(self):
        if self.props:
            return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        return ""
    
    def __repr__(self):
        return f"HTMLnode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if not isinstance(other, HTMLnode):
            return False
        return(self.tag == other.tag and 
               self.value == other.value and 
               self.children == other.children and 
               self.props == other.props)
    
