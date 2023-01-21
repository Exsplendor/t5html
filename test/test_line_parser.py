import pytest

from t5htmllib.lineparser import *

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

    DOCTYPE := <!DOCTYPE html>

    !! DOCTYPE
    @@ file from src

    """

# vi: set et ts=4 ts=4 ai cc=78 nowrap nu so=5:
