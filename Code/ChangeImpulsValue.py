import numpy as np
import IO

if __name__ == '__main__':

    file_name1 = "Result_good"
    file_name2 = "Result_bad"

    data1 = IO.import_dataset_from_file(f"..\\Data\\{file_name1}.txt")
    data2 = IO.import_dataset_from_file(f"..\\Data\\{file_name2}.txt")

    for i in range(len(data2["z"])):
        if data2['z'][i] > 30:
            data2['z'][i] = data1['z'][i]

    IO.export_dataset_to_file(data2)