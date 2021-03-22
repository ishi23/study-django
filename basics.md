## Djangoとは
- pythonのフレームワーク
- Webアプリ作成

## フレームワークとは？
- webサイトを料理としたら、各プログラムが材料である
- フレームワークはシステムキッチンに該当する
- 料理をするために必要なツールが準備されている

## Bootstrap
- 見た目を操るCSSを予め用意してある

## Django2 と Django3
- 2020年にDjango3がリリース

## webサイトの動き
- httpプロトコルでリスエストを出す　→　サーバーがレスポンス（データ）を返す

## ローカルホスト 127.0.0.1:8000
- 通常全世界で被らないIPアドレスが配布されており、ユニークなアドレスとなっている
- 127.0.0.1は配布されておらず、常に自分を指す

## 環境構築
- `pip install django`
- 自分は練習用環境としてはMacでpython=3.8のpipenv仮想環境で構築

## ファイル
- プロジェクトを作成すると、プロジェクト名のフォルダが作成される。
- その中では主にsettings.pyとurls.pyを管理、編集する
- アプリを作成すると同じ階層にアプリ名のフォルダが作成される。
- その中では主にviews.py、またurls.pyはデフォルトで入っていないが作成する。
- プロジェクト側のurls.pyでリクエストを受けて全てを処理することもできるが、アプリ側にurls.pyを作ることで、多段的に受けられる
- つまりプロジェクト側のurls.pyはurl(リクエスト)を見て各アプリ（のurls.py）に振り分け、各アプリ側で処理する。これにはinclude()を使う。
- views.pyの中に実装するviewにはfuction based view と class based view がある

# プロジェクト名フォルダの中身

## settings.py
- Webアプリの管理周りの設定
- デフォルトで色々入っているが、カスタムする
- INSTALLED_APPSにアプリを追加していく
- 本リポジトリ内のプロジェクト内のsettings.pyにメモ書き

## urls.py
- アクセスURL（リクエスト）に対して処理を規定する。
- デフォルトでは"admin/"に対して管理者ログイン画面を返す
- 本リポジトリ内のプロジェクト内のurls.pyにメモ書き

## アプリ名フォルダの中身

## views.py
- urlsで使う処理を規定しておく
- Djangoで用意されたTamplateから持って来れる
- ListViewクラス：リスト型の表示に適したViewクラス
- template_name = 'templatename.html'
- model = modelclassname defined in models.py

## models.py
- DBを使う際に使う
- クラス定義：中に変数(項目)とフィールドを準備
- `python manage.py makemigration <app_name>` で DBにテーブルを作成するためのスクリプトが作成される。これはコマンド毎に新規に作成されるので過去ver保存の意味合いもある。また中身のチェックもされる。
- `python manage.py migrate` でDBにテーブルが作成される


## admin.py
- 管理者画面で何を表示するか


## Djangoのhtml
- Django特有のHTMLタグ
- {{}} データ: 変数の表示
- {%%} 複雑な処理: for分とか

## Bootstrap
- CSSファイル
- web上のCSSを利用できる。多種多様な見た目を提供してくれている
- htmlコードは基本的にBootstrapのHPから選んでコピペ

## base.html
- Django特有のhtml共通化機能
- htmlを増やすと同じコードを部分的にたくさん書く事になる
- 共通部分に変更が生じた場合、全てのhtmlを変えなければいけない
- base.htmlというファイル名である必要はないが、慣習的にbase
- ブロック構造を共通化
- 各ブロックに何を表示させるかを各htmlで規定
- 各html側でbase.htmlから引っ張ってくることをコード{% extends 'base.html' %}を先頭に

