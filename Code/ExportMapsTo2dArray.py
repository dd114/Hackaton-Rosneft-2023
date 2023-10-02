import numpy as np
import IO


def exportMapsTo2dArray(file_name):
    # file_name = "Point_dataset"

    data = IO.import_dataset_from_file(f"..\\Data\\{file_name}.txt")

    unique_data_x = data["x"].sort_values().unique()
    unique_data_y = data["y"].sort_values().unique()

    # x_grid, y_grid = np.meshgrid(unique_data_x, unique_data_y)

    x_y_z_grid = np.zeros((len(unique_data_x), len(unique_data_y)))

    for i in range(len(data["z"])):
        x_y_z_grid[np.argwhere(unique_data_x == data["x"].iloc[i]), np.argwhere(unique_data_y == data["y"].iloc[i])] = \
        data["z"].iloc[i]

    np.save(file_name, x_y_z_grid)
