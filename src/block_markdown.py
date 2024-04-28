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

