from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    block_list = []
    for string in blocks:
        if string.strip("\n ") != "":
            string = string.strip("\n ")
            block_list.append(string)
    return block_list

def block_to_block(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    lines = block.split("\n")
    if lines[0] == "```" and lines[-1] == "```":
        return BlockType.CODE
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    if all(line.startswith(f"{index}. ") for index, line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    
