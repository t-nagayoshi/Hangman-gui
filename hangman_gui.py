import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import random


# 親クラスのtk.Tkを継承、root（window）の設定
class Hangman_app(tk.Tk):
    frame = list()

    def __init__(self):
        tk.Tk.__init__(self)
        # self._frame = None
        self.color = "aliceblue"
        self.title("hangman")
        self.geometry("580x360")
        self.configure(bg=self.color)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frame = [StartPage(master=self), Application_Drawing(master=self)]
        self.frame[0].grid(row=0, column=0, sticky="nsew")

    # NEW GAME
    def start_frame(self, event):
        new_frame = Application_Drawing(master=self)
        if self.frame[1] is not None:
            self.frame[1].destroy()
        self.frame[1] = new_frame
        self.frame[1].grid(row=0, column=0, sticky="nsew")
        self.frame[0].grid_remove()

    def switch_frame(self, event):
        # # StartPageなら、Application_Drawingに切り替える
        self.index = 0 if self.frame[0].button2 == event.widget else 1
        self.frame[(self.index + 1) % 2].grid()
        self.frame[(self.index + 1) % 2].tkraise()
        self.frame[self.index % 2].grid_remove()

    # # game画面と説明画面の入れ替え、既存のframeを破壊して、入れ替える
    # def switch_frame2(self, event):
    #     if ".!startpage" in str(event.widget):
    #         new_frame = Application_Drawing(master=self)
    #     if ".!application_drawing" in str(event.widget):
    #         new_frame = StartPage(master=self)
    #     if self._frame is not None:
    #         self._frame.destroy()
    #     self._frame = new_frame
    #     self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg=master.color)
        # self.pack()
        self.text = tk.Label(self, text="遊び方(wikiから)", font=('Helvetica', 20, "bold"))
        self.button1 = tk.Button(self, text="NEW START", fg="blue")
        self.button1.bind("<Button-1>", master.start_frame)
        self.button1.bind("<Key-Return>", master.start_frame)
        self.button2 = tk.Button(self, text="back", fg="blue")
        self.button2.bind("<Button-1>", master.switch_frame)
        self.button2.bind("<Key-Return>", master.switch_frame)

        self.t = ["1. 出題者は出題する単語を選び、その単語の文字数を表す下線を引く。絞首台を描く。",
                  "2. 解答者は、単語に入っていると思われるアルファベットを一つ答える。",
                  "3. 出題者はアルファベットが回答の単語に含まれているか判定する。",
                  "・アルファベットが単語に含まれているならば、",
                  " 下線の上のその文字が入る場所すべてにその文字を書く。",
                  "・アルファベットが単語に含まれていないならば、絞首台につるされる人の絵を描き加える。",
                  "4.勝敗が決まるまで2.3.を繰り返す。以下のときに勝敗は決まる。",
                  "・解答者が単語を正解する。-解答者の勝利",
                  "・絞首台の人の絵が完成する。-出題者の勝利"]

        # 配置
        self.text.pack(side="top", pady=10)
        for i in range(len(self.t)):
            self.explanation = tk.Label(self, text=self.t[i], bg=self.master.color)
            self.explanation.pack(anchor="w")
        self.button1.pack(pady=10)
        self.button2.pack(pady=10)

class Application_Drawing(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=200, height=160)
        # tk.Frame.__init__(self, master)
        # window背景色
        self.configure(bg=master.color)
        # rootの方でpackする
        # self.pack(pady=10)
        self.hangman = Hangman()
        self.input_guess = self.hangman.input_guess
        self.textbox_hide_judge = self.hangman.textbox_hide_judge
        self.stages = self.hangman.stages
        self.answer = self.hangman.answer_Column

        self.text_display(self.stages)
        self.answer_diplay(self.answer)
        self.textbox()
        self.startbutton()

    # 画面更新
    def update(self, stages, answer):
        for i, astage in enumerate(stages):
            self.label_han[i]["text"] = astage
        self.label["text"] = '  '.join(answer)

    # 不正解ならば、ハングマン表示
    def text_display(self, stages):
        self.label_han = list()
        for text in (stages):
            self.label = tk.Label(self, text=text, fg="white", bg="black")
            self.label.pack(fill=tk.BOTH)
            self.label_han.append(self.label)

    # 答えとなる文字列ラベルの表示
    # 正解ならば、正解した文字を表示させる（1文字）
    def answer_diplay(self, answer):
        fontStyle = tkFont.Font(family="Lucida Console", size=30)
        self.label = tk.Label(self, text='  '.join(answer), font=fontStyle)
        self.label.pack(pady=20)

    # テキストボックスの表示
    def textbox(self):
        self.textbox = tk.Entry(self, width=5)
        self.textbox.pack(pady=20)
        self.textbox.bind("<Key-Return>", self.getTextInput)

    # テキストボックスから値を取得する
    def getTextInput(self, event):
        letter = event.widget.get()
        # エラー表示
        if not (letter.isalpha() and len(letter) == 1):
            res = tk.messagebox.showwarning("警告", "1文字の英文字ではありません。")
            # macで起こるエラー対策
            tk._default_root.grab_set()
            tk._default_root.grab_release()

        # 正解ならば、答えの欄を更新、不正解ならば、ハングマンの絵を更新
        # ここで行うのは文字を渡すこと
        else:
            res = self.input_guess(letter)
            self.update(self.stages, self.answer)

        event.widget.delete(0, tk.END)
        # 完成 or 回数分間違えた処理
        res = self.textbox_hide_judge()
        if res:
            self.textbox.pack_forget()
            res = "正解は" + self.hangman.answer_word if res == 'Lose!' else res
            self.win_label = tk.Label(self, text=res, width=25, fg="red", bg=self.master.color, font=("", 20))
            self.win_label.pack(pady=10)

    # 説明ボタンの表示
    def startbutton(self):
        self.button = tk.Button(self, text="遊び方に戻る", fg="blue")
        self.button.bind("<Button-1>", self.master.switch_frame)
        self.button.bind("<Key-Return>", self.master.switch_frame)
        self.button.pack(side=tk.BOTTOM, pady=5)

class Hangman():
    lose_stages = (r"|________________________",
                   r"|            |           ",
                   r"|            |           ",
                   r"|            0           ",
                   r"|           /|\          ",
                   r"|           / \          ",
                   r"|                        ")

    def __init__(self):
        self.wrong = 0
        self.stages = [r"|                        "] * len(self.lose_stages)
        self.answer_word = self.random_answer()
        self.answer_Column = ["_"] * len(self.answer_word)

    # 答えの word をランダムに返す
    def random_answer(self):
        word_list = ["Python", "Java", "Ruby", "HTML", "PHP",
                     "COBOL", "Javascript", "Kotlin", "Scala"]
        random_number = random.randint(0, len(word_list) - 1)
        return word_list[random_number]

    # 推測した文字が答えに含まれているかの判定、各変数の更新
    def input_guess(self, guess):
        if guess.lower() in self.answer_word or guess.upper() in self.answer_word:
            # 解答の何文字目に答えた文字があるのか
            index_num = [n for n, v in enumerate(self.answer_word) if v == guess.lower() or v == guess.upper()]
            for i in index_num:
                self.answer_Column[i] = self.answer_word[i]
        else:
            self.stages[self.wrong] = self.lose_stages[self.wrong]
            self.wrong += 1

    # 完成 or 回数分間違えたときにテキストボックスを消滅させる
    def textbox_hide_judge(self):
        if "_" not in self.answer_Column:
            return "Win!"
        elif self.wrong == len(self.lose_stages):
            return "Lose!"
        else:
            return False

def main():
    root = Hangman_app()
    root.mainloop()

if __name__ == "__main__":
    main()
