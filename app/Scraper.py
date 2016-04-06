#!/usr/bin/env python
import mechanicalsoup
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
    script_list = soup.find_all('noscript')
    if len(script_list) >= 2:
        desc = script_list[1].div.prettify()
    else:
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
    img_a = soup.find(class_='ap-author-image').get('src')
    return img_a


def aBio(soup):
    bio = soup.find(
        class_='a-expander-content a-expander-partial-collapse-content').span.string
    return bio


def bookScrape(book_obj):
    url = book_obj.amazon_link
    mech = mechanicalsoup.Browser()
    page = mech.get(url)
    html = page.soup
    book_obj.image_link = bkImg(html)
    book_obj.description = bkDesc(html)
    author_link = aLink(html)
    print("*" * 80)
    if author_link:
        print("%" * 80)
        page = mech.get(author_link)
        html = page.soup
        author = book_obj.author
        author.link = aImg(html)
        author.bio = aBio(html)
        DB.session.add(author)
    DB.session.add(book_obj)
    DB.session.commit()
