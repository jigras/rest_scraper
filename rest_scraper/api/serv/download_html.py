import requests
from selectolax.parser import HTMLParser
from urllib.parse import urlparse


def download_html(url):
    req = requests.get(url)
    if req.status_code != requests.codes.ok:
        return False
    return req.content

def get_text_selectolax(html):
    """
    Getting text from html document with html, script, style tag removal

    @param html: string HTML document
    @return: text string
    """
    tree = HTMLParser(html)
    if tree.body is None:
        return None
    tags = ['head', 'style', 'script']
    tree.strip_tags(tags)
    text = tree.body.text(separator=' ', strip=True)
    return text.strip()


def get_list_image(html):
    """
    Getting list of images from html document
    @param html: string HTML document
    @return: list of img src
    """
    tree = HTMLParser(html)
    if tree.body is None:
        return None
    imgs = []
    for img in tree.css('img'):
        if img.attrs.get('src'):
            img_url = check_img_url(img.attrs['src'])
            if img_url:
                imgs.append(img_url)
    return imgs


def check_img_url(img_url):
    """
    Checking image url, if its start with '//' then the schema is added
    @param img_url: string
    @return: bool
    """
    if img_url.startswith('//'):
        img_url = '{}{}'.format('http:', img_url)
    if is_url(img_url):
        return img_url


def is_url(url):
    """
    Checking if string image url is valid URL
    @param url: string
    @return: bool
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False