import tkinter
import requests
from bs4 import BeautifulSoup

root = tkinter.Tk()
textExample=tkinter.Text(root, height=40)
textExample.pack()
textExample.place(x=90, y=40)
  
  
def  data_print():
    import requests
    get_url =txt.get()

    site = requests.get(get_url)
    data = BeautifulSoup(site.text, 'html.parser')
    textExample.insert(tkinter.END,data.find_all("p"))
       
      
# clickイベント
def btn_click():
    textExample.delete("1.0",tkinter.END)
    data_print()
    
def btn_click6():
    
    textExample.delete("1.0",tkinter.END)

# ボタン
btn = tkinter.Button(root, text='実行', command=btn_click)
btn.place(x=10, y=80)

btn6 = tkinter.Button(root, text='入力クリア', command=btn_click6)
btn6.place(x=10, y=570)



# 画面サイズ
root.geometry('700x600')
# 画面タイトル
root.title('スクレいピング')
# ラベル
lbl = tkinter.Label(text='')
lbl.place(x=10, y=10)
lbl2 = tkinter.Label(text='結果')
lbl2.place(x=10, y=50)

lbl3 = tkinter.Label(text='URL')
lbl3.place(x=10, y=10)

# テキストボックス
txt = tkinter.Entry(width=80)
txt.place(x=90, y=10)
txt.insert(tkinter.END,"")

# 表示
root.mainloop()
