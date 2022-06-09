import tkinter
import requests
from bs4 import BeautifulSoup
import webbrowser
import os
import sys




root = tkinter.Tk()
textExample=tkinter.Text(root, height=40)
textExample.pack()
textExample.place(x=90, y=40)
  
txt = tkinter.Entry(width=80)
txt.place(x=90, y=10)
txt.insert(tkinter.END,"")
  
def  data_print():
    import requests
    get_url =txt.get()

    site = requests.get(get_url)
    data = BeautifulSoup(site.text, 'html.parser')
    textExample.insert(tkinter.END,data.find_all("p"))

    SAMPLE_DIR = "C:\\html_link"
 
    if not os.path.exists(SAMPLE_DIR):
    # ディレクトリが存在しない場合、ディレクトリを作成する
        os.makedirs(SAMPLE_DIR)       

    web_site=SAMPLE_DIR+"\\scraping_result.html"
    f = open(web_site, 'w',encoding='utf-8', errors='ignore')
    message=str(data.find_all("a"))

    datalist = []


    datalist.append('<html>\n')
    datalist.append('<head>\n')
    datalist.append('<title>from python</title>\n')
    datalist.append('</head>\n')
    datalist.append('<body>\n')
    datalist.append(message)
    datalist.append('\n')
    datalist.append('</body>\n')
    datalist.append('</html>\n')

    f.writelines(datalist)

    f.close()
    webbrowser.open(web_site)

       
      
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

# 表示


def change_fill():

    # 現在選択されている項目のインデックスを取得
    indices = listbox.curselection()

    if len(indices) != 1:
        # ２つ以上選択されているor１つも選択されていない
        return

    # 項目を取得
    index = indices[0]
    color = listbox.get(index)

    # 取得した項目で長方形の色を変更
    txt.delete(0, tkinter.END) 
    txt.insert(tkinter.END,color)



# リストボックスの作成と配置
listbox = tkinter.Listbox(
    root,
    width=55, 
    height=5
)
listbox.grid(row=20, column=10, padx=10, pady=10)


# リストボックスに項目追加
colors = [
    "https://news.yahoo.co.jp/categories/domestic",
    "https://news.yahoo.co.jp/categories/sports",
    "https://news.yahoo.co.jp/categories/entertainment", 
    "https://news.yahoo.co.jp/categories/business", 
    "https://news.yahoo.co.jp/topics/top-picks"
]
for color in colors:
    listbox.insert(tkinter.END, color)

# ボタンの作成と配置
button = tkinter.Button(
    root,
    text="URLセット",
    command=change_fill
)
button.grid(row=1, column=1, padx=10, pady=10)



root.mainloop()
