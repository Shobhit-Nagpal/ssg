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
            raise ValueError("No value present in leaf node")

        if self.tag == None:
            return f"{self.value}"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        self.children = children if children is not None else []

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag mentioned for parent node")

        if self.children == []:
            raise ValueError("No children elements in parent node")

        
        children_html = ""
        for node in self.children:
            child_html = node.to_html()
            children_html = children_html + child_html

        return f"<{self.tag}>{children_html}</{self.tag}>"
