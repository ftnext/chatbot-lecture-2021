========================================
チャットボットとやり取りできるようにする
========================================

.. include:: 0-intro.rst.txt

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
