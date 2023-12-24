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
    #df.info(memory_usage='deep')

    # plt.figure(figsize=(12, 6))
    # monthly_flight_counts = df.groupby('MONTH').size()
    # monthly_flight_counts.plot(kind='bar', color='skyblue')
    # plt.xlabel('Месяц')
    # plt.ylabel('Количество рейсов')
    # plt.title('Количество рейсов по месяцам')
    # plt.savefig('plots/plot_1')
    #
    # plt.figure(figsize=(10, 6))
    # sns.lineplot(x='SCHEDULED_DEPARTURE', y='DEPARTURE_DELAY', data=df, legend=True)
    # plt.title('Линейный график: Задержка при вылете в зависимости от запланированного времени отправления')
    # plt.xlabel('Запланированное время отправления')
    # plt.ylabel('Задержка при вылете')
    # plt.savefig('plots/plot_2')
    #
    # plt.figure(figsize=(14, 8))
    # top_delays = df.nlargest(10, 'DEPARTURE_DELAY')
    # sns.boxplot(x='DEPARTURE_DELAY', data=top_delays)
    # plt.title('Box plot: 10 самых больших задержек при вылете')
    # plt.xlabel('Задержка при вылете')
    # plt.savefig('plots/plot_3')
    #
    # plt.figure(figsize=(10, 6))
    # sns.boxplot(x='MONTH', y='DEPARTURE_DELAY', data=df)
    # plt.title('Box plot: Задержки при вылете по месяцам')
    # plt.xlabel('Месяц')
    # plt.ylabel('Задержка при вылете')
    # plt.savefig('plots/plot_4')
    #
    # # График корреляции
    # numerical_columns = ['MONTH', 'DAY', 'FLIGHT_NUMBER', 'SCHEDULED_DEPARTURE', 'DEPARTURE_TIME',
    #                      'DEPARTURE_DELAY', 'AIR_TIME', 'DISTANCE', 'WHEELS_ON', 'SCHEDULED_ARRIVAL']
    # correlation_matrix = df[numerical_columns].corr()
    # plt.figure(figsize=(10, 8))
    # sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    # plt.title('Корреляционная матрица для числовых переменных')
    # plt.savefig('plots/plot_5')

if __name__ == "__main__":
    create_graphs()