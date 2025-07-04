# -*- coding: utf-8 -*-
"""
以下の課題のcsvファイルでは0-4行目が特徴量、5行目が正解のラベルが書いてあります。

演習課題
1.以下のプログラムはSupport Vector Machineを用いて
  "Clf1_Train.csv" を学習して　"Clf1_Test.csv" のデータを分類を行うプログラムです。
　　プログラムを実行してください。

2.RandomForestを用いてtestdata中にある "Clf1_Train.csv" を学習して
　　Clf1_Test.csVのデータを分類して、F値を評価してください。

3.RandomForestを用いてtestdata中にある "Clf2_Train.csv" を学習して
　　Clf2_Test.csVのデータを分類して、F値を評価してください。
"""
print(__doc__)

import os 
import numpy as np
from ConfusionMatrix import plot_confusion_matrix #同階層にあるConfusionMatrix.pyからplot_confusion_matrixをload
from sklearn import metrics


##演習課題1は下のプログラムを実行

#ファイルパスの指定
file_train = 'dataset/Clf1_Train.csv'
file_test = 'dataset/Clf1_Test.csv'

#データの読み込み
#学習用データ
#特徴量の読み込み
x_train = np.genfromtxt(file_train,usecols = range(5),#csvファイルの0-5行目の読み込み
                        delimiter=',')#csvファイルのデータ区切りを指定
#ラベルの読み込み
y_train = np.genfromtxt(file_train,usecols = 5,#5行目の読み込み
                        dtype = 'U', #文字として読み込む
                        delimiter=',')

#テスト用データ
#特徴量の読み込み
x_test = np.genfromtxt(file_test,usecols = range(5),#csvファイルの0-5行目の読み込み
                        delimiter=',')#csvファイルのデータ区切りを指定
#ラベルの読み込み
y_test = np.genfromtxt(file_test,usecols = 5,#5行目の読み込み
                        dtype = 'U', #文字列(ユニコード)として読み込む
                        delimiter=',')
#読み込んだデータの確認
print(x_train)
print(y_train)
print(x_test)
print(y_test)
#機械学習ライブラリのインポート
# sklearnのsvmの中のSVCを読み込み
from sklearn.svm import SVC

#機械学習分類器の設定
clf = SVC()#何も指定がなければデフォルトのパラメータで設定される

#学習
clf.fit(x_train,y_train)#この後にデータを学習した分類器で分類ができるようになる。

#分類
y_pred=clf.predict(x_test)#学習した分類器でx_testを一つ一つ分類してy_predに入れる

#結果の確認
#混同行列の表示
plot_confusion_matrix(y_test,y_pred)

#f値の表示
print('F_measure',metrics.f1_score(y_test, y_pred , average='weighted') )


##　↓↓　ここから演習課題2を自分で記入
##   　演習課題１のプログラムを参考に

#ファイルパスの指定



#データの読み込み
#学習用データ
#特徴量の読み込み


#ラベルの読み込み



#テスト用データ
#特徴量の読み込み


#ラベルの読み込み



#機械学習ライブラリのインポート ここではRandomForestを使用
from sklearn.ensemble import RandomForestClassifier

#機械学習分類器の設定



#学習


#分類


#結果の確認
#混同行列の表示


#F値の表示
