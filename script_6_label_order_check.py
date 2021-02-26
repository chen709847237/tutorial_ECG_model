#coding=utf-8
# Author: Ray, Jiarui Chen @ University of Macau
# Email: mb85409@um.edu.mo
# Time: 2021/2/26
# Part of ECG model tutorial @ Github: https://github.com/chen709847237/tutorial_ECG_model
# Sort the ground-truth label same order as data saved in the hdf5 file

import pandas as pd


label_file = '/Users/chenjiarui/Python Dev/Lab_project/ECG/ECG_data_csv_400Hz_pad_hdf5/test_data_info_label.csv'
check_idx_file = '/Users/chenjiarui/Python Dev/Lab_project/ECG/ECG_data_csv_400Hz_pad_hdf5/test_data_check.csv'

label_data = pd.read_csv(label_file)
check_idx = pd.read_csv(check_idx_file, index_col=0)

merge_data = pd.merge(check_idx, label_data, how='outer', on=['idx', 'idx'])
merge_data.rename({'name_x': 'name', 'name_y': 'name_check'}, inplace=True, axis='columns')

print(label_data)
print(check_idx)
print(merge_data.columns)

merge_data.to_csv('/Users/chenjiarui/Python Dev/Lab_project/ECG/ECG_data_csv_400Hz_pad_hdf5/test_data_info_label_order.csv', encoding="utf_8_sig")



