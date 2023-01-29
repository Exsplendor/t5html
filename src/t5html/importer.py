""" 
importer

helps to import additional files. 

ATM: only macro-definitions can be imported. The logic behind tree or partial
    tree imports is not resolved.

Examples:
=========

@@ file from path 
@@ file

"""
IMPLICIT_IMPORT_PATH = '~/.local/share/t5html'

from os import path

def path_from_import_string(s):
    """
    takes a import str (e.g.: @@ fname from path)
    returns a path-str
    """
    rm_head = lambda s: s.lstrip().lstrip('@@').lstrip()
    if not 'from' in s:
        return path.join(IMPLICIT_IMPORT_PATH, rm_head(s))
    fname, rest = rm_head(s).split('from', 1)
    fpath = rest.strip()
    return path.join(fpath, fname.strip())


def path_from_LineStructure(ls):
    """
    takes a LineStructure
    returns a path
    """
    if not (ls.cls == "import" and  ls.line.startswith('@@')):
        errortext = f"Not a vaild import at line {ls.nr}: {ls.line}"
        raise Exception(errortext)
    
    return path_from_import_string(ls.line)


def list_of_imports(lst):
    """
    takes a list of linestructures
    returns a list of pathnames
    """
    pfLS = path_from_LineStructure
    paths = [pfLS(ls) for ls in lst if ls.cls == 'import']
    return paths


def existing_imports(lst):
    """
    takes a list of pathnames
    returns a list of existing files
    """
    from os import getcwd
    print(getcwd())
    return [p for p in lst if path.isfile(p)]





if __name__ == '__main__':
    print("This file is meant to be imported, not to be executed.")


# vi: set et ts=4 ts=4 ai cc=78 rnu so=5 nuw=4:
