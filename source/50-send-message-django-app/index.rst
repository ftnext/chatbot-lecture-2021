========================================
チャットボットとやり取りできるようにする
========================================

.. include:: 0-intro.rst.txt

.. include:: 1-skeleton-screen-to-chat.rst.txt

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
