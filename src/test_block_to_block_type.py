import unittest
from block_markdown import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_1(self):
        text = "# Heading 1"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "heading")

    def test_heading_2(self):
        text = "## Heading 2"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "heading")

    def test_code(self):
        text = "```This is a nice lil code block```"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "code")

    def test_quote(self):
        text = ">Quote time\n>cont"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "quote")

    def test_unordered_list(self):
        text = "- Brocolli\n - Tomato"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "unordered_list")

    def test_ordered_list(self):
        text = "1. Brocolli\n 2. Tomato"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "ordered_list")

    def test_paragraph(self):
        text = "Normal lil sweet sweet paragraph"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, "paragraph")
