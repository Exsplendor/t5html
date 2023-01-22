""" 
LineParser

Contains the functions to process t5html files.

Example:

    Start of line symbols:

        # comment
        ! verbatim line
        @ import file
        MACRONAME := macro definition / text
        .. line continuation
    
    Inline symbols:

        > indent
        < dedent
        | keep level (sibling element to previous element)
        " text-node

"""
import logging as _L
_L.basicConfig(filename='/tmp/lineparser.log')


# read lines
# remove comments and empty lines
# extract macro and import lines
# ignore verbatim lines
# expand macros (therefore macros could contain reformating symbols)
# concatenate/split inline > < and | smybols


def get_indent_level(line):
    """
    takes a line 
    returns a number representing the indentation-level
    
    Because of the line-continuation symbol beeing two dots followed
    by a space, the *reasonable* indentation seems to be 3.
    """
    # explicit only normal whitespaces! no tabs, etc.
    count = len(line) - len(line.lstrip(' '))
    level = count / 3
    if type(level) == float:
        _L.warning("indentation whacky")
    return int(level)


def classify_line(line):
    """
    takes a str representing a line
    returns a string classifying the type of line
    """
    l = line.strip()
    # single classifier allowed:
    if l == '': return 'blank'

    if l.startswith('#'): return "comment"
    if l.startswith('!'): return "verbatim"
    if l.startswith('@'): return "import"
    if l.startswith('"'): return "text"

    # has to be a double-classifier
    if l.startswith('..'): return "continue"
    if ' := ' in l and l.split(' := ', 1)[0].isupper():
        return 'macro'

    return "normal"

def remove_lines(lines):
    """
    """


if __name__ == '__main__':
    print("This file is meant to be imported, not to be executed.")


# vi: set et ts=4 ts=4 ai cc=78 rnu so=5 nuw=4:
