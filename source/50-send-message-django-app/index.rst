========================================
チャットボットとやり取りできるようにする
========================================

前回まで
========================================

初回

- チャットボット＝自動応答するプログラム
- ライブラリ ``chatterbot`` を使ったPythonスクリプト

前回

- チャットボットをWebアプリとして動かすための **準備**
- Djangoを使って手元のPCで動くアプリケーションを開発
- チャットボットと会話できる

Djangoの設定

- プロジェクトとアプリケーション
- URL設定、ビュー、テンプレート

.. code-block:: shell

    $ cd ~/programming/chatbot
    $ source env/bin/activate
    $ cd app
    $ python manage.py runserver

開発tips：VSCodeの別のタブで :command:`runserver` しておく

http://127.0.0.1:8000/ をブラウザで開くと、真っ白い画面が表示されるようになっています（エラーを解決しながら設定しました）

（今回からの方向けに、前回の状態のファイルをzipにまとめて配布）

ここまでの実装内容

- URL設定：http://127.0.0.1:8000/ （パスが ``""`` （空文字列））へのリクエストに対しては、ビューの ``home`` （関数）を呼び出す
- ビュー： ``home`` 関数は、テンプレート ``chat/home.html`` を含んだレスポンスを返す
- テンプレート：空のHTMLファイルを置いただけ

``chat/home.html`` にHTMLを書くと、ブラウザに表示できます

チャットボットとやり取りできる画面を作る
========================================

フォーム
--------------------

.. literalinclude:: ../../app/chat/forms.py
    :language: python
    :caption: app/chat/forms.py

テンプレートにフォームを表示
----------------------------------------

ビュー

.. literalinclude:: ../../app/chat/views.py
    :language: python
    :caption: app/chat/views.py
    :lines: 4-10
    :emphasize-lines: 1,6,7

テンプレート

.. code-block:: html

    <!DOCTYPE html>
    <html lang="ja">
      <head>
        <meta charset="UTF-8" />
        <meta
          name="viewport"
          content="width=device-width, initial-scale=1, shrink-to-fit=no"
        />
        <title>Chatbot app</title>
      </head>
      <body>
        <h1>Talk with chatbot</h1>

        <form method="POST">
          {% csrf_token %} {{ form.as_p }}
          <button type="submit">Send</button>
        </form>
      </body>
    </html>

チャットボットが応答するURLを用意する
========================================

- http://127.0.0.1:8000/bot-response/ （フォームの ``action`` 属性に設定）
- フォーム入力されたデータの **POST** リクエストに対して、同じ ``message`` を返す

URL設定

ビュー

テンプレート

フォームからメッセージを送ると画面遷移を伴う状態

画面遷移なしでチャットボットとやり取りできる
================================================================================

画面遷移なしにする：ajax（JavaScriptを書く）。``jQuery`` を使用

テンプレートの ``<script>`` タグを書いていく

最終形

.. literalinclude:: ../../app/templates/chat/home.html
    :language: html
    :caption: app/templates/chat/home.html
    :lines: 19-58
    :emphasize-lines: 2, 4
