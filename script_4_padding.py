#coding=utf-8
# Author: Ray, Jiarui Chen @ University of Macau
# Email: mb85409@um.edu.mo
# Time: 2021/2/26
# Part of ECG model tutorial @ Github: https://github.com/chen709847237/tutorial_ECG_model
# Script for ECG signals padding

import os
import numpy as np
import pandas as pd

data_root_folder = '<Replace this string with the path of the folder where the ECG signal csv files are stored>'
output_root_folder = '<Replace this string with the path of the output target folder>'

data_file_list = os.listdir(data_root_folder)
if '.DS_Store' in data_file_list: data_file_list.remove('.DS_Store')
count = 0
for data_file in data_file_list:

    data = pd.read_csv(data_root_folder+data_file, index_col='samplenr')
    col_name = data.columns.tolist()
    temp_dict = {}
    for lead_name in col_name:
        pad_data = np.pad(data[lead_name].values, ((48, 48)), mode='constant')
        temp_dict[lead_name] = pad_data

    target_data = pd.DataFrame(temp_dict)
    target_data.index.name = 'samplenr'
    target_data.to_csv(output_root_folder+data_file)
    count += 1
    print('file:', count)

