from textnode import TextNode, TextType
from htmlnode import HTMLNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
        else:
            if delimiter in node.text:
                split_nodes = node.text.split(delimiter)
                if len(split_nodes) % 2 == 0:
                    raise Exception("delimiter not closed!")
                for i in range(len(split_nodes)):
                    if i % 2 == 0:
                        plain_node = TextNode(split_nodes[i], TextType.PLAIN)
                        new_nodes.append(plain_node)
                    else:
                        special_node = TextNode(split_nodes[i], text_type)
                        new_nodes.append(special_node)
            else:
                new_nodes.append(node)
    return new_nodes
