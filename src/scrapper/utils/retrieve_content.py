from urllib.parse import urlparse, urljoin

from urllib.request import urlopen, urlretrieve

import tinycss

from utils import *

def _retrieve(zdroj, cil):
    dir = cil.parent
    dir.mkdir(parents=True, exist_ok = True)
    try:
        urlretrieve(zdroj, cil)
    except Exception as err:
        err_msg = f"selhalo stahování {zdroj} => {cil}: {err}"
        print(err_msg)
        raise Exception(err_msg)


def retrieve_content(element, destination_dir):
    for link in element.iterlinks():
        # print(link)
        el = link[0]
        # tag = link[0].tag

        if el.tag == 'a':
            print(link[1], link[2])
            continue

        retrive_link(el, link[2], destination_dir)

def retrive_link(el, url_path, destination_dir):
        
    url = urlparse(url_path)
    # print(url)
    # exit()
    if url.netloc is '':
        zdroj = urljoin(el.base_url, url_path)
        # webbrowser.open(zdroj)
        
        destination = destination_dir / url_path.lstrip('/')

        # print(str_element(el))
        _retrieve(zdroj, destination)

        if el.tag == 'link':
            if destination.suffix == '.css' or el.attrib['rel'] == 'stylesheet':
                retrieve_css_content(
                    css_destination = destination,
                    url_path = url_path,
                    destination_dir = destination_dir,
                    base_url = el.base_url
                    )
            

def retrieve_css_content(css_destination, url_path, destination_dir, base_url):
    
    style = css_destination.read_text()
    
    stylesheet = tinycss.make_parser().parse_stylesheet(style)
    # print(stylesheet)
    for rule in stylesheet.rules:
        # print(rule, dir(rule))
        # print(type(rule))
        if isinstance(rule, tinycss.css21.ImportRule):
            print("TODO ImportRule")
            print(rule)
            continue

        for decl in rule.declarations:
            # print(dir(decl))
            value = decl.value
            for token in value:
                # if token.type not in ('IDENT', 'PERCENTAGE', 'DIMENSION', 'S', 'INTEGER', 'HASH', 'STRING', 'DELIM'):
                if token.type == 'URI':
                    # print(token.type, token)
                    if hasattr(token, 'value'):
                        
                        # print(css_destination)
                        # print(css_destination.parent)
                        # print(token.value)
                        destination = css_destination.parent.joinpath(token.value) #.resolve()
                        zdroj = Path(url_path.lstrip('/')).parent.joinpath(token.value) #.resolve()
                        zdroj = urljoin(base_url, str(zdroj))
                        # print(zdroj, destination)
                        _retrieve(zdroj, destination)
                        
                    # print(dir(token))