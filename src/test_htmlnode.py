import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="tag", value="value", children=[], props={"key": "value", "another_key": "huge_value"})
        result = node.props_to_html()
        expected = ' key="value" another_key="huge_value"'
        self.assertEqual(result, expected)

    def test_none_props(self):
            node = HTMLNode(tag="tag", value="value", children=[], props=None)
            result = node.props_to_html()
            expected = ""
            self.assertEqual(result, expected)

    def test_empty_props(self):
            node = HTMLNode(tag="tag", value="value", children=[], props={})
            result = node.props_to_html()
            expected = ""
            self.assertEqual(result, expected)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
          node = LeafNode("a", "Hello, world!", {"megakey": "what a key that was"})
          self.assertEqual(node.to_html(), '<a megakey="what a key that was">Hello, world!</a>')