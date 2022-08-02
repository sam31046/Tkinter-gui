# Python 3.x
print('==================================')
"""
===== Display labels =====
Establish a GUI window with labels of product information
"""
print("===== Display labels =====")
import tkinter as tk				       	 # import tkinter
print("start")
win = tk.Tk()       			       		 # Establish window
win.wm_title("Product Information")		     # Set window
win.resizable(width=True, height=True)		 # True: Can adjust window's width, height
win.minsize(width=640, height=480)			 # Window's minsize
win.maxsize(width=1024, height=768)	    	 # Window's maxsize
label1 =tk.Label(win,text="Hello Tkinter!")  # Establish label, display text
label1.place(x=20, y=80)                     # Set label position at x=20, y=60
win.mainloop()				          		 # Last step, combine window in a loop
print("window closed")						 # Print after you close the window
print('==================================')



"""
===== A class with product information =====
"""
print("===== A class with product information =====")

class display_productInfo(object):
    def __init__(self,name,usage,caution,storage,material
                     ,length,quantity,exp):
        self.productName = name
        self.productUsage = usage
        self.productCaution = caution
        self.productStorage = storage
        self.productMaterial = material
        self.productLength = length
        self.productQuantity = quantity
        self.productEXP = exp
    def product_info(self):
        list1 = ["Name：", "Usage：", "Caution：", "Storage：", "Material："
            , "Length：", "Quantity：", "EXP："]
        list2 = [self.productName,self.productUsage,self.productCaution,self.productStorage,
                 self.productMaterial,self.productLength,self.productQuantity,self.productEXP]
        text = str()
        for i in range(len(list1)):
            text = text + str(list1[i]) + str(list2[i]) +"\n"
        return text                                     # Combine into text

        # print("Name：",self.productName)
        # print("Usage：",self.productUsage)
        # print("Caution：",self.productCaution)
        # print("Storage：",self.productStorage)
        # print("Material：",self.productMaterial)
        # print("Length：",self.productLength)
        # print("Quantity：",self.productQuantity)
        # print("EXP：",self.productEXP)


print("start")
win = tk.Tk()
win.wm_title("Product Information")
win.resizable(width=True, height=True)
win.minsize(width=640, height=480)
win.maxsize(width=1024, height=768)
wp = display_productInfo(name="棉花棒",usage="一般清潔",
                         caution="請置於孩童不易取得之處",storage="至於陰涼乾燥處",
                         material="100%純棉",length=7.4,quantity=100*6,exp=5)

label1 =tk.Label(win,text = wp.product_info(),justify = "left")     # Set position on left side
label1.place(x=20, y=20)
win.mainloop()
print("window closed")
print('==================================\nEnd of this program')