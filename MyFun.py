# Translate number to zodiac in chinese

def Translate_Zodiac_Chinese(i_x=0):
    list = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]
    if i_x>=1 and i_x<=12:
        y=list[i_x - 1]
    else:
        y="輸入錯誤"
    return y


# Mulitply two numbers

def Math_Multiply_Two(a=0,b=0):
    return a*b


# Divide two numbers

def Math_Divide_Two(a=0,b=0):
    return a/b


# Add two numbers

def Math_Add_Two(a=0,b=0):
    return a+b


# Translate city in chinese with one parameter

def Translate_City_Chinese(city=0):
    cityEng=["Tokyo","Okinawa","Osaka"]
    cityChin=["東京","沖繩","大阪"]
    count=0                                 # 字串從第0筆開始檢查
    for i in cityEng:                       # 依序讀取英文城市
        if i.lower() == city.lower():       # 如果名稱跟輸入的一樣(避免錯誤換成小寫)
            return city,cityChin[count]     # 回傳英文、中文名稱，依照當下的筆數
        count=count+1
    return "輸入錯誤","輸入錯誤"               # 如果之前還沒回傳，表示有誤


# Ascending sort list with bubble sorting algorithm

def BubbleSort_List(list1,descend=0):         # 0預設為遞增
    # list1 做 泡沫排序法 由小到大
    x = 0
    while x < len(list1):                     # 做跟list1一樣長度的round
        y = 0
        while y < len(list1) - 1:             # 每一個做比較，減1是因為最後一筆會溢位
            # llist長度減1個間隔，每一round做最多list長度減1次交換
            # 判斷 現在的位置 和下一個位置的大小
            # 如果 list1[y] 大於 list1[y+1] 且沒遞減
            if (list1[y] > list1[y + 1]) and descend==0:

                # 與下一筆互換資料
                temp = list1[y]               # 先做 temp 為 list1[y]
                list1[y] = list1[y + 1]       # list1[y] 為 list1[y+1]
                list1[y + 1] = temp           # list1[y+1] 為 temp

            # 如果 list1[y] 小於 list1[y+1] 且有遞減
            if (list1[y] < list1[y + 1]) and descend==1:

                # 與下一筆互換資料
                temp = list1[y]               # 先做 temp 為 list1[y]
                list1[y] = list1[y + 1]       # list1[y] 為 list1[y+1]
                list1[y + 1] = temp           # list1[y+1] 為 temp

            y = y + 1
        x = x + 1
    return list1


# Preserve numbers less than certain value in a list

def Preserve_Less_list(list1,x):
    temp = list()
    for i in range(len(list1)):
        if list1[i] < x:
            temp.append(list1[i])

    return temp


# Find maximum in a list

def Find_Max_List(list1):
    max=0
    for i in range(len(list1)):
        if list1[i] > max:
            max = list1[i]
    return max


# Establish a class of student infomation

class studentClass(object):  # 繼承Python最上層的object類別
    # 屬性property
    # 提醒自己有哪些變數可以使用，不會宣告，不影響運算
    studentLastName = "Jhong"                    # 使用者姓
    studentFirstName = "Dong-You"                # 使用者名
    studentAge = 24                              # 定義年齡
    stusentID = 1                                # 定義ID
    studentWeight = 100                          # 定義體重
    studentHeight = 200                          # 定義身高
    studentGender = "Mail"                       # 定義性別
    studentEducation = "University"              # 定義學歷
    def __init__(self,LastName,FirstName,Age,ID,Weight,Height,Gender,Education):
        # 類別初始化的函數 initialize 一開始要做的函數
        self.studentLastName = LastName            # 宣告使用者姓
        self.studentFirstName = FirstName
        self.studentAge = Age
        self.studentID = ID
        self.studentWeight = Weight
        self.studentHeight = Height
        self.studentGender = Gender
        self.studentEducation = Education
    def info(self):                                #  Method 方法
        print("姓：",self.studentLastName)
        print("名：",self.studentFirstName)
        print("年齡：",self.studentAge)
        print("ID：",self.studentID)
        print("體重：",self.studentWeight)
        print("身高：",self.studentHeight)
        print("性別：",self.studentGender)
        print("學歷：",self.studentEducation)
        #self.cacluateValues()                      # 呼叫方法2

    def info_str(self):
        print("姓：", self.studentLastName)
        print("名：", self.studentFirstName)
        print("年齡：", str(self.studentAge))        # 轉成文字
        print("ID：", str(self.studentID))
        print("體重：", str(self.studentWeight))
        print("身高：", str(self.studentHeight))
        print("性別：", self.studentGender)
        print("學歷：", self.studentEducation)
    def info_fullname(self):
        print("學生：",self.studentLastName + self.studentFirstName)
    def info_allinfo(self):
        self.info_fullname()                        # 呼叫info_fullname
        self.info()                                 # 呼叫info

