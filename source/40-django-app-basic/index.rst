============================================================
Django基礎（チャットボットをWebアプリにするための準備）
============================================================

.. include:: 0-intro.rst.txt

.. include:: 1-django-overview.rst.txt

プロジェクト・アプリケーション作成
========================================

chatterbotを使った仮想環境にインストール

.. code-block:: shell

    $ pip install 'Django<4'

プロジェクト作成

.. code-block:: shell

    $ django-admin startproject djangochatbot
    $ mv djangochatbot app

settings.py を変更

アプリケーション作成

.. code-block:: shell

    $ python manage.py startapp chat

settings.py を変更（インストール）

テンプレートを表示する
========================================

http://127.0.0.1:8000/ でテンプレートを表示

1. URL設定（アプリケーションのURL設定を追加）
2. ビュー（関数を追加）
3. テンプレートを追加

真っ白な画面を表示（エラーがない状態）

テンプレートにHTMLを書く
