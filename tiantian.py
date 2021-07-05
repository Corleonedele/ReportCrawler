import requests
import openpyxl
from time import strftime as st
URL = "https://roll.eastmoney.com/fund.html"

def getResponse():
    response = requests.get(URL)
    html = response.text.split('\n')
    content = html[211:685]
    return content

def getKeyInfo(content):
    news_list = []
    for line in content:
        if "href" in line:
            lineContent = line.split('"')
            news = lineContent[8]
            news = news[1:len(news) - 4]
            herf = lineContent[3]
            news_list.append([herf, news])
    return news_list


def writeInfo(info_list):
    workbook = openpyxl.Workbook()
    wb = workbook.active
    for item in info_list:
        herf = item[0]
        news = item[1]
        wb.append([news, herf])
    date = st("%m-%d")
    workbook.save(date + ".xlsx")


def main():
    response = getResponse()
    tiantian_news_list = getKeyInfo(response)
    writeInfo(tiantian_news_list)


main()

