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
            raise ValueError(
                f"Not a valid text node type: {text_node.text_type}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []

    for node in old_nodes:
        if node.text_type != TEXT_TYPE_TEXT:
            nodes.append(node)
            continue

        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
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
        if node.text_type != TEXT_TYPE_TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        size = len(images)
        if size == 0:
            new_nodes.append(node)
            continue

        original_text = node.text
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError(
                    "Invalid markdown sytax, image section is not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TEXT_TYPE_TEXT))

            new_nodes.append(TextNode(image[0], TEXT_TYPE_IMAGE, image[1]))

            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TEXT_TYPE_TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TEXT_TYPE_TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        size = len(links)
        if size == 0:
            new_nodes.append(node)
            continue

        original_text = node.text
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)

            if len(sections) != 2:
                raise ValueError(
                    "Invalid markdown sytax, link section is not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TEXT_TYPE_TEXT))

            new_nodes.append(TextNode(link[0], TEXT_TYPE_LINK, link[1]))

            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TEXT_TYPE_TEXT))

    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TEXT_TYPE_TEXT)]
    nodes = split_nodes_delimiter(nodes,  "**", TEXT_TYPE_BOLD)
    nodes = split_nodes_delimiter(nodes,  "*", TEXT_TYPE_ITALIC)
    nodes = split_nodes_delimiter(nodes,  "`", TEXT_TYPE_CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
