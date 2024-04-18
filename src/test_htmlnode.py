import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html(self):
        node = HTMLNode(tag="a",props={"href": "https://www.google.com"})
        to_html = node.props_to_html()
        self.assertEqual(to_html, " href='https://www.google.com'")

    def test_props_to_html(self):
        node = HTMLNode(tag="a",props={"href": "https://www.google.com", "target": "_blank"})
        to_html = node.props_to_html()
        self.assertEqual(to_html, " href='https://www.google.com' target='_blank'")

    def test_all_props_to_html(self):
        node = HTMLNode("p","This is a paragraph", None, props={'class': 'my-paragraph', 'id': 'para1', 'style': 'color: blue; font-size: 16px;'})
        to_html = node.props_to_html()
        self.assertEqual(to_html, " class='my-paragraph' id='para1' style='color: blue; font-size: 16px;'")

    def test_heading_props_to_html(self):
        node = HTMLNode(tag="h1",props={"class": "class1 class2", "style": "color:red"})
        to_html = node.props_to_html()
        self.assertEqual(to_html, " class='class1 class2' style='color:red'")

    def test_repr(self):
        node = HTMLNode(tag="a",props={"href": "https://www.google.com", "target": "_blank"})
        node_repr = node.__repr__()
        self.assertEqual(node_repr, "HTMLNode(a, None, None, {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_heading_repr(self):
        node = HTMLNode(tag="h1",props={"class": "class1 class2", "style": "color:red"})
        node_repr = node.__repr__()
        self.assertEqual(node_repr, "HTMLNode(h1, None, None, {'class': 'class1 class2', 'style': 'color:red'})")

    def test_all_repr(self):
        node = HTMLNode("p","This is a paragraph", None, props={'class': 'my-paragraph', 'id': 'para1', 'style': 'color: blue; font-size: 16px;'})
        node_repr = node.__repr__()
        self.assertEqual(node_repr, "HTMLNode(p, This is a paragraph, None, {'class': 'my-paragraph', 'id': 'para1', 'style': 'color: blue; font-size: 16px;'})")

if __name__ == "__main__":
    unittest.main()
