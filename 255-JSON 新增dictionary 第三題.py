########## 由網路下載資料 ##########
import sys
import urllib.request as httplib  # 3.x
import json


filename = "臺中市海域遊憩活動"
#### 由網路下載 JSON 的 字串 ####
url = "https://datacenter.taichung.gov.tw/swagger/OpenData/7573a518-0881-4a2e-add2-e8496cbafdec"

req = httplib.Request( url,data=None,
    headers={ 'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"})
reponse = httplib.urlopen(req)               # 開啟連線動作
if reponse.code==200:                        # 當連線正常時
    contents=reponse.read()                  # 讀取網頁內容
    contents=contents.decode("utf-8")        # 轉換編碼為 utf-8
    #print(contents)
    # 儲存檔案
    with open(filename+".json", "w", encoding="utf-8") as f:
        f.write(contents)


#### 字串 換成  JSON 的 Dict ####
obj1= json.loads(contents)
print(obj1)
obj1.append( {"CName":"Testing by Sam Jhong"} )
for dict2 in obj1:
    print("  臺中市海域遊憩場所:",dict2["CName"])

