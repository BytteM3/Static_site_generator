from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


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
                    if split_nodes[i] == "":
                        continue
                    if i % 2 == 0:
                        plain_node = TextNode(split_nodes[i], TextType.PLAIN)
                        new_nodes.append(plain_node)
                    else:
                        special_node = TextNode(split_nodes[i], text_type)
                        new_nodes.append(special_node)
            else:
                new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.PLAIN:
            split_result = node_slice_img(node.text)
            new_nodes.extend(split_result)
        else:
            new_nodes.append(node)
    return new_nodes

def node_slice_img(text):
    img_props = extract_markdown_images(text)
    if not img_props:
        return [TextNode(text, TextType.PLAIN)]
    else:
        result = []
        delimiter = f"![{img_props[0][0]}]({img_props[0][1]})"
        sections = text.split(delimiter, 1)
        if sections[0]:
            result.append(TextNode(sections[0], TextType.PLAIN))
        result.append(TextNode(img_props[0][0], TextType.IMG, img_props[0][1]))
        if sections[1]:
            result.extend(node_slice_img(sections[1]))
    return result

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.PLAIN:
            split_result = node_slice_link(node.text)
            new_nodes.extend(split_result)
        else:
            new_nodes.append(node)
    return new_nodes

def node_slice_link(text):
    link_props = extract_markdown_links(text)
    if not link_props:
        return [TextNode(text, TextType.PLAIN)]
    else:
        result = []
        delimiter = f"[{link_props[0][0]}]({link_props[0][1]})"
        sections = text.split(delimiter, 1)
        if sections[0]:
            result.append(TextNode(sections[0], TextType.PLAIN))
        result.append(TextNode(link_props[0][0], TextType.LINK, link_props[0][1]))
        if sections[1]:
            result.extend(node_slice_link(sections[1]))
    return result

def text_to_textnodes(text):
    result = [TextNode(text, TextType.PLAIN)]
    result = split_nodes_delimiter(result, "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result