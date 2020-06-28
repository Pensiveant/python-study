import numpy as np 
filepath=r'D:\pensiveant\github\python-study\radar\Z_RADR_I_Z9230_20200601190100_O_DOR_SA_CAP.npz'
data= np.load(filepath)
grid_array=data['grid_array']
print('test')