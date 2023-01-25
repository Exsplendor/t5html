from t5htmllib.treebuilder import *

import pytest

def test_Tree_from_fail_on_wrong_input_type():
    with pytest.raises(Exception) as einfo:
        b = Tree_from('')
    with pytest.raises(Exception) as einfo:
        b = Tree_from(0)

    assert str(einfo.value).startswith("Can't parse source of type")

# vi: set et ts=4 ts=4 ai :
