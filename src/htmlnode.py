class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        formatted = f" {' '.join(f'{k}="{v}"' for k, v in self.props.items())}"
        return formatted
    
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        elif not self.tag:
            return f"{self.value}"
        elif not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Error: No tag")
        elif not self.children:
            raise ValueError("Error: No children")
        if self.props:
            opening_tag = f"<{self.tag}{self.props_to_html()}>"     
        else:
            opening_tag = f"<{self.tag}>"
        closing_tag = f"</{self.tag}>"
        return opening_tag + "".join([child.to_html() for child in self.children]) + closing_tag
