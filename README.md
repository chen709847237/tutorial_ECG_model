# tutorial_ECG_model
## A Tutorial for classifying ECG signals by using CNN model
 
## References
```
Ribeiro, A.H., Ribeiro, M.H., Paixão, G.M.M. et al. Automatic diagnosis of the 12-lead ECG using a deep neural network.
Nat Commun 11, 1760 (2020). https://doi.org/10.1038/s41467-020-15432-4
```
## Model and Data
The scripts and detail of this model are available at: [Here](https://github.com/antonior92/automatic-ecg-diagnosis)
Model Download: [Here](https://zenodo.org/record/3765717#.YCOS8xMzbqU)
Test Data Download: [Here](https://zenodo.org/record/3765780#.YCOS8hMzbqU)

## Requirements 
TBC.

## Run the script
### 1. Activate the anaconda
```bash
conda activate
```
### 2. Enter the environment
```bash
conda activate <name of environment>
```
e.g.
```bash
conda activate ecg
```

### 3. Enter the folder where the "automatic-ecg-diagnosis" scripts are stored.
```bash
cd <path of folder>
```
e.g.
```bash
cd /user/scripts/ECG/automatic-ecg-diagnosis-master/
```

### 4. Run the script
```bash
python predict.py <path to test data (HDF5 file)> <path to model (HDF5 file)> --ouput_file <path of output folder/name of output file> 
```
e.g.
```bash
python predict.py ./data/ecg_tracings.hdf5 ./model/model.hdf5 --ouput_file ./predict_output
```

### 5. The name of output file will end in ```.npy```



#### Example:
```bash
python prediction.py -t breast -m ./model/ -d ./test_breast.fasta -o ./result/
```

