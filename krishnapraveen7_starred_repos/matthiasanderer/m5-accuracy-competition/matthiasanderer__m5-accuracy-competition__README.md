# M5 Accuracy Competition - 2nd place solution

Below you can find a outline of how to reproduce my solution for the M5 Forecasting - Accuracy competition.
If you run into any trouble with the setup/code or have any questions please contact me at matthias.anderer@googlemail.com

The notebooks were run as Kaggle kernels / Colab notebooks - so we actually never executed the code locally.

# Repository contents
* m5-simple-fe-evaluation.ipynb	== feature preprocessing notebook
* m5-final-XX.ipynb == bottom level (lvl12) train and predict notebook
* m5-nbeats-toplvl.ipynb == top level (lvl1-5) train and predict notebook
* m5-alignandsubmit.ipynb == notebook to align bottom level with top level results
* gluonts-20200710T072218Z-001.zip == modified glutonts version (added lookahead to Trainer)

# Before you start..
1)Make sure to add gluonts to the path of the N-BEATS notebook<br>
```shell
unzip gluonts-20200710T072218Z-001.zip
```

2) Next you have to load the competition data from kaggle - assuming you use cli<br>
(Again make sure to adapt the paths to your environment)
```shell
mkdir input
cd input
kaggle competitions download -c m5-forecasting-accuracy
cd ..
```

# DATA PROCESSING
Before running please change the path settings in the m5-simple-fe-evaluation.ipynb notebook to match your local environment<br>
(Search for "Load Data" in notebook)
```shell
jupyter notebook m5-simple-fe-evaluation.ipynb
```
The resulting files grid_part_1.pkl, grid_part_2.pkl, grid_part_3.pkl will be created in the working directory and are the input for the next step

# BOTTOM LEVEL MODEL: 
For each loss_multiplier that shall be tested the notebook m5-final-XX.ipynb has to be run<br>
<br>
Before running the LOSS_MULTIPLIER variable has to be set to the desired value. <br>
(The values used for ensembling the final submission to the competition were: 0.9 , 0.93, 0.95, 0.97, 0.99 - so to reproduce the results you will need to run the notebook once for each parameter)
<br>
Before running please change the path settings in the m5-final-XX.ipynb notebook to match your local environment<br>
Search for "#PATHS for Features" in notebook - here the path has to match the output pwd of the DATA PROCESSING STEP
```shell
jupyter notebook m5-final-XX.ipynb
```
The notebook will create temporary model and test data files that you should delete after each run
```shell
rm *.pkl
rm *.bin
```
The notebook will create a "submission_vX.csv" file that contains the bottom level predictions for the chosen loss multiplier

FOR THIS TO WORK LOCALLY YOU WILL HAVE TO RENAME THIS OUTPUTFILE TO A UNIQUE NAME BEFORE RE-RUNNING THIS STEP WITH A DIFFERENT MULTIPLIER OTHERWISE IT WILL BE OVERWRITTEN

# TOP LEVEL MODEL:
* The model will try to install the required mxnet version as well as pydantic and ujson - if you do not want this to happen comment the resprective pip install lines in the notebook before running.
* Before running please make sure that the gluonts package path matches you local setup: Search for "package_path" in the notebook
* Before running please make sure that the m5_input_path matches your local setup: Search for "m5_input_path" in the notebook
* Before running please make sure that the data paths match your local setup: Search for "Load data" in the notebook
* Before running please make sure that the output paths match your desired local setup: Search for "to_csv" in the notebook
* You will need a CUDA/GPU environment for running this notebook - please make sure that the mxnet pip install matches your Cuda and mkl setup (cu101mkl is for Cuda 10.1 with mkl)

( In the competition we ran the NBEATS top level twice: Once with the configuration in the notebook which is referred to as "nbeats_toplvl_forecasts2.csv" and once with the setting: "epochs=10" in the Trainer object: Search for "Trainer(" in the notebook. The latter configuration is referred to as "nbeats_toplvl_forecasts1.csv" )

( IF YOU WANT TO USE DIFFERENT NBEATS REFERENCE PREDICTIONS MAKE SURE TO HAVE UNIQUE OUTPUT FILENAMES OTHERWISE THE OUTPUT FILE WILL BE OVERWRITTEN ON RE-RUN )
```shell
jupyter notebook m5_nbeats_toplvl.ipynb
```

# FINAL ALIGNMENT:

Finally the bottom level forecasts have to be aligned with the top level forecasts

* Before running please make sure that the paths for the NBEATS reference predictions match your local setup (i.e. the output files you created in the top level model step) : See "nbeats_pred01_df" and "nbeats_pred02_df" in the notebook
* Before running please make sure that the paths for the bottom level model predictions match your local setup (i.e. the output files you created in the bottom level model step) : See "if BUILD_ENSEMBLE:" 
* Before running please make sure that the paths for the competition data match your local setup: Search "validation_gt_data = pd.read_csv" in the notebook
```shell
jupyter notebook m5-alignandsubmit.ipynb
```
