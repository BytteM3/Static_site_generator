import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )
    
    def test_to_html_with_grandchildren_and_props(self):
         grandchild_node = LeafNode("b", "grandchild")
         child_node = ParentNode("span", [grandchild_node])
         parent_node = ParentNode("div", [child_node], {"superkey": "amazing key!"})
         self.assertEqual(
              parent_node.to_html(),
              '<div superkey="amazing key!"><span><b>grandchild</b></span></div>'
         )

    def test_to_html_no_children(self):
         child_node = ParentNode("span", "interesting text")
         parent_node = ParentNode("div", [], {"superkey": "amazing key!"})
         with self.assertRaises(ValueError):
              parent_node.to_html()