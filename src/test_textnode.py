import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", "bold", "https://www.shobhitnagpal.com")
        node2 = TextNode("This is a text node", "bold", "https://www.shobhitnagpal.com")
        self.assertEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
    
    def test_text_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.shobhitnagpal.com")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "https://www.shobhitnagpal.com")
        repr = node.__repr__()
        self.assertEqual(repr, "TextNode(This is a text node, bold, https://www.shobhitnagpal.com)")

if __name__ == "__main__":
    unittest.main()
