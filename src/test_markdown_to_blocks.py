import unittest

from block_markdown import markdown_to_blocks


class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):

        md = """This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line


        * This is a list
        * with items
        """
        final = ["This is **bolded** paragraph",
                 "This is another paragraph with *italic* text and `code` here\n        This is the same paragraph on a new line", "* This is a list\n        * with items"]

        self.assertEqual(markdown_to_blocks(md), final)

    def test_leading_ws_markdown_to_blocks(self):

        md = """      This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line


        * This is a list
        * with items
        """
        final = ["This is **bolded** paragraph",
                 "This is another paragraph with *italic* text and `code` here\n        This is the same paragraph on a new line", "* This is a list\n        * with items"]

        self.assertEqual(markdown_to_blocks(md), final)

    def test_markdown_with_new_lines__to_blocks(self):

        md = """This is **bolded** paragraph




















        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line















        * This is a list
        * with items
        """
        final = ["This is **bolded** paragraph",
                 "This is another paragraph with *italic* text and `code` here\n        This is the same paragraph on a new line", "* This is a list\n        * with items"]
        self.assertEqual(markdown_to_blocks(md), final)

    def test_markdown_broken_to_blocks(self):

        md = """This is **bolded** 
        paragraph
        This is another paragraph with *italic* 
        text and `code` here

        This is the same paragraph on a new line






        * This is a list
        * with 
        """
        final = ["This is **bolded** \n        paragraph\n        This is another paragraph with *italic* \n        text and `code` here",
                "This is the same paragraph on a new line", "* This is a list\n        * with"]
        self.assertEqual(markdown_to_blocks(md), final)
