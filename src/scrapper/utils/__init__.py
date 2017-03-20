
from pathlib import Path
from lxml import html as etree
from xml.sax.saxutils import unescape

import functools

HTML_DIR = Path(__file__).parents[2] / 'html'
TPL = HTML_DIR / 'templates'

from db.texty_preklad import collection as db_texty

def find_tree(element):
    for child in element:
        yield child
        for sub in find_tree(child):
            yield sub



def dej_metatexty(el):
    
    for meta in el.head.findall('meta'):
        # assert 'value' in meta.attrib
        
        assert(len(meta.attrib) == 2 or len(meta.attrib) == 1)
        if(len(meta.attrib) == 1):
            # print(meta.attrib.keys())
            continue

        content = meta.attrib['content']

        def occurrence():
            keys = meta.attrib.keys()
            for key in ['property', 'name']:
                if key in keys:
                    return f'{key}::{meta.attrib[key]}'
            return 'UNKNOWN'
    

        _key = f'META {occurrence()}'.replace(' ', '_')

        try:
            doc = db_texty.fetchDocument(_key)
        except KeyError as e:
            doc = db_texty.createDocument({'_key': _key})
            # doc['_key'] = _key

        doc['cs_CZ'] = content
        doc['sk'] = ''
        print(doc)
        doc.save()
        # entry = (
        #     msgid=content,
        #     msgstr='',
        #     # occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
        #     occurrences=[(f'{occurrence()}', '0')]
        # )

        meta.attrib['content'] = f'<?php echo _("{content}"); ?>'
        print(meta.attrib.keys())
        print(str_element(meta))


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
    tpl_path.parent.mkdir(parents=True, exist_ok=True)

    tpl_content = tostring(element)

    tpl_path.write_text(tpl_content)

def move_to_tpl(element, file_name, require = True):

    parent = element.getparent()

    previous = element.getprevious()   
    
    php_script = f"<?php {'' if require else '// '}require '{file_name}'; ?>\n"
    # print("php_script = ", php_script)
    
    if previous is not None:
        previous.tail = (previous.tail or '') + php_script
        # print("previous.tail = ", previous.tail)
    else:
            
        parent.text = (parent.text or '') + php_script
        # print("parent.text = ", parent.text)
            

    save_tpl(element, file_name)
    element.drop_tree()
    # parent.remove(element)
    

def open_and_exit(element, tpl_file):
    import webbrowser as browser

    print(tpl_file)
    print(str_element(element))
    url = f'http://upracmeslovensko.dev/templates/{tpl_file}'
    # print(url)
    browser.open_new_tab(url)
    exit()

def dmove_to_tpl(element, tpl_file):
    move_to_tpl(element, tpl_file)
    open_and_exit(element, tpl_file)

