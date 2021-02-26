#coding=utf-8
# Author: Ray, Jiarui Chen @ University of Macau
# Email: mb85409@um.edu.mo
# Time: 2021/2/26
# Part of ECG model tutorial @ Github: https://github.com/chen709847237/tutorial_ECG_model
# Convert predicted probabilities to binary results

import numpy as np
import pandas as pd

data_path = '<Replace this string with the path of prediction result file (dnn_output.npy)>'
outout_path = '<Replace this string with the path of output transformed file path + / + output transformed file name>'

decision_threshold = [0.12361142, 0.09042355, 0.0513474, 0.26380765, 0.36633369, 0.17381361]
prediction_result = np.load(data_path, allow_pickle=True)
for i in range(prediction_result.shape[1]):
    prediction_result[:, i] = np.int64(prediction_result[:, i]>decision_threshold[i])
output_df = pd.DataFrame(prediction_result, columns=['1dAVb', 'RBBB', 'LBBB', 'SB', 'AF', 'ST'])
output_df.to_csv(outout_path)



