import pytest

from t5htmllib.parsers import *


class Test_Element_Attr_Separation:
    """ 
    Split Elements/Tags with their id and class attributes from the other
    more specific attributes.
    """
    f = staticmethod(separate_element_from_attributes)
    def test_element(s):
        assert s.f('ele') == ('ele', '')

    def test_element_id(s):
        assert s.f('ele#id') == ('ele#id', '')

    def test_element_id_cls(s):
        assert s.f('ele#id.cls') == ('ele#id.cls', '')

    def test_element_cls(s):
        assert s.f('ele.cls') == ('ele.cls', '')

    def test_element_id_2cls(s):
        assert s.f('ele#id.cls.cls') == ('ele#id.cls.cls', '')

    def test_element_2cls(s):
        assert s.f('ele.cls.cls') == ('ele.cls.cls', '')


class Test_Element_Id_Class_Separation:
    """
    Check if there are besides the tag additional id and class attributes.
    """
    f = staticmethod(separate_element_from_id_and_class)
    def test_element(s):
        assert s.f('ele') == ('ele', '', [])

    def test_element_id(s):
        assert s.f('ele#id') == ('ele', 'id', [])

    def test_element_id_cls(s):
        assert s.f('ele#id.cls') == ('ele', 'id', ['cls'])

    def test_element_cls(s):
        assert s.f('ele.cls') == ('ele', '', ['cls'])

    def test_element_id_2cls(s):
        assert s.f('ele#id.cls.cls') == ('ele', 'id', ['cls', 'cls'])

    def test_element_2cls(s):
        assert s.f('ele.cls.cls') == ('ele', '', ['cls', 'cls'])


class Test_Attribute_Conversion:
    """
    Check for normal attribute-str to list conversion.
    """
    f = staticmethod(tuples_from_raw_attribute_str)
    def test_attr(s):
        assert s.f('attr') == [(None, 'attr')]
    
    def test_attr_val(s):
        assert s.f('attr=val') == [('attr', 'val')]
    
    def test_2attr(s):
        assert s.f('attr attr') == [(None, 'attr'), (None, 'attr')]

    def test_attr_val_attr(s):
        assert s.f('attr=val attr') == [('attr','val'), (None, 'attr')]

    def test_attr_val_x2(s):
        assert s.f('attr=val attr=val') == [('attr', 'val'), ('attr', 'val')]

    def test_attr_val_2x_quoted(s):
        assert s.f('attr="val" attr=val') == [('attr','val'), ('attr', 'val')]

    def test_attr_namespace(s):
        assert s.f('p:attr') == [(None, 'p:attr')]
    
    def test_attr_ns_val(s):
        assert s.f('p:attr=val') == [('p:attr', 'val')]
    
    def test_attr_text_assignment(s):
        assert s.f('attr="Some text"') == [('attr','Some text')]


class Test_String_From_Attribute_Tuples:
    """
    Check for normal attribute-str to list conversion.
    """
    f = staticmethod(string_from_attribute_tuples)
    def test_string_from_attribute_tuples(s):
        assert s.f([('attr', 'Some text')]) == 'attr="Some text"'

    def test_string_from_attribute_tuples_boolattr(s):
        assert s.f([(None, 'attr')]) == 'attr'

    def test_string_from_attribute_tuples_2boolattr(s):
        assert s.f([(None, 'attr'), (None, 'attr')]) == 'attr attr'

    def test_string_from_attribute_tuples_complex(s):
        _in = [("key", "value"), ("k", 'longer text'), (None, 'attr')]
        _out = 'key="value" k="longer text" attr'
        assert s.f(_in) == _out


@pytest.mark.skip('Marked for deletion. kept for teststrings atm')
def test_separate_element_from_attributes():
    """ expects (element, attributes)
    """
    lines = [
        'tag',
        'tag#id',
        'tag.cls',
        'tag#id.cls',
        'tag#id.cls',
        'tag#id.cls.dls.els',
        'tag attr',
        'tag attr=value',
        'tag#id.cls.dls.els attr attr=ab attr=abc def attr=last',
        ]
    results = [
        ('tag', ''),
        ('tag#id', ''),
        ('tag.cls', ''),
        ('tag#id.cls', ''),
        ('tag#id.cls', ''),
        ('tag#id.cls.dls.els', ''),
        ('tag', 'attr'),
        ('tag', 'attr=value'),
        ('tag#id.cls.dls.els', 'attr attr=ab attr=abc def attr=last'),
        ]
    for input, output in zip(lines, results):
        assert separate_element_from_attributes(input) == output


# vi: set et ts=4 ts=4 ai cc=78 nowrap nu so=5:
