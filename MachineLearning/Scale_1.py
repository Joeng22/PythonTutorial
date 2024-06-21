from sklearn.preprocessing import StandardScaler
import pandas as pd

def main():
    scale = StandardScaler()
    df = pd.read_csv("data.csv")

    x = df[["Volume","Weight"]]
    print("x:",x)

    scaledx = scale.fit_transform(x)
    print("scaledx:",scaledx)
    
if __name__=="__main__":
    main()