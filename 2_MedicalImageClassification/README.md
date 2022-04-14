# 医用画像識別
MRI画像の腫瘍の有無による識別をしてみましょう．

## データ
Datasetディレクトリにデータが入っています．  
> Dataset/  
> 　├ train.tar.gz  
> 　　　├ 0/  
> 　　　　　├ 1.png  
> 　　　　　├  :  
> 　　　　　└   
> 　　　└ 1/  
> 　├ val.tar.gz  
> 　└ test.tar.gz  
0が腫瘍無し，1が腫瘍あり画像です．  

## 方法 
* trainディレクトリに入っているデータを学習データとして，testディレクトリに入っているデータの認識をしましょう
* valディレクトリに入っているデータは検証データとして用い，epoch数やハイパーパラメータの調整に使ってください
* 識別器は何を使ってもOKですし，複数試してみるとなお良いです
* 特に今後のためにCNNは試してみましょう
* ちなみに[VGG-16](https://arxiv.org/abs/1409.1556)を用いて85~90%位の認識率です

## 提出方法 
* 以下の内容ををtexでまとめてpdfで提出してください
	* 必須：用いた手法の内容と認識率，混同行列
	* 推奨：正解・不正解した画像の傾向解析
* 抵抗が無ければ，ソースコードをgithubにアップロードしてそのリンクを教えてください

# Medical Image Classification
Classify MRI images by the presence or absence of tumors.

## Dataset
The dataset is stored in the Dataset directory.  
> Dataset/  
> 　├ train.tar.gz  
> 　　　├ 0/  
> 　　　　　├ 1.png  
> 　　　　　├  :  
> 　　　　　└   
> 　　　└ 1/  
> 　├ val.tar.gz  
> 　└ test.tar.gz  
0 is no tumor, 1 is with tumor.  

## Method 
* Use data in the train directory as training data to classify data in the test directory.  
* Use data in the val directory as validation data to adjust the number of epochs and hyperparameters.  
* You can use any classifier, and it is even better to try multiple ones!  
* If you try multiple classifiers, it is strongly recommended to include a convolutional neural network.  
* FYI: The recognition rate is about 85~90% using [VGG-16](https://arxiv.org/abs/1409.1556).

## How to submit 
* Write a paper using LaTeX and submit it in a pdf file with the following information.
	* Required: description of the method used, recognition rate, confusion matrix.  
	* Recommended: Detailed analysis of results (e.g., trend analysis of correct/incorrect images).  
* If you don't mind, please upload the source code to github and provide the link to it.

