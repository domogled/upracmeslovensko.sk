import polib

def po_file(file):
    if not file.is_file():
        po = polib.POFile()
        po.metadata = {
            'Project-Id-Version': '1.0',
            'Report-Msgid-Bugs-To': 'upracmeslovensko@domogled.com',
            'POT-Creation-Date': '2007-10-18 14:00+0100',
            'PO-Revision-Date': '2007-10-18 14:00+0100',
            'Last-Translator': 'you <you@example.com>',
            'Language-Team': 'English <yourteam@example.com>',
            'MIME-Version': '1.0',
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-Transfer-Encoding': '8bit',
        }

        po.save(file)
        po.save_as_mofile(file.with_suffix('.mo'))

    return polib.pofile(file)


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
                    return meta.attrib[key]
    
        source = meta.attrib.get('property', )


        file = HTML_DIR / 'locale/cs_CZ.po'
        po = po_file(file)
        entry = polib.POEntry(
            msgid=content,
            msgstr='',
            # occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
            occurrences=[(f'{occurrence()}', '0')]
        )
        po.append(entry)

        po.save(file)
        po.save_as_mofile(file.with_suffix('.mo'))

        meta.attrib['content'] = f'<?php echo _("{content}"); ?>'
        print(meta.attrib.keys())
        print(str_element(meta))