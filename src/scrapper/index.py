#!/usr/bin/env python3

from utils import *

from parser.index import create_tpl_for_body

from utils.retrieve_content import retrieve_content

URL_UKLIDME_CESKO_INDEX = 'http://www.uklidmecesko.cz/index.html'

def main():
    print('*'*45, f'PARSE URL {URL_UKLIDME_CESKO_INDEX}', sep = '\n')
    tree = parse(URL_UKLIDME_CESKO_INDEX)
            
    root = tree.getroot()

    body = root.find('body')
    # print(body)

    assert len(body) == 6

    from shutil import rmtree
    #~ if HTML_DIR.is_dir():
        #~ print(f'mažu {HTML_DIR}')
        #~ rmtree(HTML_DIR)

    HTML_DIR.mkdir(parents=True, exist_ok = True)

    print('RETRIEVE CONTENT DISABLED')
    #~ retrieve_content(root, HTML_DIR)

    dej_metatexty(body)
    root.text = '<?php require(__dir__ . "/../lib/locale.php"); ?>'

    #~ načtu odkazy
    # odkazy = body.findall('a')
    # print(odkazy)

    # for odkaz in [el for el in find_tree(body) if el.tag == 'a']:
    #     print(odkaz)



    #~ rozparsuji na šablony, abych si je mohl vypínat
    for i, child in enumerate(body):
        # print(f'#{i}: {str_element(child)}')
        create_tpl_for_body(i, child)

    save_tpl(root, 'main.php')

    # vycisti(root)
    

# nejprve vyčistím od bílého místa

def vycisti(el):
    if el.text is not None:
        el.text = el.text.strip()

    if el.tail is not None:
        el.tail = el.tail.strip()

    for child in el:
        vycisti(child)


if __name__ == "__main__":
    
    main()

    
