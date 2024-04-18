class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props != None:
            final_props = " "
            for prop, value in self.props.items():
                temp = f"{prop}='{value}'"
                final_props = final_props + temp + " "
            return final_props.rstrip()
        else:
            return ""

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        self.props = props if props is not None else {}

    def to_html(self):
        if self.value == None:
            raise ValueError

        if self.tag == None:
            return f"{self.value}"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
