""" 
TreeBuilder

Creates a HTML-File from a t5html formatted file.
Utilizes the lineparser and elementparser modules.

Example:

    html = html_from_t5html(rawstr)

"""

from t5htmllib import lineparser as lp
from t5htmllib import elementparser as ep

import sys
from collections import namedtuple

TreeElement = namedtuple("TreeElement", "level type value orig_lnr")


def build_from_str(t5htmlstr):
    """
    takes a rawstr in t5html-format
    returns a list of LineStructures
    """
    return lp.parse_str(t5htmlstr)


def LineStructureFactory(src):
    """
    takes either a string or a list of LineStructures
    returns a list of LineStructures

    basically ensures that we have LineStructures independently if we are 
    fed a string in t5html format or already a converted list of
    LineStructures.
    """
    if type(src) == str:
        return build_from_str(src)
    elif type(src) == list and src and type(src[0]) == lp.LineStructure:
        # non empty list (`and src`) with 1st item of type LineStructure
        return src


def pseudoAST_from(structured_lines):
    """
    tales a list of linestructures
    retruns a pseudoast
    """
    return [ TreeElement(
                lp.get_indent_level(line.line),
                line.cls,
                line.line.lstrip(),
                line.nr) for line in structured_lines]


def Tree_from(src):
    """
    takes an input 
    returns a pseudo-ast 
    """
    structured_lines = LineStructureFactory(src)
    if not structured_lines:
        # probably better in LineStructureFactory. E.g.: if there's a list of
        # non LineStructures, to differentiate from a valid LineStructures-List
        raise Exception("Can't parse source of type: %s." % type(src))
    ast = pseudoAST_from(structured_lines)

    tree = []
    for element in ast:
        pass

    return structured_lines
    

if __name__ == '__main__':
    print("This file is meant to be imported, not to be executed.")


# vi: set et ts=4 ts=4 ai cc=78 rnu so=5 nuw=4:
