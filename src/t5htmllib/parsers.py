import logging
logging.basicConfig(filename='parsers.debug.log', level=logging.DEBUG)
_D = logging.debug

def parse_element(line):
    """
    takes a line
    """
    element, attributes = separate_element_from_attributes(line)
    tag, _id, _cls = separate_element_from_id_and_class(element)


    reformated = "%s %s %s" %(tag, _id, attributes)
    normalized = reformated.strip()

    return normalized


def separate_element_from_id_and_class(element):
    """
    tales an element (e.g.: 'ele#id.cls.cls.cls') and
    returns a (element, id, [class,]) tuple
    """
    classes = [c for c in element.split('.') if '.' in element]
    element_id = classes.pop(0) if classes else element
    element, _id = element_id.split('#') if '#' in element_id else (element_id, '')

    return element, _id, classes


def separate_element_from_attributes(line):
    """
    takes a raw element-line (e.g.: 'ele#id.cls atr1 atr2=val') and
    returns tuple(element, attributes) (e.g.: ('ele#id.cls', 'atr1 atr2=val'))
    """
    element, attributes = line.split(' ', 1) if ' ' in line else (line, '')
    return element, attributes


# vi: set et ts=4 ts=4 ai cc=78 :

