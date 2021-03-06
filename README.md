# Hangman GUI Game

hangman game についてGUIで遊ぶゲームです。

## Description
ゲーム内容に関しては、START画面（[ハングマン (ゲーム)（Wikipedia）](https://ja.wikipedia.org/wiki/%E3%83%8F%E3%83%B3%E3%82%B0%E3%83%9E%E3%83%B3_(%E3%82%B2%E3%83%BC%E3%83%A0))）に記載のある通り、ランダムに設定されたアルファベットのの単語を予想し、その単語に含むと思われるアルファベット1文字を入力します。
正解ならば、解答のアルファベットが表示され、不正解ならhangmanの絵が一部描写されます。
hangmanの絵が完成する前に、解答を当てるゲームです

## Use
「NEW START」を押すとGame画面に移動するので、入力ボックスにアルファベットを入力します。
「遊び方に戻る」で遊び方の説明に戻ります。ゲーム画面に戻るには「back」を押します。
ゲームが開始した状態で遊び方説明画面から、「NEW START」を押すとゲーム内容が初期化されて、restartになります。

「demo画像」

<img src=demo/demo1.png width="350"> <img src=demo/demo2.png width="350"> <img src=demo/demo3.png width="350">
<!-- ![main_screen](demo/demo1.png)![demo2](demo/demo2.png)![demo3](demo/demo3.png) -->

## Requirement（動作環境）
- macOS Mojave
- Python 3.0以上

## Purpose
- GUI ライブラリの学習
- オブジェクト指向の書き方の学習

## Reference（hangman）
[独学プログラマー Python言語の基本から仕事のやり方まで(Amazon)](https://www.amazon.co.jp/dp/B07BKVP9QY/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)

## 課題とか、気になったこととか
