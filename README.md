# Fruit-Disease-Detection

The following items must be present in the working directory:
* The file "Train.csv"
* The directory "Train_Images" so that the path to each training image is 
"Train_Images/Image_ID.jpg"
	  
The following notebooks are included in the "notebooks" directory:
* "preprocess.ipynb": reads the training images, converts them to numpy arrays and
splits them into a training and a validation set.
* "Dataset_investigation.ipynb": is used to recover various statistics about the training
set.
* "architecture_comparison.ipynb": performs exploratory training runs to compare two
proposed architectures.
* "training.ipynb": performs a grid search for hyperparameters related to data augmentation
and dropout regularisation. Training and generalisation set results histories are saved 
in the "Models" directory. The hyperparameter combination with the highest average 
maximum generalisation set accuracy is selected. "check_results.py" can be used to print 
the results.
* "testing.ipynb": completes 60 training runs with the optimal hyperparameter combination.
Training and generalisation set results histories as well as the model configuration with
the highest generalisation set accuracy is saved in the "Test_models" directory.
* "process_results.ipynb": tests each of the 60 trained models on the validation set and
saves all training, generalisation and validation set results in a single output file
"results.mat".
* "evaluate_results.ipynb": extracts average results and standard deviations from
"results.mat".
	   
The dataset used with this project is available at:
https://zindi.africa/competitions/makerere-passion-fruit-disease-detection-challenge
