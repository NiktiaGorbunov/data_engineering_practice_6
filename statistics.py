import pandas as pd

def get_memory_stat_by_column(data):
    mem_usage_stats = data.memory_usage(deep=True)
    total_usage = mem_usage_stats.sum()

    print(f'file in memory size = {total_usage // 1024:10} КБ')
    column_stat = []
    for key in data.dtypes.keys():
        column_stat.append(
            {
                "column_name": key,
                "memory_abs": mem_usage_stats[key] // 1024,
                "memory_per": round(mem_usage_stats[key] / total_usage * 100, 4),
                "dtype": data.dtypes[key],
            }
        )

    column_stat.sort(key=lambda x: x["memory_abs"], reverse=True)

    for column in column_stat:
        print(
            f"{column['column_name']:30} : {column['memory_abs']:10} КБ : {column['memory_per']:10}% : {column['dtype']}"
        )


def mem_usage(pandas_obj):
    if isinstance(pandas_obj, pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else:
        usage_b = pandas_obj.memory_usage(deep=True)
    usage_mb = usage_b / 1024 ** 2

    return "{:03.2f} MB".format(usage_mb)