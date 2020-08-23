#-*- codeing = utf-8 -*-
#@Time : 2020-08-21 10:24
#@File : zimuzuspyder.py
from bs4 import BeautifulSoup
import re
import requests
import urllib.request , urllib.error
import xlwt
import lxml



def main():
    baseurl = "http://www.rrys2020.com/resourcelist/?page="
    #movieurl = "http://www.rrys2020.com/resource/26312"
    #爬网页
    datalist = getData(baseurl)
    #保存
    excel = xlwt.Workbook(encoding="utf-8")
    sheet = excel.add_sheet('USATV')
    for j in range(0,int(len(datalist)/3)):
        for k in range(0,3):
            sheet.write(j, k, datalist[j*3+k])
        #print(j)
    excel.save("result.xls")

    #dbpath = ".\\result.xls"
    #saveData(dbpath)
    #datalist = askURL(baseurl)
    #print()
   # askURL2(movieurl)


def getData(baseurl):
    datalist=[]

    for i in range(0, 40):
        url = baseurl + str(i) + "&channel=tv&area=%E8%8B%B1%E5%9B%BD&category=&year=&tvstation=&sort="
        html = askURL(url)
        datalist.extend(html)
        # save
        #print(len(datalist))
    return datalist

def askURL(url):
    heads = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    findhref = re.compile(r'<a href="(.*?)"')
    findname = re.compile(r'target="_blank">(.*?)</a>')
    request = urllib.request.Request(url, headers=heads)
    html = ""
    results = []
    try:
        response =urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        bs = BeautifulSoup(html, "html.parser")
       # print(bs)
       # t_list = bs.find_all("h3", class_="f14")
        t_list = bs.find_all("h3", class_="f14")
        for item in t_list:
            item = str(item)
            link = re.findall(findhref,item)[0]
            link2 = re.findall(findname,item)[0]
            trueURL = "http://www.rrys2020.com" + link
            level = askURL2(trueURL)
            if level != '':
                results.append(link2)
                results.append(level)
                results.append(trueURL)

            else:
                results.append(link2)
                results.append("X")
                results.append(trueURL)
            # print(trueURL)
            print(link2)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)


    return results


def askURL2(url):
    findlink = re.compile(r'/level-icon/(.)-big-1.png"')
    heads = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    request = urllib.request.Request(url, headers=heads)
    link = ""
    try:
        response =urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        bs = BeautifulSoup(html, "html.parser")
       # print(bs)
        t_list = bs.find_all("div", class_="level-item")
        for item in t_list:
             item = str(item)
             link = re.findall(findlink,item)[0]

             #print(link,name)


    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)


    return link


def saveData(dbpath):
    # excel = xlwt.Workbook(encoding="utf-8")
    # sheet = excel.add_sheet('sheet1')
    # sheet.write(0,0,'hello')
    print()


if __name__ == "__main__":
    main()
