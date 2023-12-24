import json
import os
import pandas as pd
import numpy as np
import optimizer
import statistics


pd.set_option("display.max_rows", 20, "display.max_columns", 60)

file_name = "../tasks/[4]vacancies.csv.gz"
column_names = [
        "id",
        "schedule_id",
        "schedule_name",
        "accept_kids",
        "experience_id",
        "experience_name",
        "salary_from",
        "salary_to",
        "salary_gross",
        "salary_currency",
    ]

def read_file(file_name):
    return next(pd.read_csv(file_name, chunksize=100_000, compression='gzip'))


def opt_types(optimized_dataset, file_name):
    need_column = dict()
    opt_dtypes = optimized_dataset.dtypes

    for key in column_names:
        need_column[key] = opt_dtypes[key]
        print(f"{key}: {opt_dtypes[key]}")

    with open('dtypes.json', mode='w') as file:
        dtypes_json = need_column.copy()
        for key in dtypes_json.keys():
            dtypes_json[key] = str(dtypes_json[key])

        json.dump(dtypes_json, file)

    has_header = True
    for chunk in pd.read_csv(
            file_name,
            usecols=lambda x: x in column_names,
            dtype=need_column,
            chunksize=100_000,

    ):
        print(f"chink memory usage = {statistics.mem_usage(chunk)}")
        chunk.to_csv("df.csv", mode="a", header=has_header)
        has_header = False


def main():

    data = read_file(file_name)

    print(" -- данные о первичном документе -- ")
    print(f"file size           = {os.path.getsize(file_name)}")
    statistics.get_memory_stat_by_column(data)
    data.info(memory_usage='deep')
    print()

    print('--- optimization obj ---')
    dataset_obj = data.select_dtypes(include=["object"]).copy()
    converted_obj = optimizer.opt_obj(data, compression=True)
    print(statistics.mem_usage(dataset_obj))
    print(statistics.mem_usage(converted_obj))

    print('--- optimization int ---')
    dataset_int = data.select_dtypes(include=["int"])
    converted_int = optimizer.opt_int(data)
    print(statistics.mem_usage(dataset_int))
    print(statistics.mem_usage(converted_int))

    print('--- optimization float ---')
    dataset_float = data.select_dtypes(include=["float"])
    converted_float = optimizer.opt_float(data)
    print(statistics.mem_usage(dataset_float))
    print(statistics.mem_usage(converted_float))

    print('--- optimized dataset ---')
    optimized_dataset = optimizer.opt_dataset(data)
    print(f"default data memory usage = {statistics.mem_usage(data)}")
    print(f"optimized dataset memory usage = {statistics.mem_usage(optimized_dataset)}")

    print()
    print(" -- данные об оптимизированном документе -- ")
    statistics.get_memory_stat_by_column(optimized_dataset)
    optimized_dataset.info(memory_usage='deep')

    print(" -- сохранение определенных столбцов в документе --")
    opt_types(optimized_dataset, file_name)




if __name__ == "__main__":
    main()
