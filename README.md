# weather research

## プログラムの内容
気象庁が公開しているデータのうち、日別の最高気温・最低気温のデータおよび日別の降水量のデータを使用し、前者は1年間のデータの分布をまとめた散布図に、後者は日ごとの折れ線グラフにした。  
それぞれのデータは観測地点ごとに別のフォルダにCSVで保存されていて、最高気温・最低気温のデータは **maxmin_{西暦}.csv** という名前で年ごとに分かれており、降水量のデータは **rain.csv**という名前で10年分が一つのファイルに保存されている。  

ユーザーが対話的に設定できるパラメータは、両者に共通するものとして  
* プロットするデータの個数(1以上3以下)
* データの観測地点（札幌・東京・横浜・松本・那覇）
* 各データをプロットする色  
  
がある。  
  
気温データのみについてのパラメータとしては  
* 各データの年度  
  
がある。

降水量データのみについてのパラメータとしては  
* 描画する期間  
  
がある。
***
## 工夫したところ
プロットするデータの個数を変更すると自動でパラメータの入力欄の数も変化するようにJavaScriptでHTMLのクラスを付与・削除できるようにした。入力欄の数が自動で変わるたびにそれぞれの文章の位置が上下するとごちゃごちゃした印象を与えると思ったため、データの個数に応じて変化する入力欄の表示・非表示はCSSの *visibility: hidden;* で切り替えた。  
一方、プロットするデータの種類に応じて変化する部分は *visibility: hidden;* であると余計な空白が生まれてしまうため *display: none;* で対応した。  

***
## 苦労したところ
降水量のデータがまとまっている**rain.csv**が気象庁のHPからダウンロードしてきたままのデータであると、  

|年月日|降水量の合計(mm)|降水量の合計(mm)|降水量の合計(mm)|降水量の合計(mm)|  
|---|---|---|---|---|  
|　|　|現象なし情報|品質情報|均質番号|  
|2010/1/1|0|1|8|1|  
|2010/1/2|0|1|8|1|  
  
のようになっていて、indexにしたい行とデータが始まる行が離れている上にindexにしたい行の5個の見出しのうち4個が同じ名前になっているという点で困った。（なぜindexを2行に分けたのか、、、)  
そのためpandasでCSVを読み込む際に *names=(・・・)* で設定して読み込もうとしたが、そうするとなぜか *parse_dates=True*がうまく動かなかったため、ひとまず自分でCSVにindexにする行を書き加えた。  
|date|rain|a|b|c|  
|---|---|---|---|---|  
  
↑自分で書き加えた行  

***
## やりたりなかったこと
降水量のデータは棒グラフで表示したかったがmatplotlibのデフォルトの棒グラフの見栄えが気に入らなかったのでとりあえず棒グラフにした。細かい設定をする余裕があれば棒グラフに変更したいと思う。
***
## データの取得場所
* [気象庁HP](https://www.data.jma.go.jp/gmd/risk/obsdl/index.php)