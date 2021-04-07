# 時系列識別
時系列（時間とともに変化する波形）の識別をしてみましょう．

## データ
level1～level4の4種類用意しています．各levelにはreferenceとtestの2種類フォルダがあり，それぞれに*.datという名前で時系列データが入っています（タブ区切りテキストです）．reference: 基準データとして，異なるクラス（属性）の2種類のデータが入っています（1.datがクラス1，2.datがクラス2）．波形を見れば違う性質のデータであることがわかると思います．  
test: ランダムな順番でクラス1かクラス2どちらかに属するデータが入っています（番号とクラスは無関係）．  
referenceフォルダ内の波形を基準にしてtestフォルダ内の各波形との距離をDPで計算し，testフォルダ内の各データファイルがどちらのクラスか当てるゲームです．  

### ＜level1＞
加速度計を腕につけて振った時の計測データです．  
時系列長が30で固定された1次元波形となっています．  
正しく計算すれば100%正解可能なデータです．  

### ＜level2＞
level1と同じ加速度データですが，3次元波形となっていますので距離計算をベクトルで考える必要があります．  
時系列長は30で固定です．  

### ＜level3＞
referenceはlevel2と同じデータですが，testデータがランダムに間引きされたり延長されたりしています．  
時系列長を可変にして考える必要があります．  

### ＜level4＞
level1～3とはかなり性質が違っており，実体は脳波データです．  
level3までと大きく異なる点は以下の2点です．  
1. 時系列長256で固定の64次元波形：  
　計算量がかなり多くなるので適当に間引きや次元選択/圧縮をする必要があるかもしれません．  
2. referenceに各クラス3つのデータを用意：  
　reference内のフォルダ1がクラス1，フォルダ2がクラス2のデータです．  
　各クラスで適当に1つずつ選んでもいいですし，平均をとるなどして3つをうまく組み合わせて使ってもokです．  
このデータセットはリカレントニューラルネットワークを使っても90%強しか正解できない難易度となっています．  

ひとまず正解は非公開としておきます（波形を見れば明らかなものもありますが）．  
回答を提出してくれれば正解率を返却します．  

## 認識手法
Dynamic time warping (DTW)を距離尺度として用いたk-nearest neighborを使ってみることをお勧めします．まずはscikit-learnなどのライブラリを用いて実装してみて，その後，完全スクラッチでDTWを実装してみると良いと思います．また，LSTMのようなrecurrent neural networkと比較してみることをお勧めします．

## 提出方法
使った手法の詳細をLaTeXでまとめpdfで提出してください．  
また，回答が知りたい方は，csvで認識結果を提出してください．  
抵抗が無ければ，ソースコードをgithubにアップロードしてそのリンクを教えてください．

# Time series classification
Classify time series data.  

## Dataset
We have four types of datasets from level1 to level4. Each level has two folders, reference and test, each containing time series data named *.dat (tab-delimited text).   
The reference contains two types of reference data for different classes (attributes) (1.dat and 2.dat are for classes 1 and 2, respectively). You can see from the waveforms that they have different properties.  
The test contains data belonging to either class 1 or class 2 in a random order.  
Use dynamic programming to calculate the distance between the waveform in the reference folder and each waveform in the test folder, and estimate which class each data file in the test folder belongs to.  

### level1
This is the data measured by shaking an accelerometer on your arm.  
It is a 1D waveform with a fixed time series length of 30.  
The recognition accuracy can be 100% if you calculate the distances correctly.  

### level2
This is the same acceleration data as level1, but it is a 3D waveform, so you need to consider the distance calculation as a vector.  
The time series length is fixed at 30.  

### level3
The reference is the same data as level2, but the test data is randomly resampled or extended.  
It is necessary to consider a variable time series length.  

### level4
The nature of this dataset is quite different from level1&ndash;3. This is EEG data.  
The following two points are the major differences from level1&ndash;3.  
1. 64-dimensional waveform with a fixed time series length of 256.  
　You may need to do some resampling or dimension selection/compression to save the computational costs.  
2. Three samples are prepared for each class in the reference dir.  
　Directories 1 and 2 are for classes 1 and 2, respectively.  
　Process reference samples appropriately, e.g., you can choose one sample for each class, or combine three samples by taking the average.  
FYI: The recognition accuracy is about 90% with a recurrent neural network.  

The correct answers will be kept secret for now (although some of them are obvious from the waveforms).  
If you submit your answers, I will return the recognition accuracy.  

## Recognition method
I recommend you to use k-nearest neighbor using dynamic time warping (DTW) as a distance measure. First, you can implement it using a library such as scikit-learn, and then try to implement DTW completely from scratch. It is also recommended to compare it with recurrent neural networks such as an LSTM.

## How to submit
Summarize the details of the method using LaTeX and submit in a pdf file.  
If you want to know the answer, please submit the recognition results in a csv format.  
If you don't mind, please upload the source code to github and provide the link to it.

