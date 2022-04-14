# 文字画像解析（フォントの印象分類）
フォント画像とその印象語が関連付けられたデータセットを用いて，特定の印象語に対し，フォント画像のOne-vs-Restの2クラス分類を行いましょう．

## データセットの準備
1. 以下のリンクから本ディレクトリにデータセットをダウンロード<br>https://www.cs.rochester.edu/u/tchen45/font/font.html
2. Dockerfileに従って環境構築
3. preprocess_data.pyを実行
-> dataset/fontimage_preprocessed/に前処理を施したフォント画像データが，fontName_tagWord.csvにフォントと印象後の関連付けリストがそれぞれ保存される．

## データセットに関する注意事項
上記のリンクからダウンロードしたデータセットでは，taglabelフォルダにblank fileがあるため，taglabel.zipを解凍したものと置き換える

## 内容
* データを任意の割合（7:3など）で学習データとテストデータに分割
* ある印象語を指定し（"formal"など），それに関連付けられているか否かを2値ラベルとしてフォント画像を識別するように識別器を学習
* テストデータを識別し，認識率とどのような画像が正しく（あるいは間違って）分類される傾向にあるか確認する

## 提出方法
結果をLaTeXでまとめ，pdfで提出してください．  
抵抗が無ければ，ソースコードをgithubにアップロードしてそのリンクを教えてください．

## 参考
本課題はやや難易度が高いため，卒業生が作成したコードを添付しています（reference.zip）．難しければそれを参考に実装してみてください．

# Text Image Analysis (Font Impression Classification)
Using a dataset with associated font images and their impression words, let's perform a two-class One-vs-Rest classification of font images for a particular impression word.

## Preparation of the dataset
1. Download the dataset from the following link to this directory<br>https://www.cs.rochester.edu/u/tchen45/font/font.html
2. Build the environment according to the Dockerfile.  
3. Run preprocess_data.py
-> the preprocessed font image data, and the list of fonts and their associations after impression will be stored in "dataset/fontimage_preprocessed/" and "fontName_tagWord.csv," respectively.

## Notes on the dataset
In the dataset downloaded from the link above, there is a blank file in the taglabel folder; so replace it with taglabel.zip after unzipping.

## Contents
* Split the data into training and test data in arbitrary proportions (e.g. 7:3)
* Specify an impression word (e.g. "formal"), and train a classifier to identify whether font images are associated with the specified word or not.
* Classify the test data, and check the recognition rate and what images tend to be classified correctly (or incorrectly).

## How to submit
Please summarize your results in LaTeX and submit them as a pdf file.  
If you don't mind, please upload the source code to github and provide the link.

## Reference
Since this assignment is rather difficult, I have attached the code created by an alumnus (reference.zip). If you find it difficult, please refer to it and try to implement it.



