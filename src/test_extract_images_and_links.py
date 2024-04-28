import unittest
from convert import extract_markdown_images, extract_markdown_links

class TestExtractingImagesAndLinks(unittest.TestCase):
    def test_extract_only_image(self):
        text = "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"
        link = ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")
        extracted_link = extract_markdown_images(text)
        self.assertEqual([link], extracted_link)

    def test_extract_one_image(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"
        link = ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")
        extracted_link = extract_markdown_images(text)
        self.assertEqual([link], extracted_link)

    def test_extract_two_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        links = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        extracted_link = extract_markdown_images(text)
        self.assertEqual(links, extracted_link)

    def test_extract_one_link(self):
        text = "This is text with a [link](https://www.example.com)"
        link = ("link", "https://www.example.com")
        extracted_link = extract_markdown_links(text)
        self.assertEqual([link], extracted_link)


    def test_extract_two_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        links = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        extracted_link = extract_markdown_links(text)
        self.assertEqual(links, extracted_link)
