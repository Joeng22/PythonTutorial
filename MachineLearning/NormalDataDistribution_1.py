#Normal data distribution display
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.random.normal(5.0,1.0,100000)

    plt.hist(x,100)
    plt.show()
if __name__=="__main__":
    main()