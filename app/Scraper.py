#!/usr/bin/env python
import mechanicalsoup
from bs4 import BeautifulSoup
from extensions import DB


def bkImg(html):
    soup = BeautifulSoup(html, 'html.parser')
    img_bk = soup.find_all('img', class_='frontImage')

    # grabbing specific link with this tag
    for link in img_bk:
        s = link.get('data-a-dynamic-image')

    # grabbing the usable link from string
    start = 0
    end = s.find('":[')
    result = s[start + 2:end]

    return result


def bkDesc(html):
    soup = BeautifulSoup(html, 'html.parser')
    desc = soup.find_all('noscript')[1].div.prettify()
    return desc


def aLink(html):
    soup = BeautifulSoup(html, 'html.parser')
    frag = soup.find(class_="a-link-normal contributorNameID").get('href')
    link = 'http://www.amazon.com' + frag
    return link


def aImg(html):
    soup = BeautifulSoup(html, 'html.parser')
    img_a = soup.find(class_='ap-author-image').get('src')
    return img_a


def aBio(html):
    soup = BeautifulSoup(html, 'html.parser')
    bio = soup.find(
        class_='a-expander-content a-expander-partial-collapse-content').span.string
    return bio


def bookScrape(book_obj):
    url = book_obj.amazon_link
    mech = mechanicalsoup.Browser()
    page = mech.get(url)
    html = page.read()
    book_obj.image_link = bkImg(html)
    book_obj.description = bkDesc(html)
    author_link = aLink(html)
    page = mech.get(author_link)
    html = page.read()
    author = book_obj.author
    author.link = aImg(html)
    author.bio = aBio(html)
    DB.session.add(author)
    DB.session.add(book_obj)
    DB.session.commit()