# Translate number to chinese

def numberToChinese(n):
    list1 = ["圓","拾", "佰", "仟", "萬", "拾", "佰", "仟", "億"]
    list2 = ["零", "壹", "貳", "參", "肆", "伍", "陸", "柒", "捌", "玖"]
    str1 = ""
    digit = 0
    while True:
        n1 = n % 10
        n = n // 10
        # 處理位數
        str1 = list1[digit] + str1
        # 數字轉國字
        if n1 >= 0 and n1 <= 9:
            str1 = list2[n1] + str1
        if n <= 0:  # n < 0時結束迴圈
            break

        digit = digit +1
    return str1

"""
# Establish a class of Triplicate Uniform Invoice

class tri_uniform_invoice(object):
    
    global itemEntryString
    global quantityEntryString
    global valueEntryString
    global ItemStr
    global QuantityStr
    global ValueStr
    global SAStr
    global SalesAmount
    global BusinessTax
    global BTStr
    global Total
    global TotalStr
    global ChineseTotal
    global ChineseTotalStr
    
    def __init__(self):

        self.getItem = itemEntryString.get()  # 取得itemEntry上的文字
        self.getQuan = quantityEntryString.get()  # 取得quantityEntry上的文字
        self.getVal = valueEntryString.get()  # 取得valueEntry上的文字

        ItemStr.set(str(self.getItem))  # 設定 ItemStr 上文字
        QuantityStr.set(str(self.getQuan))  # 設定 QuantityStr 上文字
        ValueStr.set(str(self.getVal))  # 設定 ValueStr 上文字
        self.sales_amount()         # 呼叫sales_amount函式，累加至SalesAmount
        SAStr.set("Sales Amount：" + SalesAmount)  # 設定 SAStr 上文字
        self.business_tax()         # 呼叫business_tax函式，計算至BusinessTax
        BTStr.set("Business Tax：" + BusinessTax)  # 設定 BTStr 上文字
        self.total()                # 呼叫total函式，計算至Total
        TotalStr.set("Total：" + Total)  # 設定 TotalStr 上文字
        # 呼叫numberToChinese函式，計算至ChineseTotal
        ChineseTotal = numberToChinese(Total)
        ChineseTotalStr.set("總計：" + ChineseTotal)

    def sales_amount(self):
        global SalesAmount
        SalesAmount = SalesAmount + (int(self.getQuan) * int(self.getVal))

    def business_tax(self):
        global BusinessTax
        BusinessTax = SalesAmount *5 /100       # 營業稅 5%

    def total(self):
        global SalesAmount
        global BusinessTax
        global Total
        Total = SalesAmount + BusinessTax
"""

# Evaluate a string including math operators

