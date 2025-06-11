# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 10:54:30 2025

@author: komoto_univ
"""
import numpy as np
import pandas as pd
# =============================================================================
# 集計:
# 　Pandasのデータの集計を行います．Age列の平均値を計算してください。データは以下のものを使います
# ・Name: 'Alice', 'Bob', 'Charlie'
# ・Age: 25, 30, 35
# 
# =============================================================================

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)
print(df)
average_age = df['Age'].mean()
print(average_age)

print('========================================')
# =============================================================================
# 欠損値の処理:
# 
# 　任意の欠損値を含むデータフレームを作成し、欠損値を0で埋めてください。データとしては以下のものを用います．
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, np.nan, 35]
# 
# =============================================================================


data_missing = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, np.nan, 35]
}

df_missing = pd.DataFrame(data_missing)
print(df_missing)
df_filled = df_missing.fillna(0)
print(df_filled)

print('========================================')
# =============================================================================
# 列の追加と削除:
# 
# 　新しい列Cityをデータフレームに追加し、任意の値を割り当ててください。その後、City列を削除してください。もともとのデータとして以下のものを用います．
#  'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35]
# 追加するCityのデータは以下のものです．
# 'City'：['New York', 'Los Angeles', 'Chicago']
# 
# =============================================================================


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

print(df)
df['City'] = ['New York', 'Los Angeles', 'Chicago']
print(df)
df = df.drop(columns=['City'])
print(df)

print('========================================')
# =============================================================================
# データの結合:
# 
# 　2つのデータフレームを作成し、それらを結合して新しいデータフレームを作成してください。データは以下のものを用いてください
# ・data1:
# 　Name: 'David', 'Edward', 'Fiona'
# 　Age: 40, 45, 50
# ・data2:
# 　Name: 'George', 'Hannah', 'Ian'
# 　Age: 55, 60, 65
# =============================================================================


data1 = {'Name': ['David', 'Edward', 'Fiona'], 'Age': [40, 45, 50]}
data2 = {'Name': ['George', 'Hannah', 'Ian'], 'Age': [55, 60, 65]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1, df2)

df_combined = pd.concat([df1, df2], ignore_index=True)

print(df_combined)


