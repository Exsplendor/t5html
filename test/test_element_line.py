import pytest

from t5htmllib.parsers import *


class Test_Element_Attr_Separation:
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
    f = staticmethod(split_attributes)
    def test_attr(s):
        assert s.f('attr') == ['attr']


@pytest.mark.skip(reason='Marked for deletion. kept for teststrings atm')
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


# vi: set et ts=4 ts=4 ai cc=78 nowrap :
