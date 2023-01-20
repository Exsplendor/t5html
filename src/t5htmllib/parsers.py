import logging
logging.basicConfig(filename='parsers.debug.log', level=logging.DEBUG)
_D = logging.debug

def parse_element(line):
    """
    takes a raw-line and
    returns a formatted line 
    """
    element, attributes = separate_element_from_attributes(line)
    es = separate_element_from_id_and_class(element)

    reformated = stringify_ElementStructure(es)
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


def tuples_from_raw_attribute_str(attribute_str):
    """
    takes a string of attributes and 
    returns a list of attribute-tuples
    """
    # There are three possible 'words':
    #   1. standalone attributes (aka bool. attr), 2a. simple assignments (key=value), 
    #   2b. text assignments (key="quoted longer text")

    words = attribute_str.split()
    next_word_belongs_to_last_value = False
    attributes = []

    for word in words:

        if next_word_belongs_to_last_value:

            # remove last (key, value) pair and add current word to value
            # reappend and get next word
            
            (key, value) = attributes.pop()
            if word.endswith('"'):
                next_word_belongs_to_last_value = False
            value += ' ' + word.strip('"')
            attr = (key, value)
            
            attributes.append(attr)
            continue

        is_assignment = '=' in word
        if is_assignment:
            key, value = word.split('=')
            if value.startswith('"') and not value.endswith('"'):
                next_word_belongs_to_last_value = True
            attr = key, value.strip('"')
        else:
            # boolean attribute
            attr = (None, word)

        attributes.append(attr)

    return attributes


def stringify_AttributeStructure(attrlst):
    """
    takes a list of attribute tuples (key, value) or (None, boolean-attr) and
    returns a string

    """
    reformated = [f'{key}="{value}"' if key else f'{value}' for (key, value) in attrlst]
    return ' '.join(reformated)


def stringify_ElementStructure(es):
    """
    takes a element tuple (tag, id, [classes]) and
    returns a string
    """
    (tag, _id, classes) = es
    return f'{tag} id={_id} class="{" ".join(classes)}"' 


# vi: set et ts=4 ts=4 ai cc=78 rnu so=5 nuw=4:
