import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

pd.set_option("display.max_rows", 20, "display.max_columns", 60)


def read_types(file_name):
    dtypes = {}
    with open(file_name, mode='r') as file:
        dtypes = json.load(file)

    for key in dtypes.keys():
        if dtypes[key] == 'category':
            dtypes[key] = pd.CategoricalDtype
        else:
            dtypes[key] = np.dtype(dtypes[key])

    return dtypes

def create_graphs():
    need_dtyps = read_types('dtypes.json')
    df = pd.read_csv('df.csv', usecols=lambda x: x in need_dtyps.keys(), dtype=need_dtyps)

    # 1. Гистограмма для firstSeen
    plt.figure(figsize=(10, 5))
    df['firstSeen'] = pd.to_datetime(df['firstSeen'])
    plt.hist(df['firstSeen'], bins=30, color='skyblue')
    plt.title('Гистограмма для первого появления')
    plt.xlabel('Дата первого появления')
    plt.ylabel('Частота')
    plt.savefig('plots/plot_1')

    # 2. Столбчатая диаграмма для color
    events_by_color = df['color'].value_counts()
    threshold = 10
    top_colors = events_by_color.head(threshold)
    plt.figure(figsize=(10, 8))
    top_colors.plot(kind='bar', color='skyblue')
    plt.title('Столбчатая диаграмма для 10 самых популярных цветов')
    plt.xlabel('Цвет')
    plt.ylabel('Число автомобилей')
    plt.xticks(rotation=45)
    plt.savefig('plots/plot_2')

    # 3. Круговая диаграмма для brandName
    plt.figure(figsize=(8, 8))
    events_by_brand = df['brandName'].value_counts()
    threshold = 10
    top_brands = events_by_brand.head(threshold)
    remaining_brands = events_by_brand.iloc[threshold:]
    remaining_brands_sum = remaining_brands.sum()
    top_brands = pd.concat([top_brands, pd.Series([remaining_brands_sum], index=['Остальные'])])
    plt.pie(top_brands, labels=top_brands.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Круговая диаграмма для брендов')
    plt.savefig('plots/plot_3')

    # 4. Категориальный график (Countplot) для dealerID
    top_values_cat1 = df['color'].value_counts().head(10).index
    top_values_cat2 = df['brandName'].value_counts().head(10).index
    df_filtered = df[df['color'].isin(top_values_cat1) & df['brandName'].isin(top_values_cat2)]
    contingency_table = pd.crosstab(df_filtered['color'], df_filtered['brandName'])
    plt.figure(figsize=(8, 6))
    sns.heatmap(contingency_table, annot=True, fmt='d', cmap='coolwarm', cbar=False)
    plt.title('Тепловая карта для 10 наиболее часто встречающихся цветов и брендов')
    plt.savefig('plots/plot_4')

    # 5. диаграмма
    df['firstSeen'] = pd.to_datetime(df['firstSeen'])
    df['quarter'] = df['firstSeen'].dt.to_period('Q')
    average_price_by_quarter = df.groupby('quarter')['askPrice'].mean()
    plt.figure(figsize=(10, 5))
    average_price_by_quarter.plot(kind='line', marker='o', color='skyblue', linestyle='-', linewidth=2)
    plt.title('Средняя цена на каждый квартал')
    plt.xlabel('Квартал')
    plt.ylabel('Средняя цена')
    plt.xticks(rotation=45)
    plt.savefig('plots/plot_5')

if __name__ == "__main__":
    create_graphs()