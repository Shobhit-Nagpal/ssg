def text_node_to_html_node(text_node):
    switch text_node.text_type:
        case "text":
            return convert_text_to_html(text_node)
        case "bold":
            return convert_bold_to_html(text_node)
        case "italic":
            return convert_italic_to_html(text_node)
        case "code":
            return convert_code_to_html(text_node)
        case "link":
            return convert_link_to_html(text_node)
        case "image":
            return convert_image_to_html(text_node)
        case _:
            print("Not a valid text node type")


def convert_text_to_html(text_node):
    return LeafNode(value=text_node.text)

def convert_bold_to_html(text_node):
    return LeafNode("b", text_node.text)

def convert_italic_to_html(text_node):
    return LeafNode("i", text_node.text)

def convert_code_to_html(text_node):
    return LeafNode("code", text_node.text)

def convert_link_to_html(text_node):
    return LeafNode("a", text_node.text, {"href": text_node.url})

def convert_image_to_html(text_node):
    return LeafNode("img","", {"src": text_node.url, "alt": text_node.text})
