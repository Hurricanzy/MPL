from concurrent.futures import ProcessPoolExecutor as Pool
import pandas as pd
import random as rd
import math


def generate_csv(filename: str) -> None:
    data = {
        'cathegory': [],
        'value': []
    }

    for _ in range(20):
        cathegory = chr(rd.randint(ord('A'), ord('D')))
        value = rd.random()

        data['cathegory'].append(cathegory)
        data['value'].append(value)

    df = pd.DataFrame(data)

    try:
        df.to_csv(filename, index=False)
    except Exception as e:
        print(f"an error occurred: {e}")


def process_csv(filename: str):
    path = f"{filename}.csv" if not filename.endswith('.csv') else filename
    data = pd.read_csv(path).to_dict(orient='records')
    data_by_cathegories = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
    }
    result_data = {
        'cathegory': [],
        'median': [],
        'dispersion': [],
    }

    for item in data:
        if item['cathegory'] in data_by_cathegories:
            data_by_cathegories[item['cathegory']].append(item['value'])

    for cathegory in data_by_cathegories.keys():
        values_list = data_by_cathegories[cathegory]
        median = get_median(values_list)

        if (median != None):
            std_dev = get_standard_deviation(values_list)
            result_data['cathegory'].append(cathegory)
            result_data['median'].append(median)
            result_data['dispersion'].append(std_dev)

    return result_data


def get_median(numbers: list) -> None | float:
    quantity = len(numbers)
    numbers.sort()

    if quantity == 0: return None
    if quantity == 1: return numbers[0]

    if (quantity % 2) == 0:
        return (numbers[(quantity // 2) - 1] + numbers[quantity // 2]) / 2
    else:
        return numbers[(quantity // 2)]


def get_mean(numbers: list) -> float:
    if not numbers: return 0.0
    return sum(numbers) / len(numbers)


def get_standard_deviation(numbers: list):
    if len(numbers) < 2: return 0.0

    mean = get_mean(numbers)
    dispersions_squares_sum = 0
    quantity = len(numbers)

    for number in numbers:
        dispersions_squares_sum += (number - mean) ** 2

    return math.sqrt(dispersions_squares_sum / quantity)


def merge_processed_files(filenames: list[str]):
    merged_data = {
        'cathegory': [],
        'value': []
    }

    for filename in filenames:
        data_to_merge = pd.read_csv(f"{filename}.csv").to_dict(orient='records')
        for row in data_to_merge:
            merged_data['cathegory'].append(row['cathegory'])
            merged_data['value'].append(row['median'])

    df = pd.DataFrame(merged_data)

    try:
        df.to_csv("data_processed_merged.csv", index=False)
    except Exception as e:
        print(f"an error occurred: {e}")


if __name__ == '__main__':
    filenames_to_process = []

    for i in range(5):
        generate_csv(f"data_{i + 1}.csv")
        filenames_to_process.append(f"data_{i + 1}")

    with Pool(max_workers=5) as executor:
        results = list(executor.map(process_csv, filenames_to_process))

    for i in range(5):
        df = pd.DataFrame(results[i])
        filenames_to_process[i] = f"{filenames_to_process[i]}_processed"

        try:
            df.to_csv(f"{filenames_to_process[i]}.csv", index=False)
        except Exception as e:
            print(f"an error occurred: {e}")

    merge_processed_files(filenames_to_process)
    result = process_csv("data_processed_merged")
    df = pd.DataFrame(result)

    try:
        df.to_csv("result.csv", index=False)
    except Exception as e:
        print(f"an error occurred: {e}")

    print("Done!")