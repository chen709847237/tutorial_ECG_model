#coding=utf-8
# Author: Ray, Jiarui Chen @ University of Macau
# Email: mb85409@um.edu.mo
# Time: 2021/2/26
# Part of ECG model tutorial @ Github: https://github.com/chen709847237/tutorial_ECG_model
# Script for scale the ECG signals

import os
import numpy as np
import pandas as pd

data_root_folder = '/Users/chenjiarui/Python Dev/Lab_project/ECG/ECG_data_csv_400Hz/'
output_root_folder = '/Users/chenjiarui/Python Dev/Lab_project/ECG/ECG_data_csv_400Hz_scale_60/'

data_file_list = os.listdir(data_root_folder)
if '.DS_Store' in data_file_list: data_file_list.remove('.DS_Store')
count = 0
for data_file in data_file_list:

    data = pd.read_csv(data_root_folder+data_file, index_col='samplenr')

    col_name = data.columns.tolist()
    temp_dict = {}
    for lead_name in col_name:

        scale_data = np.array(data[lead_name].tolist()) / 600
        temp_dict[lead_name] = scale_data

    target_data = pd.DataFrame(temp_dict)
    target_data.index.name = 'samplenr'

    target_data.to_csv(output_root_folder+data_file)

    count += 1
    print('file:', count)

    #break





