#Machine learning tutorial -3
# Percentile

import numpy as np
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = np.percentile(ages,95.23809523809524)
print("Percentile:",x)