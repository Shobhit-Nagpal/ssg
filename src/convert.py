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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        size = len(images)
        if size == 0:
            new_nodes.append(node)
        else:
            i = 0
            split_nodes = node.text.split(
                f"![{images[0][0]}]({images[0][1]})", 1)
            while len(split_nodes) != 0:
                if i != 0 and i < size:
                    split_nodes = split_nodes[0].split(
                        f"![{images[i][0]}]({images[i][1]})")

                if split_nodes[0] != "":
                    if not split_nodes[0].isspace():
                        text_node = TextNode(split_nodes[0], TEXT_TYPE_TEXT)
                        new_nodes.append(text_node)

                if i < size:
                    image_node = TextNode(
                        images[i][0], TEXT_TYPE_IMAGE, images[i][1])
                    new_nodes.append(image_node)

                split_nodes.pop(0)
                i = i + 1

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        size = len(links)
        if size == 0:
            new_nodes.append(node)
        else:
            i = 0
            split_nodes = node.text.split(f"[{links[0][0]}]({links[0][1]})", 1)
            while len(split_nodes) != 0:
                if i != 0 and i < size:
                    split_nodes = split_nodes[0].split(
                        f"[{links[i][0]}]({links[i][1]})")

                if split_nodes[0] != "":
                    if not split_nodes[0].isspace():
                        text_node = TextNode(split_nodes[0], TEXT_TYPE_TEXT)
                        new_nodes.append(text_node)

                if i < size:
                    link_node = TextNode(
                        links[i][0], TEXT_TYPE_LINK, links[i][1])
                    new_nodes.append(link_node)

                split_nodes.pop(0)
                i = i + 1

    return new_nodes
