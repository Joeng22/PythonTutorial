#Machine learning tutorial - 2
# Standard deviation

import numpy as np

speed = [86,87,88,86,87,85,86]

x = np.std(speed)

print("stanard deviation:",x)
print("variance:",np.var(speed))