import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html_without_tag(self):
        """Test to_html method when no tag is provided."""
        node = LeafNode(value="Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_to_html_with_tag(self):
        """Test to_html method with tag and properties."""
        props = {"class": "highlight"}
        node = LeafNode(tag="span", value="Highlighted", props=props)
        self.assertEqual(node.to_html(), "<span class='highlight'>Highlighted</span>")

    def test_to_html_raises_exception_on_no_value(self):
        """Test that to_html raises ValueError if value is None."""
        node = LeafNode(tag="p")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_html_output_complex(self):
        """Test complex HTML generation."""
        props = {"class": "new", "id": "unique"}
        node = LeafNode(tag="div", value="Complex content", props=props)
        self.assertEqual(node.to_html(), "<div class='new' id='unique'>Complex content</div>")

if __name__ == '__main__':
    unittest.main()
