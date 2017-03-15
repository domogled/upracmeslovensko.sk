#!/usr/bin/env python3


from utils import *

from index_tpl import create_tpl_for_content

from retrieve_content import retrieve_content


def main():
    print('*'*45, 'PARSE URL http://www.uklidmecesko.cz/index.html')
    tree = parse('http://www.uklidmecesko.cz/index.html')
            
    root = tree.getroot()

    body = root.find('body')
    # print(body)

    assert len(body) == 6

    from shutil import rmtree
    rmtree(HTML_DIR)

    retrieve_content(root, HTML_DIR)

    create_tpl_for_body(body)

    save_tpl(root, 'main.php')

    # vycisti(root)
    

@tpl
def create_tpl_for_body(i, el):
    

    # print(f'#{i}: {str_element(el)}')

    if i == 2:
        # MENU
        assert el.text.strip() == 'Menu'
        return

    if i == 3:

        move_to_tpl(el, 'menu.php')
        return

    if i == 4:
        # CONTENT
        assert el.text.strip() == 'Content'
        return

    if i == 5:
        create_tpl_for_content(el)
        return

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

    
