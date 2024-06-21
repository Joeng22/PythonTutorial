from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
def main():
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    mymodel = np.poly1d(np.polyfit(x,y,3))

    myline = np.linspace(1, 22, 100)

    print("myline:",myline)
    plt.scatter(x, y)
    plt.plot(myline, mymodel(myline))
    plt.show()

    print(r2_score(y, mymodel(x)))

if __name__=="__main__":
    main()

