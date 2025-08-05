import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from textsplit import split_nodes_delimiter, split_nodes_link, split_nodes_image


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

    def test_delimiter_split_bold(self):
        nodes = [
            TextNode("I have a lot of text and **some of it** is bold", TextType.PLAIN),
            TextNode("I have none of the bold text", TextType.PLAIN),
            TextNode("Im very bold", TextType.BOLD)
        ]
        processed = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(
            processed,
            [TextNode("I have a lot of text and ", TextType.PLAIN),
             TextNode("some of it", TextType.BOLD),
             TextNode(" is bold", TextType.PLAIN),
             TextNode("I have none of the bold text", TextType.PLAIN),
             TextNode("Im very bold", TextType.BOLD)
             ]
        )
    def test_delimiter_split_italic(self):
        nodes = [
            TextNode("I have a lot of text and _some of it_ is italic", TextType.PLAIN),
            TextNode("I have none of the italic text", TextType.PLAIN),
            TextNode("Im so italic its stupid", TextType.ITALIC)
        ]
        processed = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(
            processed,
            [TextNode("I have a lot of text and ", TextType.PLAIN),
             TextNode("some of it", TextType.ITALIC),
             TextNode(" is italic", TextType.PLAIN),
             TextNode("I have none of the italic text", TextType.PLAIN),
             TextNode("Im so italic its stupid", TextType.ITALIC)
             ]
        )
    
    def test_delimiter_split_code(self):
        nodes = [
            TextNode("I have a lot of text and `some of it` is code", TextType.PLAIN),
            TextNode("I have none of the code", TextType.PLAIN),
            TextNode("Im all code", TextType.CODE)
        ]
        processed = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(
            processed,
            [TextNode("I have a lot of text and ", TextType.PLAIN),
             TextNode("some of it", TextType.CODE),
             TextNode(" is code", TextType.PLAIN),
             TextNode("I have none of the code", TextType.PLAIN),
             TextNode("Im all code", TextType.CODE)
             ]
        )
    
    def test_delimiter_exception(self):
        nodes = [
            TextNode("I have a lot of text and `some of it is code", TextType.PLAIN),
            TextNode("I have none of the code", TextType.PLAIN),
            TextNode("Im all code", TextType.CODE)
        ]
        with self.assertRaises(Exception):
            split_nodes_delimiter(nodes, "`", TextType.CODE)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMG, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMG, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [serious link](https://importantbussiness.com/huge) and another [second link](https://trivialstuff.com/nonsense)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("serious link", TextType.LINK, "https://importantbussiness.com/huge"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second link", TextType.LINK, "https://trivialstuff.com/nonsense"
                ),
            ],
            new_nodes,
        )
if __name__ == "__main__":
    unittest.main()