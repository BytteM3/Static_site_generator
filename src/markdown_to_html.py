import re
from blocktype import BlockType, markdown_to_blocks, block_to_block
from htmlnode import HTMLNode, ParentNode, LeafNode
from textsplit import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block(block)
        children.append(block_to_htmlnode(block, block_type))
    return ParentNode("div", children=children)



def block_to_htmlnode(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        text = " ".join(block.split("\n"))
        children = text_to_children(text)
        return ParentNode("p", children=children)
    elif block_type == BlockType.HEADING:
        level = len(block) - len(block.lstrip("#"))
        text = block[level+1:].strip()
        return ParentNode(f"h{str(level)}", children=text_to_children(text))
    elif block_type == BlockType.UNORDERED_LIST:
        lines = block.split("\n")
        children = []
        for line in lines:
            line_children = text_to_children(line.lstrip("- ").strip())
            children.append(ParentNode("li", children=line_children))
        return ParentNode("ul", children=children)
    elif block_type == BlockType.ORDERED_LIST:
        lines = block.split("\n")
        children = []
        for line in lines:
            line_text = re.sub(r"^\d+\.\s*", "", line)
            line_children = text_to_children(line_text.strip())
            children.append(ParentNode("li", children=line_children))
        return ParentNode("ol", children=children)
    elif block_type == BlockType.QUOTE:
        lines = block.split("\n")
        clean_lines = [line.lstrip("> ").strip() for line in lines]
        text = " ".join(clean_lines)
        children = text_to_children(text)
        return ParentNode("blockquote", children=children)
    elif block_type == BlockType.CODE:
        lines = block.split("\n")
        code_lines = lines[1:-1]
        code_text = "\n".join(code_lines) + "\n"
        child_node = LeafNode("code", value=code_text)
        return ParentNode("pre", children=[child_node])

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes