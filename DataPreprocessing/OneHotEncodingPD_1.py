#One hot encoding tutorial using Pandas
import pandas as pd

def main():
    data = {'Employee id': [10, 20, 15, 25, 30],
            'Gender': ['M', 'F', 'F', 'M', 'F'],
            'Remarks': ['Good', 'Nice', 'Good', 'Great', 'Nice'],
            }

    df = pd.DataFrame(data)

    print(df)

    onehotencodeddf = pd.get_dummies(df,columns=["Gender","Remarks"],dtype='int')
    print(onehotencodeddf)

if __name__=="__main__":
    main()