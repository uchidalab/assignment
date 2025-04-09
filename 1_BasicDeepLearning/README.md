# 深層学習の基礎
深層学習の基礎と，[pytorch](https://pytorch.org/)の基本を学びましょう．

## 内容
0. python+pytorchのプログラミング環境構築
    * [labwiki](https://sites.google.com/human.ait.kyushu-u.ac.jp/labwiki/home)もしくは先輩方に聞きながら環境構築を行いましょう
    * Dockerを使った環境構築がおすすめです．[こちら](https://github.com/Kkun84/NvidiaDocker)が参考になると思います．
    * **有名な仮想環境としてanacondaがありますが使用は控えてください．**
1. 深層学習の基本
	* [pytorch turorial](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html) を参考にpytorchを使った深層学習の実装の流れを確認しましょう
	* Fashion-MNISTというデータを分類するモデルの構築ができれば目標達成です！
2. 深層学習の応用
    * 「1. 深層学習の基本」のプログラムを基に自分なりの工夫をして精度改善を行ってみましょう．
    * ヒント: Networkの層数を増やす，データ拡張，転移学習などなど

## 提出物（この他の内容を書いていただいても構いません）
* 「2. 深層学習の応用」での工夫点やその他考察
* 実験条件（データセット，学習時に使ったパラメータなど）
* 学習結果（精度の比較，学習曲線，混同行列など）

## 提出方法
LaTeXを使ってpdfファイルにまとめ提出してください．  
抵抗が無ければ，ソースコードをgithubにアップロードしてそのリンクを教えてください

# Basics of Deep Learning
Learn the basics of deep learning and programming using [pytorch](https://pytorch.org/).

## Contents
0. Build python+pytorch programming environment  
	* If you have any questions, please check [labwiki](https://sites.google.com/human.ait.kyushu-u.ac.jp/labwiki/home) or feel free to ask your colleagues.  
    * We recommend using Docker for the environment setup. [This repository](https://github.com/Kkun84/NvidiaDocker) may be helpful.
    * **Although Anaconda is a well-known virtual environment, please refrain from using it.**
1. Basics of deep learning
	* Check the implementation workflow of deep learning using PyTorch by referring to the [pytorch turorial](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html)
	* The goal is to build a model that classifies the Fashion-MNIST dataset. 
2. Applications of Deep Learning  
	* Based on the program from ``1. Basics of Deep Learning'' try to improve accuracy with your own ideas and modifications. 
    * Hints: Increase the number of network layers, use data augmentation, apply transfer learning, etc.

## Report
* Key ideas and additional insights in ``. Applications of Deep Learnin''
* Experimental setup (e.g., dataset, training parameters, etc.)
* Training results (e.g., accuracy comparison, learning curves, confusion matrix, etc.)

## How to submit
Write a paper using LaTeX and submit it in a pdf file.  
If you don't mind, upload the source code to github and send me the link.

