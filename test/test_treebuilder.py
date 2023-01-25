from t5htmllib.treebuilder import *
from t5htmllib.lineparser import *


import pytest

@pytest.mark.parametrize("src, expected",
                            [('', "Can't parse source of type"),
                             (0, "Can't parse source of type"),
                             ([], "Can't parse source of type"),
                           ])
def test_Tree_from_exception_on_wrong_input_type(src, expected):
    with pytest.raises(Exception) as einfo:
        b = Tree_from(src)
    assert str(einfo.value).startswith(expected)

def test_Tree_from_exception_on_correct_input():
    b = Tree_from([LineStructure(0, '!! TEST', 'verbatim')])
    assert type(b) == list
    assert type(b[0]) == LineStructure

# vi: set et ts=4 ts=4 ai :
