# coding=utf-8
# Author: Ray, Jiarui Chen @ University of Macau
# Email: mb85409@um.edu.mo
# Time: 2021/4/6
# Part of ECG model tutorial @ Github: https://github.com/chen709847237/tutorial_ECG_model
# New data extraction script for XML file with new data format

import os
import pandas as pd
import xmltodict

data_root_folder = '/Users/chenjiarui/Python Dev/Lab_project/ECG/sample_2021_4_6/raw_data/'
output_root_folder = '/Users/chenjiarui/Python Dev/Lab_project/ECG/sample_2021_4_6/'
output_file_name = 'sample_data_label_summary.csv'

data_file_list = os.listdir(data_root_folder)
if '.DS_Store' in data_file_list: data_file_list.remove('.DS_Store')

file_name_list, case_id_list = [], []
patient_name_list, patient_birth_list, patient_gender_list = [], [], []
sample_rate_num_list, sample_rate_unit_list = [], []
vr_value_list, vr_unit_list = [], []
wave_length_list = []

max_interpretation_num = 5
interpretation_dict = {0: [], 1: [], 2: [], 3: [], 4: []}


count = 0
for data_file in data_file_list:

    file_name = data_file.split('.')[0]

    with open(data_root_folder + data_file, 'rb') as xml:
        data = xmltodict.parse(xml.read().decode('utf8'))
        xml.close()

    # patientInfo
    # PATH: 'sapphire' - 'dcarRecord' - 'patientInfo'
    patientInfo = data['sapphire']['dcarRecord']['patientInfo']
    # Name
    patient_name =patientInfo['name']['@use']
    # id
    case_id = patientInfo['identifier']['id']['@V']
    # birth day
    patient_birth = patientInfo['birthDateTime']['@V']
    # gender
    patient_gender = patientInfo['gender']['@V']

    # SAMPLE RATE
    sample_rate = patientInfo['visit']['order']['ecgResting']['params']['ecg']['wav']['ecgWaveformMXG']['sampleRate']
    sample_rate_num = sample_rate['@V']
    sample_rate_unit = sample_rate['@U']

    # ECG WAVE
    # PATH: ['visit']['order']['ecgResting']['params']['ecg']['wav']['ecgWaveformMXG']['ecgWaveform']
    ecg_wave = patientInfo['visit']['order']['ecgResting']['params']['ecg']['wav']['ecgWaveformMXG']['ecgWaveform']
    # FORMAT: LIST
    # NUM:12
    patient_ecg_wave = {}
    for i in range(len(ecg_wave)):
        wave_length_check = int(ecg_wave[i]['@asizeVT'])
        wave_label = ecg_wave[i]['@label']
        wave = ecg_wave[i]['@V'].strip().split()
        wave_length = len(wave)
        if wave_length != wave_length_check:
            print(wave_label)
            raise ValueError
        patient_ecg_wave[wave_label] = wave
        #break

    ecg_wave_df = pd.DataFrame(patient_ecg_wave)
    ecg_wave_df.index.name = 'samplenr'
    ecg_wave_df.to_csv(output_root_folder+file_name+'.csv', index=True)


    # Ventricular Rate
    # PATH: ['visit']['order']['ecgResting']['params']['ecg']['num']['ventricularRate']
    patient_ventricular_rate = patientInfo['visit']['order']['ecgResting']['params']['ecg']['num']['ventricularRate']
    patient_ventricular_rate_num = patient_ventricular_rate['@V']
    patient_ventricular_rate_unit = patient_ventricular_rate['@U']

    # Interpretation
    # PATH: ['visit']['order']['ecgResting']['params']['ecg']['interpretation']
    patient_interpretation = patientInfo['visit']['order']['ecgResting']['params']['ecg']['interpretation']['statement']['@V']
    patient_interpretation = patient_interpretation.strip()
    patient_interpretation_list = patient_interpretation.split()
    print(patient_interpretation_list)

    if len(patient_interpretation_list) < max_interpretation_num:
        patient_interpretation_list = patient_interpretation_list + [''] * (max_interpretation_num - len(patient_interpretation_list))
    for i in range(0, max_interpretation_num): interpretation_dict[i].append(patient_interpretation_list[i])

    file_name_list.append(file_name)
    case_id_list.append(case_id)
    patient_name_list.append(patient_name)
    patient_birth_list.append(patient_birth)
    patient_gender_list.append(patient_gender)
    sample_rate_num_list.append(sample_rate_num)
    sample_rate_unit_list.append(sample_rate_unit)
    vr_value_list.append(patient_ventricular_rate_num)
    vr_unit_list.append(patient_ventricular_rate_unit)
    wave_length_list.append(wave_length)

    #break

out_df = pd.DataFrame(
    {'file_name': file_name_list, 'case_id': case_id_list,
     'patient_name': patient_name_list, 'patient_birth': patient_birth_list,
     'patient_gender': patient_gender_list,
     'ventricular_rate_value': vr_value_list, 'ventricular_rate_unit': vr_unit_list,
     'sample_rate_num': sample_rate_num_list, 'sample_rate_unit': sample_rate_unit_list,
     'wave_length': wave_length_list})

for key in interpretation_dict.keys():
    out_df['conclusion_' + str(key)] = interpretation_dict[key]

out_df.to_csv(output_root_folder + output_file_name, encoding="utf_8_sig", index=False)