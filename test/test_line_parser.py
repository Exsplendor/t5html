from t5htmllib.lineparser import *

import pytest
from textwrap import dedent


class TestLineClassifiers:
    def test_classify_comment_line(s):
        assert classify_line('## Some comment') == "comment"

    def test_classify_continue_line(s):
        assert classify_line('.. follow up') == "continue"

    def test_classify_verbatim_line(s):
        assert classify_line('!! <!- html comment -->') == "verbatim"
        
    def test_classify_normal_line(s):
        assert classify_line('      div#gallery.blog') == "normal"

    def test_classify_import_line(s):
        assert classify_line('@ path/to/file') == "import"


def test_indent_level():
    assert get_indent_level('') == 0
    assert get_indent_level(' '*3) == 1
    assert get_indent_level(' '*6) == 2
    # test for int:
    assert get_indent_level(' '*7) == 2
    assert get_indent_level('\t'*2) ==0


class TestLineParsing:
    """
    # t5html

    HTML5 := <!DOCTYPE html>
    !! HTML5
    @@ file from src

    html
       head
          title > "t5html example
       body
       header | nav
       main
          article
             section
                "text node
                .. over multiple line
          article
             section
    """
    def setup_class(c):
        c._html = dedent(c.__doc__)

    def test_doc_as_text(s):
        assert '# t5html' in s._html

    def test_indentation(s):
        body = [l for l in s._html.splitlines() if 'body' in l][0]
        title = [l for l in s._html.splitlines() if 'title' in l][0]
        assert 'body' in body and get_indent_level(body) == 1
        assert 'title' in title and get_indent_level(title) == 2

    def test_classify_lines(s):
        b, c, n, m, v, i, cc, t =\
        "blank comment normal macro verbatim import continue text".split()
        manual = enumerate([b,c,b,m,v,i,b,*(n,)*8,t,cc,n,n])
        auto = enumerate(map(classify_line, s._html.splitlines()))
        assert list(auto) == list(manual)

# vi: set et ts=4 ts=4 ai cc=78 nowrap nu so=5:
