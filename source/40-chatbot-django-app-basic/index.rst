今回の位置づけ
========================================

前回の復習
----------------------------------------

- チャットボット＝自動応答するプログラム
- ライブラリ ``chatterbot`` を使ったPythonスクリプトを動かした（デモ）

今回やること
----------------------------------------

チャットボットをWebアプリとして動かすための **準備** をします。

- Djangoを使って手元のPCで動くアプリケーションを開発していきます
- 今回チャットボットは触りません

DjangoによるWebアプリ
========================================

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2020_slides/pycon_shizu_Feb_django_intro/slide.html" title="Djangoで始めるWeb開発の世界 〜Web開発を知らない方に贈る、Django Girls Tutorialとその周辺のクイックツアー〜"></iframe>

押さえておきたいポイント

- URL設定
- ビュー
- テンプレート

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

チャットボットとやり取りできるようにする
========================================

フォーム

POSTする（オウム返し）

画面遷移を伴う状態

画面遷移なしにする：ajax（JavaScriptを書く）
