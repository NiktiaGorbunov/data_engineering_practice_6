import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    # df.info(memory_usage='deep')

    # # 1. Столбчатая диаграмма для параметра "albedo"
    # df['name'] = df['name'].astype(str)
    # plt.figure(figsize=(10, 6))
    # plt.bar(df['name'][:10], df['albedo'][:10], color='skyblue')
    # plt.title('Albedo for Different Asteroids')
    # plt.xlabel('Asteroid Name')
    # plt.ylabel('Albedo')
    # plt.xticks(rotation=45, ha='right')
    # plt.tight_layout()
    # plt.savefig('plots/plot_1')

    # # 2. Круговая диаграмма для параметра "pha"
    # plt.figure(figsize=(8, 8))
    # df['pha'].value_counts().plot.pie(autopct='%1.1f%%', colors=['skyblue', 'lightcoral'], startangle=90)
    # plt.title('PHA распределение')
    # plt.ylabel('')
    # plt.savefig('plots/plot_2')

    # # 3. Точечная диаграмма
    # plt.figure(figsize=(10, 6))
    # plt.scatter(df['sigma_a'], df['sigma_q'], s=100, alpha=0.7)
    # plt.title('Точечный график зависимости Sigma_a и Sigma_q')
    # plt.xlabel('Sigma_a')
    # plt.ylabel('Sigma_q')
    # plt.grid(True)
    # plt.tight_layout()
    # plt.savefig('plots/plot_3')

    # # 4. Линейный график для параметра "sigma_a"
    # df['name'] = df['name'].astype(str)
    # plt.figure(figsize=(10, 6))
    # plt.scatter(df['name'][:10], df['sigma_a'][:10], marker='o', color='skyblue')
    # plt.title('Сигма А для разных астероидов (первые 10)')
    # plt.xlabel('Asteroid Name')
    # plt.ylabel('Sigma A')
    # plt.xticks(rotation=45, ha='right')
    # plt.tight_layout()
    # plt.savefig('plots/plot_4')

    # # 5. Тепловая карта
    # numeric_columns = df.select_dtypes(include=['float32', 'float64']).columns
    # corr_matrix = df[numeric_columns].corr()
    # plt.figure(figsize=(10, 6))
    # sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
    # plt.title('Heatmap of Correlation Matrix (Numeric Features Only)')
    # plt.savefig('plots/plot_5')

if __name__ == "__main__":
    create_graphs()