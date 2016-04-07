#!/usr/bin/env python
import mechanicalsoup
import time
from extensions import DB


def bkImg(soup):
    img_bk = soup.find_all('img', class_='frontImage')

    # grabbing specific link with this tag
    s = ""
    for link in img_bk:
        s = link.get('data-a-dynamic-image')

    # grabbing the usable link from string
    start = 0
    end = s.find('":[')
    result = s[start + 2:end]
    return result


def bkDesc(soup):
    try:
        script_list = soup.find_all('noscript')
        if len(script_list) >= 2:
            desc = script_list[1].div.prettify()
        else:
            desc = "sorry no description found"
    except Exception:
        desc = "sorry no description found"
    return desc


def aLink(soup):
    frag = soup.find(class_="a-link-normal contributorNameID")
    if frag:
        link = 'http://www.amazon.com' + frag.get('href')
    else:
        link = None
    return link


def aImg(soup):
    img_a = soup.find(class_='ap-author-image')
    if img_a:
        img_a = img_a.get('src')
    else:
        img_a = None
    return img_a


def aBio(soup):
    try:
        bio = soup.find(
            class_='a-expander-content a-expander-partial-collapse-content').span.string
    except Exception:
        bio = "No Bio Found"
    return bio


def bookScrape(book_obj):
    url = book_obj.amazon_link
    mech = mechanicalsoup.Browser()
    page = mech.get(url)
    # retry block to keep hitting the page until appropriate reponse
    retries = 0
    while page.status_code == 503 and retries < 5:
        time.sleep(2)
        retries += 1
        page = mech.get(url)
    if retries == 5:
        return 0
    html = page.soup
    book_obj.image_link = bkImg(html)
    book_obj.description = bkDesc(html)
    author_link = aLink(html)
    val = 0
    if author_link:
        page = mech.get(author_link)
        retries = 0
        while page.status_code == 503 and retries < 5:
            time.sleep(2)
            retries += 1
            page = mech.get(url)
        if retries == 5:
            return 0
        html = page.soup
        try:
            author = book_obj.author
        except Exception:
            DB.session.rollback()
            book_obj.description = "None"
            author = book_obj.author
        author.link = aImg(html)
        author.bio = aBio(html)
        DB.session.add(author)
        val = 1
    try:
        DB.session.add(book_obj)
        DB.session.commit()
    except Exception:
        DB.session.rollback()
        book_obj.description = "None"
        DB.session.add(book_obj)
        DB.session.commit()
    return val
