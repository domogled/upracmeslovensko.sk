
from pathlib import Path
from lxml import html as etree
from xml.sax.saxutils import unescape

import functools

HTML_DIR = Path(__file__).parents[2] / 'html'
TPL = HTML_DIR / 'templates'
TPL.mkdir(parents=True, exist_ok=True)

def parse(file):
    
    # je potřeb audělat si vlastní parser, jinak si vyláme zuby na neuzavřených elementech link

    parser = etree.HTMLParser(recover=True)
    tree = etree.parse(file, parser)

    return tree

def parse_template(file):
    str = Path(TPL / file)
    return etree.fragment_fromstring(str.read_text())

def str_element(element):
    if isinstance(element, etree.HtmlComment):
        return f"# COMMENT {element.text}"
    else:
        attributes = [f"{key}='{value}'" for key, value in element.attrib.items()]
        attributes = ' '.join(attributes)
        if attributes:
            attributes = f" {attributes}"
        return f"<{element.tag}{attributes}><!-- {len(element)} items text {element.text is not None} tail: {element.tail is not None} --> </{element.tag}>"


def tostring(element):
    # return etree.tostring(element, encoding='utf-8').decode()

    str = etree.tostring(element, encoding='utf-8', pretty_print=True)
    str = str.decode()
    return unescape(str)

def save_tpl(element, file_name):
    tpl_path = TPL / file_name

    tpl_content = tostring(element)

    tpl_path.write_text(tpl_content)

def move_to_tpl(element, file_name):

    parent = element.getparent()

    previous = element.getprevious()   

    php_script = f"<?php require '{file_name}'; ?>\n"

    if previous is not None:
        previous.tail = (previous.tail or '') + php_script
    else:
        parent.text = (parent.text or '') + php_script

    save_tpl(element, file_name)
    element.drop_tree()
    # parent.remove(element)
    

def open_and_exit(element, tpl_file):
    import webbrowser as browser

    print(tpl_file)
    print(str_element(element))
    url = f'http://localhost/upracmeslovensko.sk/src/html/templates/{tpl_file}'
    # print(url)
    browser.open_new_tab(url)
    exit()

def dmove_to_tpl(element, tpl_file):
    move_to_tpl(element, tpl_file)
    open_and_exit(element, tpl_file)

PREFIX = 'create_tpl_for_'

def tpl(function):
    
    @functools.wraps(function)
    def wrapper(element, write_other = None):
        if write_other is None:
            write_other = element

        print(function.__name__)

        for i, child in enumerate(element):
            print(f'#{i}: {str_element(child)}')
            function(i, child)

        name = function.__name__
        assert name.startswith(PREFIX)
        tpl_name = name[len(PREFIX):]
        print(tpl_name)
        tpl_file_name = f'{tpl_name}.php'
        save_tpl(write_other, tpl_file_name)
        
        
    return wrapper