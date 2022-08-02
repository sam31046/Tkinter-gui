########## 由網路下載資料 ##########
import sys
import urllib.request as httplib  # 3.x
import json


filename = "台南景點中文名稱"
#### 由網路下載 JSON 的 字串 ####
url="https://soa.tainan.gov.tw/Api/Service/Get/5767e748-f68b-4b96-809a-19d68c0d450a"

req = httplib.Request( url,data=None,
    headers={ 'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"})
reponse = httplib.urlopen(req)               # 開啟連線動作
if reponse.code==200:                        # 當連線正常時
    contents=reponse.read()                  # 讀取網頁內容
    contents=contents.decode("utf-8")        # 轉換編碼為 utf-8
    #print(contents)
    # 儲存檔案
    with open(filename + ".json", "w", encoding="utf-8") as f:
        f.write(contents)


#### 字串 換成  JSON 的 Dict ####
obj1= json.loads(contents)
print(obj1)
obj1["data"].append( {"景點中文名稱":"Testing by Sam Jhong"} )
for dict2 in obj1["data"]:
    print("  景點中文名稱:",dict2["景點中文名稱"])

