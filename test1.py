import requests

url = "http://data.eastmoney.com/report/zw_stock.jshtml?encodeUrl=VlGKMWHU/qAWPfsBmACIGFs5XPvf4EnHM6IctFF+M6M="

res = requests.get(url)
content = res.text.split("\n")
for line in content:
    if "rightlab" in line:
        print(line)

print()