#! /usr/bin/env python3

import sys
import io

# windowsにおける文字化け回避
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# 以下のコードを書かないと、htmlとして読み込んでもらえない。
print("Content-type: text/html; charset=utf-8")

# htmlの部分。printでHTMLコードを表示させることで、ブラウザがHTMLコードとして認識してくれる。
print(
   """
     <html lang="ja">

    <head>
        <meta charset="utf-8">
        <title>コンタクト</title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>
    <header id="#header">
      <div class="header_icon">
        <a href="index.html"></a>
        <h1>どうも山田です。</h1>
        <p>Kento Yamada</p>
      </div>
      <nav>
        <ul>
           <li><a href="#introduction">自己紹介</a></li>
          <li><a href="#myhistory">経歴</a></li>
          <li><a href="#myhobby">趣味</a></li>
          <li><a href="#sns">近況報告</a></li>
          <li class="last_li"><a href="#contact">問い合わせ</a></li>
        </ul>
      </nav>
    </header>

    <section id="formform">
        <h1>問い合わせフォームに入力をお願いします。</h1>

        <form action="comp.py" method="post">
            <p>氏名or会社名</p>
            <input type="text" name="name"><br>
            <p>メールアドレス</p>
            <input type="text" name="mail"><br>
            <p>メッセージ</p>
            <textarea name="message" cols="30" rows="10"></textarea><br>

            <input type="submit" value="送信する">
        </form>
    </section>
    <footer>
        Copyright Kento Yamada All Rights Reserved.
   </footer>
    </body>
</html>
"""
)
