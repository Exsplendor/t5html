import pytest

from t5htmllib.parsers import *

class Test_Element_Id_Class_Separation:
    def test_element(s):
        f = separate_element_from_id_and_class
        assert f('ele') == ('ele', '', [])

    def test_element_id(s):
        f = separate_element_from_id_and_class
        assert f('ele#id') == ('ele', 'id', [])

    def test_element_id_cls(s):
        f = separate_element_from_id_and_class
        assert f('ele#id.cls') == ('ele', 'id', ['cls'])

    def test_element_cls(s):
        f = separate_element_from_id_and_class
        assert f('ele.cls') == ('ele', '', ['cls'])

    def test_element_id_2cls(s):
        f = separate_element_from_id_and_class
        assert f('ele#id.cls.cls') == ('ele', 'id', ['cls', 'cls'])

    def test_element_2cls(s):
        f = separate_element_from_id_and_class
        assert f('ele.cls.cls') == ('ele', '', ['cls', 'cls'])


class Test_Attribute_Conversion:
    def test_attr(s):
        pass


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


def test_element_parsing():
    """ only element parsing
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
        'tag attr="value"',
        'tag#id.cls.dls.els attr attr=ab attr=abc def attr=last',
        ]
    results = [
        'tag',
        'tag id="id"',
        'tag class="cls"',
        'tag id="id" class="cls"',
        'tag id="id" class="cls dls els"',
        'tag attr',
        'tag attr="value"',
        'tag attr="value"' ,
        'tag id="id" class="cls dls els" attr attr="ab" attr="abc def" attr="last"',
        ]
    for input, output in zip(lines, results):
        assert parse_element(input) == output
    

# vi: set et ts=4 ts=4 ai cc=78 nowrap :
