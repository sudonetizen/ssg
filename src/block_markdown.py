from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"

def markdown_to_blocks(md):
    blocks = []
    for block in md.split("\n\n"):
        block = block.strip()
        if block:
            blocks.append(block)
    return blocks

def block_to_block_type(md):
    # heading
    if md.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")): return BlockType.HEADING

    # code
    if md.startswith("```") and md.endswith("```"): return BlockType.CODE

    # quote
    lines = md.split("\n"); q_counter = 0
    for line in lines:
        if line.startswith(">"): q_counter += 1
    if len(lines) == q_counter: return BlockType.QUOTE

    # unordered list
    lines = md.split("\n"); ul_counter = 0
    for line in lines:
        if line.startswith("- "): ul_counter += 1
    if len(lines) == ul_counter: return BlockType.UL

    # ordered list
    lines = md.split("\n"); ol_counter = 0
    for ix, line in enumerate(lines):
        if line.startswith(f"{ix+1}. "): ol_counter += 1
    if len(lines) == ol_counter: return BlockType.OL

    # paragraph
#    lines = md.split("\n"); p_counter = 0
#    for line in lines:
#        if line[0].isalpha() and line[-1].isalpha(): p_counter += 1
#    if len(lines) == p_counter: return BlockType.PARAGRAPH
    return BlockType.PARAGRAPH

