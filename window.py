import tkinter as tk
from tkinter import messagebox
import time


# 親クラスのtk.Frameを継承したApplication_Frame1クラスを作成
class Application_Frame1(tk.Frame):
    # ウィンドウ
    def __init__(self, master=None):
        # 親クラスの__init__メソッドを実行
        super().__init__(master, width=350, height=150)
        self.color = '#E3FFFD'
        self.configure(bg=self.color)
        self.pack(pady=15)
        self.create_label()
        self.create_spinbox()
        self.create_optionmenu()

    # 文字ラベル設定
    def create_label(self):
        label_text = ["初期作動時間（秒）　　　　　：",
                      "スクリーンショット時間（秒）：",
                      "スクリーンショット回数　　　：",
                      "キー入力方向　　　　　　　　：",
                      "保存フォーマット　　　　　　："]

        # グリッドに沿って縦に配置
        for i in range(len(label_text)):
            self.label = tk.Label(self, text=label_text[i], bg=self.color)
            self.label.grid(column=0, row=i)

    def create_spinbox(self):
        init_value = [5, 2.5, 3]
        to_i = [20, 5, 500]

        # グリッドに沿ってlabelの横に縦に配置
        for i in range(len(init_value)):
            # self.text = tk.Entry(self, width=10, highlightbackground=self.color)
            # self.text.insert(0, init_value[t[i]])
            # self.text.grid(column=1, row=i, sticky=tk.W)
            self.val = tk.StringVar()
            self.val.set(init_value[i])
            if i == 2:
                self.sp = tk.Spinbox(self, width=10, state="normal",
                                     textvariable=self.val, from_=1, to=to_i[i], increment=1)
            else:
                self.sp = tk.Spinbox(self, width=10, state="readonly",
                                     textvariable=self.val, from_=1, to=to_i[i], increment=0.1)
            self.sp.grid(column=1, row=i, sticky=tk.W)

    # オプションメニュー (ドロップダウンリスト)の設定
    def create_optionmenu(self):
        key_list_value = ["Right", "Left", "UP", "Down"]
        format_list_value = ["PDF", "PNG"]
        list_value = [key_list_value, format_list_value]

        # グリッドに沿って配置
        for i in range(len(list_value)):
            self.variable = tk.StringVar(self)
            self.variable.set(list_value[i][0])
            self.optm = tk.OptionMenu(self, self.variable, *list_value[i])
            self.optm.config(bg=self.color)
            self.optm.grid(column=1, row=i + 3, sticky=tk.W)

# 親クラスのtk.Frameを継承したApplication_Frame2クラスを作成
class Application_Frame2(tk.Frame):
    # ウィンドウ
    def __init__(self, master=None):
        # 親クラスの__init__メソッドを実行
        super().__init__(master, width=350, height=50)
        self.color = '#CFE3E8'
        self.pack(padx=20, ipadx=10, ipady=5)
        self.configure(bg=self.color)
        self.create_button()

    # ボタンの設定
    def create_button(self):
        # 各パラメーター
        self.button1 = tk.Button(self, text='実行', width=15, height=2)
        self.button2 = tk.Button(self, text='中断', width=15, height=2)
        self.button1.pack(padx=15, side=tk.RIGHT)
        self.button2.pack(padx=15, side=tk.LEFT)
        self.button1.bind("<Button-1>", self.btn_click)
        self.button1.bind("<Key-Return>", self.btn_click)
        self.button2.bind("<Button-1>", self.btn_click)
        self.button2.bind("<Key-Return>", self.btn_click)

    # ボタンが押されたときのコールバック関数
    def btn_click(self, event):
        t = ["実行", "中断"]
        res = tk.messagebox.askyesno(event.widget.cget("text") + "確認", "実行しますか？")
        # Mac上のTkinterのエラー対策
        tk._default_root.grab_set()
        tk._default_root.grab_release()
        if res:
            if event.widget.cget("text") == t[0]:
                print(t[0] + "します")
            if event.widget.cget("text") == t[1]:
                print(t[1] + "します")

def main():
    # Tkインスタンスを作成し、root変数に格納する
    root = tk.Tk()
    root.title('Auto_ScreenShot')
    root.geometry('380x250')
    root.configure(bg="aliceblue")
    # root.resizable(width=False, height=False)
    frame1 = Application_Frame1(master=root)
    frame2 = Application_Frame2(master=root)
    root.mainloop()

if __name__ == '__main__':
    main()
