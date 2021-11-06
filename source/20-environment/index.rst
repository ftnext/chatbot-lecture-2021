====================
環境構築
====================

現在のドキュメントのバージョンは、macOSを前提としています。

Pythonのバージョン
====================

確認しましょう

.. code-block:: shell

    $ python3 -V

（構築した方法によっては :command:`python` かもしれません）

**Python 3.7.x** で進めます。

インストールしていない場合は `Python 3.7 インストール方法 <https://scrapbox.io/nikkie-memos/Python_3.7_%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB_(2021%2F11%E6%99%82%E7%82%B9)>`_

作業ディレクトリを作る
========================================

以下のコマンドのディレクトリのパスは一例です。

.. code-block:: shell

    $ mkdir -p ~/programming/chatbot
    $ cd ~/programming/chatbot

仮想環境
====================

作業ディレクトリにいる状態を前提にしています（:command:`pwd` で確認しましょう）。

.. code-block:: shell

    $ python3.7 -m venv env
    $ source env/bin/activate
    (env) $ python -m pip install -U pip

プロンプトの ``(env)`` は仮想環境が有効になった状態を示します。

``ChatterBot`` インストール
========================================

.. code-block:: shell

    (env) $ pip install ChatterBot

2021/11時点では ``1.0.8`` がインストールされます。

この時点では対話モードで ``import chatterbot`` してもエラー（``ModuleNotFoundError``）が送出されます。
次の項目にて、依存するライブラリをインストールすることで解決します。
