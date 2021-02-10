# tutorial_ECG_model
## A Tutorial for classifying ECG signals by using CNN model
 
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

## Run the script
### STEP 1. Activate the anaconda.
```bash
conda activate
```
### STEP 2. Enter the environment.
```bash
conda activate <name of environment>
```
e.g.
```bash
conda activate ecg
```

### STEP 3. Enter the folder where the "automatic-ecg-diagnosis" scripts are stored.
```bash
cd <path of folder>
```
e.g.
```bash
cd /user/scripts/ECG/automatic-ecg-diagnosis-master/
```

### STEP 4. Run the script.
```bash
python predict.py <path to test data (HDF5 file)> <path to model (HDF5 file)>
```
e.g.
```bash
python predict.py ./data/ecg_tracings.hdf5 ./model/model.hdf5
```

### STEP 5. The prediction result is stored in the file ```dnn_output.npy```, it is located in the same folder that appeared in STEP 3.

### STEP 6. Read the output file
Open 
```python
python predict.py ./data/ecg_tracings.hdf5 ./model/model.hdf5
```


