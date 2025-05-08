import unittest
from block_markdown import markdown_to_blocks, BlockType, block_to_block_type
from markdown_html import markdown_to_html_node

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [   
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items"   
            ]
        )


    def test_markdown_to_blocks2(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [   
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items"   
            ]
        )


    def test_block_heading(self):
        block = block_to_block_type("# this is heading")
        self.assertEqual(block, BlockType.HEADING)

    def test_block_code(self):
        md = "```print('hello world')```"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.CODE)

    def test_block_quote(self):
        md = ">As you start to walk on the way,\n>the way appears\n>RUMI"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.QUOTE)

    def test_block_ul(self):
        md = "- banana\n- apple\n- milk\n- tea bags"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.UL)

    def test_block_ol(self):
        md = "1. banana\n2. apple\n3. milk\n4. tea bags"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.OL)

    def test_block_paragraph(self):
        md = "this is a paragraph"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.PARAGRAPH)

    def test_block_types(self):
        block = "## heading" 
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
 
        block = "```\ncode\n```" 
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        block = "> quote\n> more quote" 
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

        block = "- list\n- items" 
        self.assertEqual(block_to_block_type(block), BlockType.UL)

        block = "1. list\n2. items" 
        self.assertEqual(block_to_block_type(block), BlockType.OL)

        block = "paragraph" 
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_markdown_html1(self):
        md = md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        )


    def test_markdown_html2(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        )


    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>"
        )

    def test_paragraph2(self):
        md = """
This is **bolded** and _italic_ text
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> and <i>italic</i> text</p></div>"
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>"
        )

    def test_blockquote(self):
        md = """
> This is a 
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>"
        )

    def test_ul(self):
        md = """
- This is a list
- with items
- and _more_ items
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul></div>"
        )


    def test_ol(self):
        md = """
1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>"
        )

    def test_ul_ol(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>"   
        )
