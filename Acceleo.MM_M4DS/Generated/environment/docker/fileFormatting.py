import pandas as pd
import json
import h5py
import pyarrow

wf_imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary=pd.read_csv('/wf_validation_python/data/pmmldb1/missing_input_dataDictionary.csv', sep = ',')
wf_imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary.to_parquet('/wf_validation_python/data/pmmldb1/missing_input_dataDictionary.parquet')

