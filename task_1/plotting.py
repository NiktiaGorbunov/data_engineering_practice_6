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
    dataset = pd.read_csv('df.csv', usecols=lambda x: x in need_dtyps.keys(), dtype=need_dtyps)
    dataset.info(memory_usage='deep')
    # # Линейный график
    # dataset['date'] = pd.to_datetime(dataset['date'], format='%Y%m%d')
    # yearly_counts = dataset.groupby(dataset['date'].dt.year)['number_of_game'].sum().reset_index()
    # plt.figure(figsize=(15, 7))
    # plt.plot(yearly_counts['date'], yearly_counts['number_of_game'], marker='o', linestyle='-', color='b')
    # plt.title('Число игр по кварталам')
    # plt.xlabel('Квартал')
    # plt.ylabel('Число игр')
    # plt.grid(True)
    # plt.savefig('plots/plot_1')
    #
    # # Столбчатая диаграмма
    # plt.figure(figsize=(10, 5))
    # sns.countplot(x='day_of_week', data=dataset, palette='viridis', legend=False)
    # plt.title('Распределение общей посещаймости по дням')
    # plt.xlabel('День недели')
    # plt.ylabel('Число игр')
    # plt.savefig('plots/plot_2')
    #
    # # Столбчатая диаграмма
    # dataset['date'] = pd.to_datetime(dataset['date'], format='%Y%m%d')
    # selected_fields = ['park_id', 'length_minutes']
    # park_length_means = dataset.groupby('park_id')[selected_fields[1]].mean().reset_index()
    # sorted_park_lengths = park_length_means.sort_values(by='length_minutes', ascending=False)
    # top_10_park_lengths = sorted_park_lengths.head(10)
    #
    # plt.figure(figsize=(10, 5))
    # plt.bar(top_10_park_lengths['park_id'], top_10_park_lengths['length_minutes'], color='orange', alpha=0.7)
    # plt.title('Средняя длительность игр в каждом парке')
    # plt.xlabel('ID парка')
    # plt.ylabel('Средняя длительность игр (минуты)')
    # plt.savefig('plots/plot_3')
    #
    # # Круговая диаграмма
    # plt.figure(figsize=(8, 8))
    # dataset['day_of_week'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
    # plt.title('Распределение общей посещаймости по дням')
    # plt.savefig('plots/plot_4')
    #
    #
    # # График корреляции
    # dataset['date'] = pd.to_datetime(dataset['date'], format='%Y%m%d')
    # selected_fields = ['number_of_game','length_minutes', 'v_hits', 'h_hits', 'h_walks', 'h_errors']
    # correlation_matrix = dataset[selected_fields].corr()
    # plt.figure(figsize=(10, 8))
    # sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
    # plt.title('График корреляции')
    # plt.savefig('plots/plot_5')

if __name__ == "__main__":
    create_graphs()