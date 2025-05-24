

class HTMLNode ():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html = ""
        for prop in self.props:
            html += " " + prop + '="' + self.props[prop] + '"'
        return html
    
    def __repr__(self):
        return f"HTML Node: Tag = {self.tag} Value= {self.value} Children= {self.children} Props= {self.props}"
    
class LeafNode (HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError()
        
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode (HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Mising tag")
        
        if self.children is None:
            raise ValueError("Parent Node must have children")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'
        