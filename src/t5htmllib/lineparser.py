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
from collections import namedtuple, OrderedDict


RawLine = namedtuple('RawLine', 'nr line')
ClassifiedLine = namedtuple('ClassifiedLine', 'nr line cls')

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
    # TODO: we don't handle indentation errors, atm!
    level = int(count / 3)
    return level


def RawLines_from_str(text):
    """
    takes a string 
    returns a RawLineStructure [(nr, line), ...]
    """
    rls = [RawLine(n, l.rstrip())
            for n, l in enumerate(text.splitlines())]
    return rls


def ClassifiedLines_from_RawLines(rls):
    """
    tales a RawLinesStructure 
    returns a ClassifiedLinesStructure
    """
    cls = [ClassifiedLine(n, l, classify_line(l))
            for n, l in rls]
    return cls


def sanitized_ClassifiedLines(cls):
    """
    takes a ClassifiedLineStructure
    returns a CLS without blanks and comments
    """
    sls = [t for t in cls if t.cls not in ('comment', 'blank')]
    return sls


def split_by_classifier(cls, clsname):
    """
    takes a ClassifiedLinesStructure 
    returns a split by named classifier
    """
    extracted = [t for t in cls if t.cls == clsname] or []
    rest = [t for t in cls if not t.cls == clsname]
    return extracted, rest


def split_macros(scls):
    """
    takes a ClassifiedLinesStructure
    returns two lists: (macros, scls without macros)
    """
    return split_by_classifier(scls, 'macro')
    

def split_imports(scls):
    """
    takes a ClassifiedLinesStructure
    returns two lists: (imports, scls without imports)
    """
    return split_by_classifier(scls, 'import')
    

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


def MacroDef_from_ClassifiedLines(cls):
    """
    takes classifiedLines
    returns a OrderedDict of MacorKey: MacroValue
    """
    macrodef = OrderedDict()
    for m in cls:
        k, v = m.line.split(' := ')
        macrodef[k] = v
    return macrodef
    

    



if __name__ == '__main__':
    print("This file is meant to be imported, not to be executed.")


# vi: set et ts=4 ts=4 ai cc=78 rnu so=5 nuw=4:
