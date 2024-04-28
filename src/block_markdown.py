import re

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
    code_pattern = re.compile(r"^```.*```$")

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
    heading = f"<h{heading_number}>"
    heading = heading + content[1] + f"</h{heading_number}>"
    return heading

def create_html_paragraph(block):
    return "<p>" + block + "</p>"

def create_html_quote(block):
    quote = "<blockquote>"
    # add quote
    quote = quote + "</blockquote>"
    return quote

def create_html_code(block):
    content = block.split("```")
    code = "<pre><code>"
    code = code + content[1] + "</code></pre>"
    return code

def create_html_ordered_list(block):
    items = block.split("\n")
    ol = "<ol>"

    for item in items:
        content = item.split(" ", 1)
        li = f"<li>{content[1]}</li>"
        ol = ol + li

    ol = ol + "</ol>"
    return ol

def create_html_unordered_list(block):
    items = block.split("\n")
    ul = "<ul>"

    for item in items:
        content = item.split(" ", 1)
        li = f"<li>{content[1]}</li>"
        ul = ul + li

    ul = ul + "</ul>"
    return ul
