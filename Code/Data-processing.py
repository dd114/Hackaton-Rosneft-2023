# In[1]:


import numpy as np
# import matplotlib.pyplot as plt

import IO
import ExportMapsTo2dArray
import PointDatasetOnMapGrid
import ExportFinalGrid

# plt.rcParams ['figure.figsize'] = [20, 10]


# In[39]:

map_names = ["Map_1", "Map_2", "Map_3", "Map_4", "Map_5"]

for i in map_names:
    ExportMapsTo2dArray.exportMapsTo2dArray(i)

PointDatasetOnMapGrid.pointDatasetOnMapGrid()


# In[40]:


# In[41]:


point_dataset = np.load("Point_dataset_on_Map_1_grid.npy")
# point_dataset = np.load("Point_dataset_on_Map_3_grid.npy")


# In[42]:



# In[43]:


map_npy_names = ["Map_1.npy", "Map_2.npy", "Map_3.npy", "Map_4.npy", "Map_5.npy"]

maps = []

for i, item in enumerate(map_npy_names):
    maps.append(np.load(item))
    #arrays[i][arrays[i] == 0] = np.nan


# In[44]:


maps[2] = maps[2][:-1, :]
maps[3] = maps[3][:-1, :]


# In[45]:


number_of_maps = len(maps)
for i in range(number_of_maps - 3):
    for j in range(i + 1, number_of_maps):
        maps.append(maps[i] * maps[j])


# In[46]:


maps_points_dataset = []
point_dataset_arr = 0
for map in maps:
    maps_points_dataset.append(map[point_dataset != 0])

#print(maps_points_dataset[0])

point_dataset_arr = point_dataset[point_dataset != 0]

matrix = np.empty((440, len(maps)))

for i, arr in enumerate(maps_points_dataset):
    matrix[:, i] = arr


# In[47]:


from sklearn.linear_model import LinearRegression
# reg = LinearRegression().fit(matrix[:5, :], point_dataset_arr[:5])
reg = LinearRegression().fit(matrix, point_dataset_arr)


# In[48]:


bias = reg.intercept_
weights = reg.coef_
print(weights, bias)


# In[49]:


matrix[:10, :].dot(weights) + bias, point_dataset_arr[:10]


# In[50]:


final_grid = np.zeros(maps[0].shape)

for i, map in enumerate(maps):
    final_grid += map * weights[i]

final_grid += bias


# In[51]:


np.save("Final_grid", final_grid)


# In[52]:


# print_maps = maps.copy()
# print_final_grid = final_grid.copy()
# print_point_dataset_pool = point_dataset_pool.copy()
#
#
# for i, item in enumerate(map_npy_names):
#     print_maps[i][print_maps[i] == 0] = np.nan
#
#     plt.subplot(2, 3, i + 1)
#
#     plt.title(item)
#     plt.imshow(print_maps[i], cmap='seismic')

# plt.figure(figsize=(30, 30))

# plt.show()


# In[53]:


# print_point_dataset_pool[print_point_dataset_pool == 0] = np.nan
#
# plt.subplot(1, 2, 1)
# plt.title("point_dataset_pool")
# plt.imshow(print_point_dataset_pool, cmap='seismic')
#
# print_final_grid[final_grid < 0] = np.nan
#
# plt.subplot(1, 2, 2)
# plt.title("final_grid")
# plt.imshow(print_final_grid, cmap='seismic')
#
# plt.show()


# In[54]:


number_of_point = len(final_grid[point_dataset != 0] - point_dataset[point_dataset != 0])
print(number_of_point)


# In[55]:


print((((final_grid[point_dataset != 0] - point_dataset[point_dataset != 0]) ** 2).sum() / number_of_point) ** 0.5)



ExportFinalGrid.exportFinalGrid()

