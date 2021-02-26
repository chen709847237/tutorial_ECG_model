# A Tutorial for classifying ECG signals by using CNN model
 
## References
```
Ribeiro, A.H., Ribeiro, M.H., Paixão, G.M.M. et al. Automatic diagnosis of the 12-lead ECG using a deep neural network.
Nat Commun 11, 1760 (2020). https://doi.org/10.1038/s41467-020-15432-4
```
## Model and Data
* The scripts and detail of this model are available at: [Here](https://github.com/antonior92/automatic-ecg-diagnosis)
* Model Download: [Here](https://zenodo.org/record/3765717#.YCOS8xMzbqU)
* Test Data Download: [Here](https://zenodo.org/record/3765780#.YCOS8hMzbqU)

## Requirements 
* numpy>=1.14.3
* pandas>=0.22
* tensorflow=2.2
* h5py>=2.8
* xmljson>=0.1.9
* scipy>=1.1
* scikit-learn>=0.20
* tqdm>=4.26
* xarray>=0.11.2
* seaborn>=0.9
* openpyxl>=3.0

## Run the Model
### STEP 1
Activate the anaconda.
```bash
conda activate
```
### STEP 2
Enter the python environment.
```bash
conda activate <name of environment>
```
e.g.
```bash
conda activate ecg
```
### STEP 3
Enter the folder where the "automatic-ecg-diagnosis" repository was cloned.
```bash
cd <path of folder>
```
e.g.
```bash
cd /user/scripts/ECG/automatic-ecg-diagnosis-master/
```
### STEP 4
Run the script.
```bash
python predict.py <path to test data (HDF5 file)> <path to model (HDF5 file)>
```
e.g.
```bash
python predict.py ./data/ecg_tracings.hdf5 ./model/model.hdf5
```
### STEP 5 
The prediction result is stored in the file ```dnn_output.npy```, it is located in the same folder that appeared in STEP 3.
### STEP 6
Load & convert the prediction result from probability to binary label.
1. Copy script ```script_7_prob2bin.py``` from this repository to the same folder that appeared in STEP 3.
2. Define the paths in the script.
```python
data_path = '<Replace this string with the path of prediction result file (dnn_output.npy)>'
outout_path = '<Replace this string with the path of output transformed file path + / + output transformed file name>'
# e.g.
data_path = './automatic-ecg-diagnosis-master/dnn_output.npy'
outout_path = './automatic-ecg-diagnosis-master/dnn_output_bin.csv'
```
3. Save & Run the script.
```bash
python script_7_prob2bin.py
```
4. The converted binary prediction results will be stored in the specified folder as a CSV file.
### STEP 7.
Your binary prediction result should be exactly the same as the content of file ```dnn_output_bin.csv```

****
## Preprocessing Steps of Our Data
### STEP 0 
Extract ECG signals from xml file as a csv file by using ECGToolkit. (Windows Only) (script_0_xml2csv.bat) :warning:TBC:warning: 
### STEP 1 
Diagnosis conclusion extraction. (script_1_label_extract.py)
### STEP 2  
ECG signals resampling, from 500Hz to 400Hz. (script_2_ecg_resample.py)
### STEP 3 
Scale ECG signals, ECG signal X/600 currently. (script_3_scale.py)
### STEP 4 
ECG signals padding, 4000x12 to 4096x12 (script_4_padding.py)
### STEP 5 
Pack padded csv files into hdf5 file. (script_5_csv2hdf5.py)
### STEP 6 
Sort the ground truth label with the same order as data saved in the hdf5 file (script_6_order_label.py)

