import numpy as np
import IO

def exportFinalGrid():

    file_name1 = "Result_schedule"
    file_name2 = "Map_1"

    data1 = IO.import_dataset_from_file(f"..\\Data\\{file_name1}.txt")
    data2 = IO.import_dataset_from_file(f"..\\Data\\{file_name2}.txt")

    final_grid = np.load("Final_grid.npy")

    # unique_data1_x = data1["x"].sort_values().unique()
    # unique_data1_y = data1["y"].sort_values().unique()

    unique_data2_x = data2["x"].sort_values().unique()
    unique_data2_y = data2["y"].sort_values().unique()

    # x_y_z_grid = np.zeros((len(unique_data2_x), len(unique_data2_y)))

    for i in range(len(data1["z"])):
        temp_data1_x = data1["x"].iloc[i]
        temp_data1_y = data1["y"].iloc[i]

        index_x = np.searchsorted(unique_data2_x, temp_data1_x)
        index_y = np.searchsorted(unique_data2_y, temp_data1_y)


        if unique_data2_x[index_x] == temp_data1_x and unique_data2_y[index_y] == temp_data1_y:
            data1["z"].iloc[i] = final_grid[index_x][index_y]

        if i % 10000 == 0:
            print(i)


    data1["z"] = data1["z"].fillna(0)

    # save array to the file
    # np.save("Point_dataset_on_map_grid", x_y_z_grid)
    data1.loc[data1["z"] < 0, "z"] = 10

    IO.export_dataset_to_file(data1)