class str_2_operators(object):

    def __init__(self,str):
        self.str = str
        self.evaluation()

    def evaluation(self):
        x = "0"                         # string between two operators
        opercount = 0                   # operator index: first, second...
        temp = 0                        # sum before the operator
        index = 1                       # the index in the string starting with 1
        lastoper = ""                   # last operator
        self.str = "0" + self.str       # to prevent the str starting with negative operator

        for i in self.str:

            # if character is integer
            if i.isdigit() or (i == "="):
                if i != "=":
                    x = x + i               # append characters

                # if end of the string
                if index == len(self.str) or (i == "="):
                    if lastoper == "+":
                        temp = temp + int(x)
                        return str(temp)
                    elif lastoper == "-":
                        temp = temp - int(x)
                        return str(temp)
                    elif lastoper == "*":
                        temp = temp * int(x)
                        return str(temp)
                    elif lastoper == "/":
                        temp = temp / int(x)
                        return str(temp)
                    else:
                        temp = int(x)
                        return str(temp)
            else:
                # if character is operator
                if i == "+":
                    opercount = opercount + 1
                    if opercount == 1:
                        temp = int(x)
                    lastoper = "+"
                    # store the sum in temp
                    if opercount == 2:
                        temp = temp + int(x)

                    x = "0"                 # clear string between two operators
                elif i == "-":
                    #if index == 1:
                        #temp = 0 - int(x)                    # if the starting of string is negative
                    #if index != 1:
                    opercount = opercount + 1
                    if opercount == 1:
                        temp = int(x)
                    lastoper = "-"
                    if opercount == 2:
                        temp = temp - int(x)

                    x = "0"
                elif i == "*":
                    opercount = opercount + 1
                    if opercount == 1:
                        temp = int(x)
                    lastoper = "*"
                    if opercount == 2:
                        temp = temp * int(x)

                    x = "0"
                elif i == "/":
                    opercount = opercount + 1
                    if opercount == 1:
                        temp = int(x)
                    lastoper = "/"
                    if opercount == 2:
                        temp = temp / int(x)

                    x = "0"
            index = index + 1


# To import chinese font on Linus, MacOS, Windows
# For GUI, plot purpose
# import sys
class font_import(object):

    def __init__(self):
        import sys
        if sys.platform.startswith("linux"):
            # could be "linux", "linux2", "linux3", ...
            self.font_linuxOS()
        elif sys.platform == "darwin":
            # MAC OS X
            self.font_macOS()
        elif sys.platform == "win32":
            # Windows (either 32-bit or 64-bit)
            self.font_winOS()

    def font_linuxOS(self):
        print("linux need font")  # linux
        print("Initiated font")

    def font_macOS(self):
        try:
            import seaborn as sns
            sns.set(font="Arial Unicode MS")  # "DFKai-SB"
            print("Initiated Seaborn font")
        except:
            print("Initiated Seaborn font failed")
        try:
            import matplotlib.pyplot as plt
            from matplotlib.font_manager import FontProperties
            plt.rcParams['font.sans-serif'] = 'Arial Unicode MS'
            plt.rcParams['axes.unicode_minus'] = False
            print("Initiated matplotlib font")
        except:
            print("Initiated matplotlib font failed")

    def font_winOS(self):
        # Windows (either 32-bit or 64-bit)
        try:
            import seaborn as sns
            sns.set(font="sans-serif")  # "DFKai-SB"
            print("Initiated Seaborn font ")
        except:
            print("Initiated Seaborn font failed")
        try:
            import matplotlib.pyplot as plt
            plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 換成中文的字體
            plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決seaborn座標軸亂碼問題）
            print("Initiated matplotlib font")
        except:
            print("Initiated matplotlib font failed")


def df_split_date(df,needSplitColheader=None,newCol1header=None
                  ,newCol2header=None,newCol3header=None
                  ,splitSymbol='/',expand=True):
    import pandas as pd
    # print("Original DataFrame:")
    # print(df)
    df[[newCol1header, newCol2header, newCol3header]] = df[needSplitColheader].str.split(splitSymbol, expand=expand)
    ## Tips: Return str type
    # print("\nNew DataFrame:")
    # print(df)
"""
https://www.tutorialspoint.com/write-a-program-in-python-to-split-the-date-column-into-day-month-year-in-multiple-columns-of-a-given-dataframe
Sample Code:
import pandas as pd
df = pd.DataFrame({
      'date': ['17/05/2002','16/02/1990','25/09/1980','11/05/2000','17/09/1986']
   })
print("Original DataFrame:")
print(df)
df[["day", "month", "year"]] = df["date"].str.split("/", expand = True)
print("\nNew DataFrame:")
print(df)
"""



