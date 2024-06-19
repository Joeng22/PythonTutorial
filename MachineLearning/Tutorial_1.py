#Machine learning statistics tutorial - 1 
#Mean/median/Mode 


import numpy as np
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

print("Mean:",np.mean(speed))
print("Median:",np.median(speed))
print("Mode:",stats.mode(speed))