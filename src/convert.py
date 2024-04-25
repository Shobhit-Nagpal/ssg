import re
from htmlnode import LeafNode
from textnode import TextNode

TEXT_TYPE_TEXT = "text"
TEXT_TYPE_BOLD = "bold"
TEXT_TYPE_ITALIC = "italic"
TEXT_TYPE_CODE = "code"
TEXT_TYPE_LINK = "link"
TEXT_TYPE_IMAGE = "image"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(value=text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Not a valid text node type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []      
    closing_limiter_found = False

    for node in old_nodes:
        if node.text_type != TEXT_TYPE_TEXT:
            nodes.append(node)
            continue
        
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid Markdown syntax")

        split_nodes = node.text.split(delimiter)
        for idx, split_node in enumerate(split_nodes):
            if idx % 2 == 0:
                text_node = TextNode(split_node, TEXT_TYPE_TEXT)
                nodes.append(text_node)
                continue

            text_node = TextNode(split_node, text_type)
            nodes.append(text_node)

    return nodes

def extract_markdown_images(text):
#    r"!\[(.*?)\]\((.*?)\)"
    all_images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return all_images

def extract_markdown_links(text):
    all_links = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return all_links
