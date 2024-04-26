import re
from textnode import TextNode
from convert import extract_markdown_images, extract_markdown_links


TEXT_TYPE_TEXT = "text"
TEXT_TYPE_BOLD = "bold"
TEXT_TYPE_ITALIC = "italic"
TEXT_TYPE_CODE = "code"
TEXT_TYPE_LINK = "link"
TEXT_TYPE_IMAGE = "image"

#    r"!\[(.*?)\]\((.*?)\)"


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