import os
def text_read(filename, encodetyp='utf-8'):
    filename = filename + '.txt'
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        with open(filename, 'r', encoding=encodetyp) as fr:
            lines = fr.readlines()  # Become a list
            str1 = ""
            for line in lines:
                str1 = str1 + line
                #print(str1)
                fr.close()
            return str1
        return ""
    return print('File Not Accessible!')


def text_write(filename, content):
    filename = filename + '.txt'
    with open(filename, 'w') as fw:
        fw.write(content)
        fw.close()
        return content
    return print('File Not Accessible!')


def file_exit(filename):
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        return True
    return False


def file_del(filename):
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        os.remove(filename)
        return True
    return False


def file_rename(filename, newfilename):
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        os.rename(filename, newfilename)
        return True
    return False


import shutil
def file_copy(filename, newfilename):
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        shutil.copy(filename, newfilename)
        return True
    return False

from datetime import datetime
def date_current_str(form='%Y-%m-%d %H:%M:%S'):
    x = datetime.today().strftime(form)
    #print(x)
    return x
"""
    EX:
    x = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    print(x)
    x = datetime.today().strftime('%Y%m%d')
    print(x)
"""

import csv
def CSV_conv_to2Darray(filename='CSV_conv_to2Darray.csv'):
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        list1 = []
        with open(filename, 'r', encoding='utf-8') as fin:
            read = csv.reader(fin, delimiter=',')
            header = next(read)  # 讀取第一行標題 , 如果沒有標題，請移除
            # print(header)  # 輸出標題      , 如果沒有標題，請移除
            list1.append(header)
            count = 0
            for row in read:
                list1.append(row)
                # print(row)  # 輸出每一行
                count = count + 1  # 計算總共有幾行
            fin.close()  # 關閉檔案
        return list1
    return print('File Not Accessible!')



def Array_2D_Select(array,rowStart=None,rowEnd=None
                   ,colStart=None,colEnd=None):
    array = array[rowStart:rowEnd][colStart:colEnd]
    return array


import matplotlib.pyplot as plt
def Plt_save_png_show(filename="1.png"):
    plt.savefig(filename)
    from PIL import Image
    img = Image.open(filename)
    img.show()


import pandas as pd
def CSV_conv_to_xlsx(filename='CSV_conv_to_xlsx'):
    try:
        path = get_current_directory()
        read_file = pd.read_csv(path + filename + '.csv')
        read_file.to_excel(path + filename + '.xlsx'
                           , index=None, header=True)
        print("csv convert to xlsx successfully!")
    except:
        print("csv convert to xlsx failed!")



def get_current_directory():
    return os.getcwd()

# get path first before using pathFix
import sys
def Folder_path_fix(iPath):
    if sys.platform.startswith("linux") or sys.platform == "darwin":  # MAC OS X
        iPath = iPath.replace("\\","/")
        #print("Folder path fixed!")
    elif sys.platform == "win32":   # Windows (either 32-bit or 64-bit)
        iPath = iPath.replace("/", "\\")
        #print("Folder path fixed!")
    return iPath


def Folder_exist(iPath):      # 查詢資料夾是否存在
    iPath = Folder_path_fix(iPath)
    if os.path.exists(iPath):
        #print("Folder found!")
        return True
    #print("Folder not found!")
    return False



def Folder_create(iPath):       # 在指定路徑創建資料夾
    iPath = Folder_path_fix(iPath)
    if Folder_exist(iPath)==False:   # 查詢資料夾是否存在
        os.mkdir(iPath)
        print("Folder created successfully!")
        return True
    print("Folder exist!")
    return False


# Default: 上一層
def Folder_goto(iPath="../"):       # 進入資料夾
    iPath = Folder_path_fix(iPath)
    if Folder_exist(iPath)==True:   # 查詢資料夾是否存在
        os.chdir(iPath)
        print("You have gone to...")
        print("Current location: ",iPath)
        return True
    print("Failed!")
    print("Current location: ",iPath)
    return False



def Folder_del(iPath):     # 移除資料夾
    iPath = Folder_path_fix(iPath)
    if Folder_exist(iPath)==True:   # 查詢資料夾是否存在
        os.rmdir(iPath)
        print("Folder deleted successfully!")
        return True
    print("Folder not found!")
    return False


