#!/usr/bin/env python

import sys
from mechanize import Browser
from bs4 import BeautifulSoup

def bkImg (html) :
	soup = BeautifulSoup(html, 'html.parser')
	img_bk = soup.find_all('img', class_='frontImage')

	#grabbing specific link with this tag
	for link in img_bk :
		s = link.get('data-a-dynamic-image')

	#grabbing the usable link from string
	start = 0
	end = s.find('":[')
	result = s[start + 2:end]

	return result

def bkDesc (html) :
	soup = BeautifulSoup(html, 'html.parser')
	desc = soup.find_all('noscript')[1].div.prettify()
	return desc

def aLink (html) :
	soup = BeautifulSoup(html, 'html.parser')
	frag = soup.find(class_="a-link-normal contributorNameID").get('href')
	link = 'http://www.amazon.com' + frag
 	return link

def aImg (html) :
	soup = BeautifulSoup(html, 'html.parser')
	return

def aBio (html) :
	soup = BeautifulSoup(html, 'html.parser')
	bio = soup.find(class_='a-expander-content a-expander-partial-collapse-content').span.string
	return bio

def scrape (url, type) :

	mech = Browser()
	page = mech.open(url)
	html = page.read()

	if type == 0 : #book html page
		print(bkImg(html))
		print(bkDesc(html))
		print(aLink(html))

	if type == 1 : #author html page
		print(aImg(html))
		print(aBio(html))
	

