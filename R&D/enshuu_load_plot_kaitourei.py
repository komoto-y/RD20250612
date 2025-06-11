# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 10:16:18 2025

@author: komoto_univ
"""

import numpy as np
import matplotlib.pyplot as plt
import glob

file='dataset/GraphData1.csv'

data = np.loadtxt(file,delimiter=',',skiprows=1) # 1000行2列の行列がロードされる
x = data[:,0] #dataの0列目
y = data[:,1] #dataの1列目

plt.plot(x,y,'r')#'r'は色が赤の実線であることを示す
plt.xlim(0,200)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


"""
dataset/uv-visのファイル内のスペクトルを可視化してください。
1)　spec1.csvのファイルを読み取りグラフにしてください。
2) 以下のfilesが何かをprintして確認してください。
3) 全てのスペクトルを1枚のグラフに描画してください。
4) 全てのスペクトルを個別のグラフで描画してください。
5) グラフの700nm以上の部分を0にしてください。
6)　スペクトルの250nm以上の最大の強度を求めてください。
以下にプログラムを記入
"""
## 1
file = 'dataset/uv-vis/spec1.csv'

data = np.loadtxt(file,delimiter=',',skiprows=1) 
x = data[:,0] #dataの0列目
y = data[:,1] #dataの1列目

plt.plot(x,y)
plt.xlabel('Wavelength / nm')
plt.ylabel('Intensity')
plt.show()

files = glob.glob('dataset/uv-vis/*.csv')

## 2
print(files)


## 3
for file in files:
    data = np.loadtxt(file,delimiter=',',skiprows=1)
    
    x = data[:,0]
    y = data[:,1]
    
    plt.plot(x,y)
    
plt.xlabel('Wavelength / nm')
plt.ylabel('Intensity')
plt.show()

## 4
for file in files:
    data = np.loadtxt(file,delimiter=',',skiprows=1)
    
    x = data[:,0]
    y = data[:,1]
    
    plt.plot(x,y)
    
    plt.xlabel('Wavelength / nm')
    plt.ylabel('Intensity')
    plt.show()

## 5 & 6
for file in files:
    data = np.loadtxt(file,delimiter=',',skiprows=1)
    
    x = data[:,0]
    y = data[:,1]
    
    y[x>700] = 0 # 5
    print('250nm以上の最大強度は',np.max(y[x>250])  ) # 6
    
    plt.plot(x,y)
    
plt.xlabel('Wavelength / nm')
plt.ylabel('Intensity')
plt.show()



