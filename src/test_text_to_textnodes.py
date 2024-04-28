import unittest
from inline_markdown import text_to_textnodes
from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TestTextToTextNodes(unittest.TestCase):
    def test_convert_all_texts_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        final = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]

        self.assertEqual(final, text_nodes)

    def test_convert_italic_and_bold_to_textnodes(self):
        text = "This is **text** with an *italic* word"
        text_nodes = text_to_textnodes(text)
        final = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ]

        self.assertEqual(final, text_nodes)

    def test_convert_bold_and_image_to_textnodes(self):
        text = "This is **text** with ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"
        text_nodes = text_to_textnodes(text)
        final = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with ", text_type_text),
            TextNode("image", text_type_image,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        ]

        self.assertEqual(final, text_nodes)

    def test_text_only_to_textnode(self):
        text = "This is text with "
        text_nodes = text_to_textnodes(text)
        final = [
            TextNode("This is text with ", text_type_text),
        ]

        self.assertEqual(final, text_nodes)

    def test_images_and_links_to_textnode(self):
        text = "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        final = [
            TextNode("image", text_type_image,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]

        self.assertEqual(final, text_nodes)
