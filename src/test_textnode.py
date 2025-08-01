import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()