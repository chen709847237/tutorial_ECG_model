#coding=utf-8
# Author: Ray, Jiarui Chen @ University of Macau
# Email: mb85409@um.edu.mo
# Time: 2021/2/26
# Part of ECG model tutorial @ Github: https://github.com/chen709847237/tutorial_ECG_model
# Script for converting CSV file to hdf5 file

import os
import numpy as np
import pandas as pd
import h5py

data_root_folder = '<Replace this string with the path of the folder where padded ECG signal data files are stored>'
out_put_folder = '<Replace this string with the path of the output hdf5 file folder>'
out_put_file_name = '<Replace this string with the name of the output hdf5 file>'

data_file_list = os.listdir(data_root_folder)
if '.DS_Store' in data_file_list: data_file_list.remove('.DS_Store')
count = 0
data_idx = []
data_name = []
out_data = []
out_data_info = {}
for data_file in data_file_list:
    data = pd.read_csv(data_root_folder+data_file, index_col='samplenr')
    print(str(data_file.split('_')[0]))
    print(str(data_file.split('_')[1].split('.')[0]))
    data_idx.append(str(data_file.split('_')[0])+'\t')
    data_name.append(str(data_file.split('_')[1].split('.')[0]))
    out_data.append(data)
    count += 1
    print('file:', count)

print(np.array(out_data).shape)
print(np.array(data_idx).shape)
print(np.array(data_name).shape)

hdfFile = h5py.File(out_put_folder+out_put_file_name+'.h5', 'w')
hdfFile.create_dataset('tracings', data=np.array(out_data))
hdfFile.close()

out_data_info = {'idx': data_idx, 'name': data_name}
out_df = pd.DataFrame(out_data_info)
out_df.to_csv(out_put_folder+out_put_file_name+'_order.csv', encoding="utf_8_sig")

