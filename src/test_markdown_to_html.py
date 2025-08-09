import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unordered_list(self):
        md = """
Theres some **important** items here

- spooky item
- cool item
- crazy item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Theres some <b>important</b> items here</p><ul><li>spooky item</li><li>cool item</li><li>crazy item</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
Theres some _important_ items here

1. spooky item
2. cool item
3. crazy item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Theres some <i>important</i> items here</p><ol><li>spooky item</li><li>cool item</li><li>crazy item</li></ol></div>"
        )

    def test_heading(self):
        md = """
## section

Some very nice text is here,
some of it is even interesting
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>section</h2><p>Some very nice text is here, some of it is even interesting</p></div>"
        )