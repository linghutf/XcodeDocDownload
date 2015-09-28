# -*- coding: utf-8 -*-
__author__ = 'xdc'

import requests
from bs4 import BeautifulSoup as bs
from lxml import etree

def getAppleXcodeDocXml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'zh_CN',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    r = requests.get(url,headers=headers)
    return r.content

def readXml(doc):
    #soup = bs(doc,'lxml')
    soup=etree.fromstring(doc)
    names = soup.xpath("//key[text()='name']/following::*[1]")
    sources = soup.xpath("//key[text()='source']/following::*[1]")
    data=dict()
    if len(names)!=len(sources):
        return data
    for i in xrange(len(names)):
        data[names[i].text]=sources[i].text
    return data

if __name__ == '__main__':
    data=readXml(getAppleXcodeDocXml("https://developer.apple.com/library/downloads/docset-index.dvtdownloadableindex"))
    for (k,v) in data.items():
        print '-'*20
        print k,'\n',v



