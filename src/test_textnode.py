import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This node is not ok", TextType.ITALIC)
        node2 = TextNode("This node is ok", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_present(self):
        node = TextNode("I have a URL", TextType.IMG, "somerandomurl")
        node2 = TextNode("Me too!", TextType.IMG, "alsourl")
        self.assertIsNotNone(node.url, node2.url)

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_bold(self):
        node = TextNode("bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")

    def test_text_node_link(self):
        node = TextNode("click me", TextType.LINK, "https://testssuck.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "click me")
        self.assertEqual(html_node.props["href"], "https://testssuck.com")

    def test_text_node_image(self):
        node = TextNode("alt text", TextType.IMG, "image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "image.jpg")
        self.assertEqual(html_node.props["alt"], "alt text")


if __name__ == "__main__":
    unittest.main()