def markdown_to_blocks(markdown):
    blocks = []
    blocks = markdown.split("\n\n")

    blocks = list(map(lambda x: x.strip(), blocks))
    blocks = [block for block in blocks if block != ""]

    return blocks

