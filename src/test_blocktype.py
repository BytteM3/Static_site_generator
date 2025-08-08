import unittest
from blocktype import BlockType, markdown_to_blocks, block_to_block

class TestBlockType(unittest.TestCase):
    def test_block_to_block(self):
        markdown = """
```
this_is_code(blahblah)
something = something_else
```

- This
- is
- a list

1. So
2. is
3. this
"""
        block_list = markdown_to_blocks(markdown)
        expected_types = [
            BlockType.CODE,
            BlockType.UNORDERED_LIST,
            BlockType.ORDERED_LIST
        ]
        for block, expected in zip(block_list, expected_types):
            result = block_to_block(block)
            assert result == expected, f"Block: {block!r} produced {result}, expected {expected}"