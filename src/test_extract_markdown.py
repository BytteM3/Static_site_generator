import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links, extract_title
from blocktype import markdown_to_blocks

class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [beautiful link](https://somethingsomething.com/cool)"
        )
        self.assertListEqual([("beautiful link", "https://somethingsomething.com/cool")], matches)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_2(self):
        md = """

    This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

    - This is a list
- with items\n
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_extract_title(self):
        md = """
# Cool Title  

some nice text here
"""
        title = extract_title(md)
        self.assertEqual(title, "Cool Title")

    def test_extract_title_error(self):
        md = """
## Wrong Title

some wrong text
"""
        with self.assertRaises(Exception):
            extract_title(md)
