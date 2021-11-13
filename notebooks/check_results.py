import numpy as np
from scipy.io import loadmat

c1vals = [0.025, 0.05, 0.075]
c2vals = [0.2, 0.3, 0.4]

for i in range(3):
	for j in range(3):
		av_val = 0; av_train = 0
		for k in range(10):
			perfdict = loadmat(f'Models/run_{k+1}_{i}_{j}.mat')
			av_val += np.max(perfdict['val_accuracy'])/10 
			av_train += np.max(perfdict['accuracy'])/10 
			
		print(f'c1 = {c1vals[i]}; c2 = {c2vals[j]}; train_acc = {av_train}; val_acc = {av_val}') 
