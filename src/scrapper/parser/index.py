#!/usr/bin/env python3


from utils import *

def create_tpl_for_body(i, el):
    

    if i == 2:
        # MENU
        assert el.text.strip() == 'Menu'
        return

    if i == 3:

        move_to_tpl(el, 'index/menu.php')
        return

    if i == 4:
        # CONTENT
        assert el.text.strip() == 'Content'
        return

    if i == 5:
        for i, sub_el in enumerate(el):
            create_tpl_for_content(i, sub_el)
        
        return


def create_tpl_for_content(i, element):

        if i == 0:
            assert element.text.strip() == 'Content'
            return

        if i == 1:
            # move_to_tpl(child, 'content_content.php')
            # from content import create_tpl_for_content_content

            assert len(element) == 1

            #  pozor, projíždím potomka element[0]
            for i, sub_el in enumerate(element[0]):
                create_tpl_for_content_content(i, sub_el)

            move_to_tpl(element, 'index/content_content.php')
            return

        if i == 2:
            assert element.text.strip() == 'Footer'
            return

        if i == 3:
            move_to_tpl(element, 'index/content_footer_container.php')
            return

        if i == 4:
            assert element.text.strip() == '/container'
            return

        if i == 5:
            move_to_tpl(element, 'index/generalni_partner.php')
            return

        if i == 6:
            move_to_tpl(element, 'index/kontakty.php')
            return

        if i == 7:
            move_to_tpl(element, 'index/spolufinancovan_MZP.php')
            return

        if i == 8:
            assert element.text.strip() == 'Scripts'
            return

        if i == 9:
            assert element.tag == 'script'
            # move_to_tpl(element, 'content_script_1.php')
            return

        if i == 10:
            assert element.tag == 'script'
            # move_to_tpl(element, 'content_script_2.php')
            return

        if i == 11:
            # move_to_tpl(element, 'content_fb_root.php')
            return

        if i == 12:
            assert element.tag == 'script'
            # move_to_tpl(element, 'content_script_3.php')
            return


def create_tpl_for_content_content(i, element):
    
            
    if i == 0:
        move_to_tpl(element, 'index/banner.php')
        return


    if i >= 1 and i <= 3:
        move_to_tpl(element, f'index/velke_menu_var_{i}.php')
        return

    if i == 4:
        # move_to_tpl(element, 'content_content_script.php')
        assert element.tag == 'script'
        return

    if i == 5:
        assert len(element) == 6

        for i, sub_el in enumerate(element):
                create_tpl_for_content_content_block(i, sub_el)
        
        move_to_tpl(element, 'index/content_content_block.php')
        return
        

def create_tpl_for_content_content_block(i, element):
    

    if i == 0:
        assert element.tag == 'script'
        return

    if i == 1:
        assert element.tag == 'script'
        return

    if i == 2:
        assert element.tag == 'script'
        return

    if i == 3:
        assert len(element) == 3

        for i, sub_el in enumerate(element):
                create_tpl_for_content_content_block_row_1(i, sub_el)
        
        move_to_tpl(element, 'index/content_content_block_row_1.php')
        return
        
    if i == 4:
        assert len(element) == 3
        
        for i, sub_el in enumerate(element):
                create_tpl_for_content_content_block_row_2(i, sub_el)
        
        move_to_tpl(element, 'index/content_content_block_row_2.php')
        return

    if i == 5:
        assert len(element) == 0
        # tady je zakomentovaný nějaký php blok kodu
        return

    
def create_tpl_for_content_content_block_row_1(i, element):
   
    if i == 0:
        move_to_tpl(element, 'index/foto_z_lonska.php')
        # element.drop_tree()
        return

    if i == 1:
        move_to_tpl(element, 'index/statistika_uklidu.php')
        return

    if i == 2:
        move_to_tpl(element, 'index/soutez_musime_to_uklidit.php')
        return
   
def create_tpl_for_content_content_block_row_2(i, element):
    
    if i == 0:
        move_to_tpl(element, 'index/co_je_noveho.php')
        return

    if i == 1:
        move_to_tpl(element, 'index/medialni_partneri.php')
        return

    if i == 2:
        move_to_tpl(element, 'index/napsali_o_nas.php')
        return
