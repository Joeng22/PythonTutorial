#linear regression

from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats




def main():
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    plt.scatter(x,y)
    plt.show()

    slope, intercept, r, p, std_err = stats.linregress(x, y)
    print(slope, intercept, r, p, std_err)


    def myfunc(x):
        return slope * x + intercept
    
    mymodel = list(map(myfunc, x))
    plt.scatter(x,y)
    plt.plot(x, mymodel)
    plt.show()

if __name__=="__main__":
    main()