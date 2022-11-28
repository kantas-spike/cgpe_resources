# スクリプティングの例

CG制作演習で学んだスクリプティングの講義をもとに、
自分でスクリプトを作成しました。

いずれのスクリプトも、ターミナルからBlenderコマンドと共に起動することを想定しています。

~~~shell
/Applications/Blender.app/Contents/MacOS/Blender -P スクリプトファイルのパス
~~~

## ハローを表示する

https://youtu.be/HdwLHx9Sgv8 で紹介したPythonスクリプトです。

### [hello.py](hello.py)

ターミナル内に"hello!!"とだけ表示して、そのままBlenderを起動するスクリプト

~~~shell
/Applications/Blender.app/Contents/MacOS/Blender -P ./hello.py
~~~

### [hello_v2.py](hello_v2.py)

Blenderをスプラッシュ画面を非表示で起動し、不要な立方体を削除するスクリプト


### [hello_v3.py](hello_v3.py)

[hello_v2.py](hello_v2.py)に、出力とRigid Body Worldの設定を追加したスクリプト

### [hello_v3.1.py](hello_v3.1.py)

[hello_v3.py](hello_v3.py)を整理して、関数にしたスクリプト

### [hello_v4.py](hello_v4.py)

[hello_v3.1.py](hello_v3.1.py)に、実験ルームとライト、カメラを追加し、渦とハローという文字メッシュを追加したスクリプト

### [hello_v5.py](hello_v5.py)

[hello_v4.py](hello_v4.py)を修正し、配列に定義された文字から文字メッシュを追加するスクリプト

## 字幕ファイルから文字を表示する

### [create-subtitles-movie.py.py](create-subtitles-movie.py.py)

SubRip形式の字幕ファイルから文字を表示するスクリプト

ターミナルから、以下のように使います。

~~~shell
/Applications/Blender.app/Contents/MacOS/Blender -P ./create-subtitles-movie.py.py -- ./50on.srt -s 25
~~~

Blenderのコマンドライン引数の`--`以降の引数が、`create-subtitles-movie.py.py`への引数になります。

`--`以降に`-h`を

~~~shell
% /Applications/Blender.app/Contents/MacOS/Blender -P ./create-subtitles-movie.py.py -- -h
Read prefs: /Users/kanta/Library/Application Support/Blender/3.3/config/userpref.blend
hello!!
['-h']
usage: create-subtitles-movie.py [-h] [-s MOVIE_SEC] SRT_FILE

指定された字幕ファイルの内容をムービーに変換する

positional arguments:
  SRT_FILE              SubRip形式の字幕ファイルのパス

options:
  -h, --help            show this help message and exit
  -s MOVIE_SEC, --sec MOVIE_SEC
                        作成するムービーの長さ(秒). デフォルト値: 60
Saved session recovery to '/var/folders/8b/__pw1f4s56j1617cbx4qmq740000gp/T/quit.blend'
~~~

### [my_blender.py](my_blender.py)

`hello_*.py`でBlender操作に利用した関数を外部モジュールにしたもの

### [my_srt.py](my_srt.py)

SubRip形式の字幕ファイルを解析するモジュール

### [50on.srt](50on.srt)

[SubRip形式](https://ja.wikipedia.org/wiki/SubRip)の字幕ファイル

[北原白秋さんの「五十音」](https://ja.wikisource.org/wiki/%E4%BA%94%E5%8D%81%E9%9F%B3_(%E5%8C%97%E5%8E%9F%E7%99%BD%E7%A7%8B))を一部抜粋、改変したもの
