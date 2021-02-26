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

#data_root_folder = '/Users/chenjiarui/Python Dev/Lab_project/ECG/ECG_data_csv_400Hz_scale_60_pad/'
#out_put_folder = '/Users/chenjiarui/Python Dev/Lab_project/ECG/ECG_data_csv_400Hz_scale_60_pad_hdf5/'

data_root_folder = '/Users/chenjiarui/Python Dev/Lab_project/ECG/ECG_data_csv_400Hz_pad/'
out_put_folder = '/Users/chenjiarui/Python Dev/Lab_project/ECG/ECG_data_csv_400Hz_pad_hdf5/'

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

hdfFile = h5py.File(out_put_folder+'test_data.h5', 'w')
hdfFile.create_dataset('tracings', data=np.array(out_data))
hdfFile.close()

out_data_info = {'idx': data_idx, 'name': data_name}
out_df = pd.DataFrame(out_data_info)
out_df.to_csv(out_put_folder+'test_data_check.csv', encoding="utf_8_sig")





'''plt.figure(figsize=(20, 10))
sample_rate = 1
sample_count = 4096
t = np.linspace(0, sample_count/sample_rate, sample_count)
ax0 = plt.subplot(111)
ECG_line = ax0.plot(t, np.array(data['I'].tolist()), label='ECG_500Hz')
ax0.set_xlabel("Time")
ax0.set_ylabel("Amp")
plt.legend(handles=ECG_line)
plt.show()
plt.close'''



'''h5_f = h5py.File('/Users/chenjiarui/Python Dev/Lab_project/ECG/automatic-ecg-diagnosis-master/data/ecg_tracings.hdf5', "r")
x = h5_f['tracings']
x_np = np.array(x)'''

'''print(x_np.shape)'''

'''sample = x_np[1, :, :]
#print(x_np[0,:,:].shape)
pd_info(sample)



plt.figure(figsize=(20, 10))
sample_rate = 1
sample_count = 4096
t = np.linspace(0, sample_count/sample_rate, sample_count)
ax0 = plt.subplot(111)
ECG_line = ax0.plot(t, sample[:, 0], label='ECG_500Hz')
ax0.set_xlabel("Time")
ax0.set_ylabel("Amp")
plt.legend(handles=ECG_line)
plt.show()
plt.close'''






