import pandas as pd
import numpy as np

def opt_float(data):
    dataset_float = data.select_dtypes(include=["float"])
    converted_float = dataset_float.apply(pd.to_numeric, downcast="float")

    compare_floats = pd.concat([dataset_float.dtypes, converted_float.dtypes], axis=1)
    compare_floats.columns = ["before", "after"]
    compare_floats.apply(pd.Series.value_counts)
    print(compare_floats)

    return converted_float

def opt_int(data):
    dataset_int = data.select_dtypes(include=["int"])
    converted_int = dataset_int.apply(pd.to_numeric, downcast="unsigned")

    compare_ints = pd.concat([dataset_int.dtypes, converted_int.dtypes], axis=1)
    compare_ints.columns = ["before", "after"]
    compare_ints.apply(pd.Series.value_counts)
    print(compare_ints)

    return converted_int

def opt_obj(data, compression=False):
    converted_obj = pd.DataFrame()
    dataset_obj = data.select_dtypes(include=["object"]).copy()

    for col in dataset_obj.columns:
        num_unique_values = len(dataset_obj[col].unique())
        num_total_values = len(dataset_obj[col])
        if compression:
            if num_unique_values / num_total_values < 0.5:
                converted_obj.loc[col] = dataset_obj[col].astype("category")
            else:
                converted_obj[col] = dataset_obj[col]
        else:
            if num_unique_values / num_total_values < 0.5:
                converted_obj.loc[:, col] = dataset_obj[col].astype("category")
            else:
                converted_obj[:, col] = dataset_obj[col]

    return converted_obj


def opt_dataset(data, compression=False):
    optimized_dataset = data.copy()
    converted_int = opt_int(data)
    converted_float = opt_float(data)
    converted_obj = opt_obj(data, compression)

    optimized_dataset[converted_int.columns] = converted_int
    optimized_dataset[converted_float.columns] = converted_float
    optimized_dataset[converted_obj.columns] = converted_obj

    return optimized_dataset