========================================
チャットボットとやり取りできるようにする
========================================

.. include:: 0-intro.rst.txt

.. include:: 1-skeleton-screen-to-chat.rst.txt

.. include:: 2-chatbot-response-endpoint.rst.txt

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
