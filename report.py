import time
import requests

session = requests.session()
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "searchapi.eastmoney.com",
    "Referer": "https://so.eastmoney.com/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

URL_front = "https://searchapi.eastmoney.com/bussiness/Web/GetSearchList?cb=jQuery35108916697183193074_1625468720071&keyword="
URL_back = "&type=501&pageindex=1&pagesize=10&name=normal&_=1625468720072"


keyWord = ["600519"]








def getUrlList(keyWord):
    urlList = []
    for i in keyWord:
        urlList.append(URL_front + str(i) + URL_back)
    for i in urlList:
        print(i)
    return urlList

def getInfo(urlList):
    responseList = []
    for i in urlList:
        response = session.get(i, headers = headers)
        tem = response.text.split(",")
        responseList.append(tem)
        time.sleep(2)
    return responseList

def getReportUrls(stockUrlList):
    reportUrlsList = []
    for stock in stockUrlList:
        for index, line in enumerate(stock):
            if "Title" in line:
                title = line
                url = stock[index + 2]
                time = stock[index + 1]
                # print([title, url, time])
                reportUrlsList.append([title, url, time])
            else: continue
    return reportUrlsList

def downloadReport(reportUrlList):
    downloadUrl = []
    for report in reportUrlList:
        reportUrl = report[1][7:-1]
        response = requests.get(reportUrl)
        detail = response.text.split("\n")
        for line in detail:
            if "rightlab" in line:
                line = line.split('"')
                url = line[3]
                downloadUrl.append(url)
                continue
    return downloadUrl


def main():
    urlList = getUrlList(keyWord)
    stockUrlList = getInfo(urlList)
    reportUrlsList = getReportUrls(stockUrlList)
    result = downloadReport(reportUrlsList)
    for i in result:
        print(i)





main()