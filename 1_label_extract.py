#coding=utf-8
# Author: Ray, Jiarui Chen @ University of Macau
# Email: mb85409@um.edu.mo
# Time: 2021/2/26
# Part of ECG model tutorial @ Github: https://github.com/chen709847237/tutorial_ECG_model
# Script for diagnosis conclusion extraction

import os
import pandas as pd
import xmltodict

data_root_folder = '/Users/chenjiarui/Python Dev/Lab_project/ECG/ECG_data_HL7/'
output_root_folder = '/Users/chenjiarui/Python Dev/Lab_project/ECG/'
data_file_list = os.listdir(data_root_folder)
if '.DS_Store' in data_file_list: data_file_list.remove('.DS_Store')

file_idx_list, file_name_list = [], []
hr_value_list, hr_unit_list = [], []
conclusion_dict = {0: [], 1: [], 2: [], 3: [], 4: []}

count = 0
for data_file in data_file_list:

    file_idx = data_file.split('_')[0]
    file_name = data_file.split('_')[1].split('.')[0]

    with open(data_root_folder+data_file, 'rb') as xml:
        data = xmltodict.parse(xml.read().decode('utf8'))
        annotations_list = data['AnnotatedECG']['component']['series']['subjectOf']['annotationSet']['component']['annotation']['component']
        # annotations---heart rate
        heartrate_data_group = annotations_list[-2]['annotation']
        heartrate_data_name = heartrate_data_group['code']['@code']
        heartrate_data_value = heartrate_data_group['value']
        heartrate_data_value_num = heartrate_data_group['value']['@value']
        heartrate_data_value_unit = heartrate_data_group['value']['@unit']
        #print(heartrate_data_value_num, heartrate_data_value_unit)

        # annotations---interpretation
        interpretation_data_group = annotations_list[-1]['annotation']
        interpretation_data_name = interpretation_data_group['code']['@code']
        interpretation_data_list = interpretation_data_group['component']
        # annotations---interpretation---conclusion
        interpretation_conclusion_data_group = interpretation_data_list[-1]['annotation']
        interpretation_conclusion_data_name = interpretation_conclusion_data_group['code']['@code']
        interpretation_conclusion_data_value = interpretation_conclusion_data_group['value']['#text']
        #print(interpretation_conclusion_data_value.split('\n'))

        xml.close()

    file_idx_list.append(file_idx+'\t')
    file_name_list.append(file_name)
    hr_value_list.append(heartrate_data_value_num)
    hr_unit_list.append(heartrate_data_value_unit)

    conclusion_split_list = interpretation_conclusion_data_value.split('\n')
    if len(conclusion_split_list) < 5:
        conclusion_split_list = conclusion_split_list + [''] * (5-len(conclusion_split_list))
    for i in range(0, 5): conclusion_dict[i].append(conclusion_split_list[i])

    count += 1

    print(count)


out_df = pd.DataFrame({'idx':file_idx_list, 'name':file_name_list, 'heartrate':hr_value_list, 'heartrate_unit':hr_unit_list})
for key in conclusion_dict.keys():
    out_df['conclusion_'+str(key)] = conclusion_dict[key]
out_df.to_csv('./test_data_info_conclu.csv', encoding="utf_8_sig", index=False)