# Get a row with all columns
def xlsx_get_row(sheet, row1=1):
    list1=[]
    col1=1
    while col1<sheet.max_column:
        x=sheet.cell(row=row1, column=col1).value  # Get A1
        # print(x)
        list1.append(x)
        col1=col1+1
    return list1


# Get a column with all rows
def xlsx_get_col(sheet, col1=2):
    list1=[]
    row1 = 1
    while row1<sheet.max_row:
        x=sheet.cell(row=row1, column=col1).value  # Get A2
        # print(x)
        list1.append(x)
        row1=row1+1
    return list1


# Python program to check if two
# to get unique values from list
# using traversal
# function to get unique values

### Method 2: list unique values in class set ###
# print(set(country_list))
# print(type(set(country_list)))
# country_list = list(set(country_list))

def List_unique_value(list1):
        # initialize a null list
        unique_list = []
        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
        return unique_list


import matplotlib.pyplot as plt
def Plt_charts(x,y,title,xlabel,ylabel):
    fig, ax = plt.subplots(2, 2,figsize=(16,7)
                            , facecolor='#FFFFF0')
    """
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    """
    #### subplot 1 #####
    ax[0, 0].plot(x, y, '*',c='red')
    ax[0, 0].plot(x, y, '--',c='#FF8C00')
    ax[0, 0].tick_params(axis='x', labelsize=8, rotation=90)
    ax[0, 0].tick_params(axis='y', labelsize=8, rotation=0)
    ax[0, 0].set_xlabel(xlabel, fontsize=10)  # X label
    ax[0, 0].set_ylabel(ylabel, fontsize=10)  # Y label
    ax[0, 0].set_title(title) #, fontsize=7)

    #### subplot 2 ####
    ax[0, 1].bar(x, y, color='#339999')
    ax[0, 1].tick_params(axis='x', labelsize=8, rotation=90)
    ax[0, 1].tick_params(axis='y', labelsize=8, rotation=0)
    ax[0, 1].set_xlabel(xlabel, fontsize=10)  # X label
    ax[0, 1].set_ylabel(ylabel, fontsize=10)  # Y label
    ax[0, 1].set_title(title)

    #### subplot 3 ####
    ax[1, 0].plot(x, y, 'r+')
    ax[1, 0].tick_params(axis='x', labelsize=8, rotation=90)
    ax[1, 0].tick_params(axis='y', labelsize=8, rotation=0)
    ax[1, 0].set_xlabel(xlabel, fontsize=10)  # X label
    ax[1, 0].set_ylabel(ylabel, fontsize=10)  # Y label
    ax[1, 0].set_title(title)

    #### sunplot 4 ####
    area = y
    colors = y
    ax[1, 1].scatter(x, y, s=area, c=colors, alpha=0.5)
    ax[1, 1].tick_params(axis='x', labelsize=8, rotation=90)
    ax[1, 1].tick_params(axis='y', labelsize=8, rotation=0)
    ax[1, 1].set_xlabel(xlabel, fontsize=10)  # X label
    ax[1, 1].set_ylabel(ylabel, fontsize=10)  # Y label
    ax[1, 1].set_title(title)

    fig.tight_layout()
    plt.show()


def XLSX_conv_to_CSV(filename='XLSX_conv_to_CSV'):
    try:
        path = get_current_directory()
        read_file = pd.read_excel(path + filename + '.xlsx')
        read_file.to_csv(path + filename + '.csv')
        print("xlsx convert to csv successfully!")
    except:
        print("xlsx convert to csv failed!")


def CSV_conv_to_JSON(filename='CSV_conv_to_JSON'):
    try:
        path = get_current_directory()
        csv_data = pd.read_csv(path + filename + '.csv', sep=",")
        csv_data.to_json(path + filename + '.json', orient="records")
        print("csv convert to json successfully!")
    except:
        print("csv convert to json failed!")


import json
def JSON_file_read(filename='JSON_file_read'):
    # Python program to read json file
    # Opening JSON file
    f = open(filename + ".json")
    # returns JSON object as a dictionary
    dictionary = json.load(f)
    # Closing file
    f.close()
    return dictionary