import unittest

from convert import split_nodes_delimiter
from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TestSplitDelimiter(unittest.TestCase):
    def test_code_block_split(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, result)

    def test_multiple_code_block_split(self):
        node = TextNode("This is text with a `code block` word and `another code block` word.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word and ", text_type_text),
            TextNode("another code block", text_type_code),
            TextNode(" word.", text_type_text),
        ]
        self.assertEqual(new_nodes, result)

    def test_italic_split(self):
        node = TextNode("This is text with a *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, result)

    def test_multiple_italic_split(self):
        node = TextNode("This is text with a *italic* word and *another italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and ", text_type_text),
            TextNode("another italic", text_type_italic),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, result)

    def test_bold_split(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, result)

    def test_multiple_bold_split(self):
        node = TextNode("This is text with a **bold** word and yet **another bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word and yet ", text_type_text),
            TextNode("another bold", text_type_bold),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, result)

