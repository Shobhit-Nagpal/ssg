import re
from inline_markdown import text_to_textnodes,text_node_to_html_node
from htmlnode import ParentNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ordered_list = "ordered_list"
block_type_unordered_list = "unordered_list"


def markdown_to_blocks(markdown):
    blocks = []
    blocks = markdown.split("\n\n")

    blocks = list(map(lambda x: x.strip(), blocks))
    blocks = [block for block in blocks if block != ""]

    return blocks


def block_to_block_type(block):

    heading_pattern = re.compile(r"^##?#?#?#?#?\s.*$")
    quote_pattern = re.compile(r"^>.*$", re.MULTILINE)
    unordered_list_pattern = re.compile(r"^[*-]\s.*$", re.MULTILINE)
    ordered_list_pattern = re.compile(r"^(1|[2-9]\d*)\.\s.*$", re.MULTILINE)
    code_pattern = re.compile(r"^```[\s\S]*?```$")

    if heading_pattern.search(block):
        return block_type_heading
    elif quote_pattern.search(block):
        return block_type_quote
    elif unordered_list_pattern.search(block):
        return block_type_unordered_list
    elif ordered_list_pattern.search(block):
        return block_type_ordered_list
    elif code_pattern.search(block):
        return block_type_code
    else:
        return block_type_paragraph

def markdown_to_html_node(markdown):
    html = "<div>" 
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case "heading":
                html = html + create_html_heading(block)
            case "paragraph":
                html = html + create_html_paragraph(block)
            case "quote":
                html = html + create_html_quote(block)
            case "code":
                html = html + create_html_code(block)
            case "ordered_list":
                html = html + create_html_ordered_list(block)
            case "unordered_list":
                html = html + create_html_unordered_list(block)
            case _:
                raise ValueError("Block type not recognized")

    html = html + "</div>"
    return html 

def create_html_heading(block):

    content = block.split(" ", 1)

    heading_number = len(content[0])

    text_nodes = text_to_textnodes(content[1])
    leaf_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
    heading_value = ""
    for leaf_node in leaf_nodes:
        heading_value = heading_value + leaf_node.to_html()

    heading = f"<h{heading_number}>"
    heading = heading + heading_value + f"</h{heading_number}>"
    return heading

def create_html_paragraph(block):
    paragraph_value = ""

    text_nodes = text_to_textnodes(block)
    leaf_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]

    for leaf_node in leaf_nodes:
        paragraph_value = paragraph_value + leaf_node.to_html()

    return "<p>" + paragraph_value + "</p>"

def create_html_quote(block):
    contents = block.split("\n")
    quote_blocks = []
    for content in contents:
        quote_blocks.append(content.split(">")[1])

    quote_value = ""
    for block in quote_blocks:
        quote_value = quote_value + block + "\n"

    quote = "<blockquote>"
    quote = quote + quote_value + "</blockquote>"
    return quote

def create_html_code(block):
    code_value = ""
    text_nodes = text_to_textnodes(block)
    text_nodes.pop(len(text_nodes)-1)
    text_nodes.pop(0)
    leaf_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]


    for leaf_node in leaf_nodes:
        code_value = code_value + leaf_node.to_html()

    code = "<pre>"
    code = code + code_value.strip() + "</pre>"
    return code

def create_html_ordered_list(block):
    items = block.split("\n")

    ol = "<ol>"

    for item in items:
        content = item.split(" ", 1)
        list_value = ""
        text_nodes = text_to_textnodes(content[1])
        leaf_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]

        for leaf_node in leaf_nodes:
            list_value = list_value + leaf_node.to_html()

        ol = ol + f"<li>{list_value}</li>"

    ol = ol + "</ol>"
    return ol

def create_html_unordered_list(block):
    items = block.split("\n")
    ul = "<ul>"

    for item in items:
        content = item.split(" ", 1)
        list_value = ""
        text_nodes = text_to_textnodes(content[1])
        leaf_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]

        for leaf_node in leaf_nodes:
            list_value = list_value + leaf_node.to_html()

        ul = ul + f"<li>{list_value}</li>"
    ul = ul + "</ul>"
    return ul


def extract_title(markdown):
    title = markdown.split("\n")[0]
    title_content = title.split(" ", 1)
    heading_number = len(title_content[0])

    if block_to_block_type(title) != "heading" or heading_number != 1:
        raise Exception("Invalid heading at beginning. Make sure first line is heading 1")

    title_text = title_content[1]
    return title_text


def generate_page(from_path, template_path, dest_path):
    print(f"Generating path from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown = file.read()

    with open(template_path, "r") as file:
        template = file.read()

    html_title = extract_title(markdown)
    html_content = markdown_to_html_node(markdown)

    template = template.replace("{{ Title }}", html_title)
    template = template.replace("{{ Content }}", html_content)
    
    with open(dest_path, "w") as file:
        file.write(template)

