import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_simple_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        html = node.to_html()
        self.assertEqual(html, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_nested_element_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode("div", [
                    LeafNode("p", "Complex content", {"class": "new", "id": "unique"})
                    ]),
                LeafNode("i", "italic text"),
            ],
        )

        html = node.to_html()
        self.assertEqual(html, "<p><b>Bold text</b><div><p class='new' id='unique'>Complex content</p></div><i>italic text</i></p>")

    def test_complex_nested_element_to_html(self):
        node = ParentNode(
            "div",
            [
                LeafNode("h1", "Heading 1"),
                ParentNode(
                    "section",
                    [
                        LeafNode("h2", "Heading 2"),
                        ParentNode(
                            "article",
                            [
                                LeafNode("p", "Paragraph 1"),
                                ParentNode(
                                    "ul",
                                    [
                                        ParentNode(
                                            "li",
                                            [
                                                LeafNode("b", "Bold text"),
                                                LeafNode("i", "Italic text"),
                                            ],
                                        ),
                                        ParentNode(
                                            "li",
                                            [
                                                LeafNode("code", "print('Hello, World!')"),
                                            ],
                                        ),
                                    ],
                                ),
                                ParentNode(
                                    "div",
                                    [
                                        LeafNode(
                                            "p",
                                            "Complex content",
                                            {"class": "new", "id": "unique"},
                                        )
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                ParentNode(
                    "footer",
                    [
                        LeafNode("p", "Footer text"),
                    ],
                ),
            ],
        )

        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><section><h2>Heading 2</h2><article><p>Paragraph 1</p><ul><li><b>Bold text</b><i>Italic text</i></li><li><code>print('Hello, World!')</code></li></ul><div><p class='new' id='unique'>Complex content</p></div></article></section><footer><p>Footer text</p></footer></div>",
        )
