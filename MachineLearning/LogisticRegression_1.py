#Logistic regression tutorial
import numpy as np
from sklearn import linear_model

def main():
    X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
    y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])


    model = linear_model.LogisticRegression()
    model.fit(X,y)

    print(model.coef_)

    print(model.predict(np.array([3.46]).reshape(-1,1)))

if __name__=="__main__":
    main()