import pandas as pd


def import_dataset_from_file(path_to_file: str) -> pd.DataFrame:
    """
    Функция импортирования исходных данных.
    :param path_to_file: путь к загружаемому файлу;
    :return: структура данных.
    """
    dataset = pd.read_table(path_to_file, delim_whitespace=True, names=['x', 'y', 'z'])

    return dataset


def export_dataset_to_file(dataset: pd.DataFrame):
    """
    Функция экспортирования результата в файл result.txt.
    :param dataset: входная структура данных.
    """
    n, c = dataset.shape

    assert c == 3, 'Количество столбцов должно быть 3'
    assert n == 1196590, 'Количество строк должно быть 1196590'

    with open('Data\\Result.txt', 'w') as f:
        for i in range(n):
            f.write('%.2f %.2f %.5f\n' % (dataset.x[i], dataset.y[i], dataset.z[i]))


if __name__ == "__main__":
    # Вспомогательные данные, по которым производится моделирование
    map_1_dataset = import_dataset_from_file("Data\\Map_1.txt")
    map_2_dataset = import_dataset_from_file("Data\\Map_2.txt")
    map_3_dataset = import_dataset_from_file("Data\\Map_3.txt")
    map_4_dataset = import_dataset_from_file("Data\\Map_4.txt")
    map_5_dataset = import_dataset_from_file("Data\\Map_5.txt")

    # Данные, по которым необходимо смоделировать
    point_dataset = import_dataset_from_file("Data\\Point_dataset.txt")

    # Точки данных, в которые необходимо провести моделирование (сетка данных)
    point_grid = import_dataset_from_file("Data\\Result_schedule.txt")

    # Блок вычислений
    # dataset = calc(point_grid)

    # Экспорт данных в файл (смотри Readme.txt)
    # export_dataset_to_file(dataset=dataset)
