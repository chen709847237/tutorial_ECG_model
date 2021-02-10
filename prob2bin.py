import numpy as np
import pandas as pd


if __name__ == '__main__':

    data_path = '<Replace this string with the path of prediction result file (dnn_output.npy)>'
    outout_path = '<Replace this string with the path of output transformed file path/output transformed file name>'
    decision_threshold = [0.12361142, 0.09042355, 0.0513474, 0.26380765, 0.36633369, 0.17381361]
    prediction_result = np.load(data_path, allow_pickle=True)
    for i in range(prediction_result.shape[1]):
        prediction_result[:, i] = np.int64(prediction_result[:, i]>decision_threshold[i])
    output_df = pd.DataFrame(prediction_result, columns=['1dAVb', 'RBBB', 'LBBB', 'SB', 'AF', 'ST'])
    output_df.to_csv(outout_path)



