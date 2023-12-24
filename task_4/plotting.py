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

    # # 1. Гистограмма
    # df['salary_difference'] = df['salary_to'] - df['salary_from']
    # grouped_data = df.groupby('experience_name')['salary_difference'].mean().reset_index()
    # plt.figure(figsize=(10, 6))
    # sns.barplot(x='experience_name', y='salary_difference', data=grouped_data)
    # plt.title('Средняя разница между salary_from и salary_to в зависимости от опыта')
    # plt.xlabel('Опыт')
    # plt.ylabel('Средняя разница в зарплате')
    # plt.savefig('plots/plot_1')

    # # 2. Violin plot для поля "salary_to"
    # plt.figure(figsize=(10, 6))
    # sns.violinplot(x='salary_to', data=df.dropna(subset=['salary_to']))
    # plt.title('Violin plot: Распределение зарплат (salary_to)')
    # plt.xlabel('Зарплата (salary_to)')
    # plt.savefig('plots/plot_2')

    # # 3. Линейный график для зарплаты в зависимости от опыта
    # plt.figure(figsize=(12, 6))
    # sns.lineplot(x='experience_name', y='salary_from', data=df, marker='o')
    # plt.title('Линейный график: Зарплата в зависимости от опыта')
    # plt.xlabel('Опыт')
    # plt.ylabel('Зарплата (salary_from)')
    # plt.savefig('plots/plot_3')

    # # 4. Круговая диаграмма для соотношения валюты
    # plt.figure(figsize=(8, 8))
    # threshold = 3
    # events_by_currency = df['salary_currency'].value_counts()
    # top_currency = events_by_currency.head(threshold)
    # remaining_curr = events_by_currency.iloc[threshold:]
    # remaining_curr_sum = remaining_curr.sum()
    # top_currency = pd.concat([top_currency, pd.Series([remaining_curr_sum], index=['Остальные'])])
    # plt.pie(top_currency, labels=top_currency.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    # plt.title('Круговая диаграмма: Соотношение валюты')
    # plt.savefig('plots/plot_4')

    # # 5. Точечная диаграмма для сравнения "salary_from" и "salary_to"
    # plt.figure(figsize=(10, 6))
    # sns.scatterplot(x='salary_from', y='salary_to', data=df)
    # plt.title('Точечная диаграмма: Сравнение salary_from и salary_to')
    # plt.xlabel('Зарплата (salary_from)')
    # plt.ylabel('Зарплата (salary_to)')
    # plt.savefig('plots/plot_5')

if __name__ == "__main__":
    create_graphs()