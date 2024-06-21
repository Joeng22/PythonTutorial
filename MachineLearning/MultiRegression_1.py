import pandas as pd
from sklearn import linear_model
def main():
    df = pd.read_csv("data.csv")

    print(df.head())

    x = df[["Volume","Weight"]]
    y = df[["CO2"]]

    print("x:",x)
    print("y:",y)

    mymodel = linear_model.LinearRegression()
    mymodel.fit(x,y)
    print(mymodel.coef_)
    predictedCO2 = mymodel.predict([[2300, 1300]])

    print(predictedCO2)
if __name__=="__main__":
    main()