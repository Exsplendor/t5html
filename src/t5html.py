#!/usr/bin/python3
"""
"""
from t5htmllib import lineparser as lp
from t5htmllib import elementparser as ep
from t5htmllib import treebuilder as tb

from pprint import pprint
example = """
## t5html

DOCTYPE := <!DOCTYPE html>

!! DOCTYPE

!! <-- This is
.. and html comment
.. over multiple lines -->

html
   head
   body
      div.id.cls1.cls2 attr1=value1 attr2="some quoted value"
         article.id > p > "textnode
            .. over multiple
            .. lines
            section
               p.id1 | p.id2 | p.id3
               p.id4 > "Text Node < p.id5
               p.id6
                  "Text Node
"""

def start():
    """
    entry point
    """
    lines = lp.parse_str(example)

    #pprint(lines)
    #print(lp.content_from_ls(lines))

    lines = tb.Tree_from(example)
    pprint(lines)


if __name__ == "__main__":
    start()


# vi: set et ts=4 ts=4 ai cc=78 nowrap nu so=5:
