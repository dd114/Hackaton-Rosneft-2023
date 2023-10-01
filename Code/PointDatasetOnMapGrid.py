import numpy as np
import IO

if __name__ == '__main__':

    file_name1 = "Point_dataset"
    file_name2 = "Map_1"

    data1 = IO.import_dataset_from_file(f"..\\Data\\{file_name1}.txt")
    data2 = IO.import_dataset_from_file(f"..\\Data\\{file_name2}.txt")

    # unique_data1_x = data1["x"].sort_values().unique()
    # unique_data1_y = data1["y"].sort_values().unique()

    unique_data2_x = data2["x"].sort_values().unique()
    unique_data2_y = data2["y"].sort_values().unique()

    x_y_z_grid = np.zeros((len(unique_data2_x), len(unique_data2_y)))

    for i in range(len(data1["z"])):
        temp_shift_data2_x = data2["x"] - data1["x"].iloc[i]
        temp_shift_data2_y = data2["y"] - data1["y"].iloc[i]

        temp_hypot = (temp_shift_data2_x ** 2 + temp_shift_data2_y ** 2) ** 0.5
        arg_hypot_min = temp_hypot.argmin()

        x_y_z_grid[np.argwhere(unique_data2_x == data2["x"].iloc[arg_hypot_min]), np.argwhere(unique_data2_y == data2["y"].iloc[arg_hypot_min])] = data1["z"].iloc[i]

    # save array to the file
    np.save("Point_dataset_on_map_grid", x_y_z_grid)


