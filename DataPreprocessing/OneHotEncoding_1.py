#One Hot encoding tutorial using sklearn

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def main():
    data = {'Employee id': [10, 20, 15, 25, 30],
        'Gender': ['M', 'F', 'F', 'M', 'F'],
        'Remarks': ['Good', 'Nice', 'Good', 'Great', 'Nice'],
        }
    
    df = pd.DataFrame(data)

    print(df)

    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    #print(categorical_columns)


    encoder = OneHotEncoder(sparse=False)

    one_hot_encoded = encoder.fit_transform(df[categorical_columns])
    print(one_hot_encoded)

    one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names(categorical_columns))

    # Concatenate the one-hot encoded dataframe with the original dataframe
    df_encoded = pd.concat([df, one_hot_df], axis=1)

    # Drop the original categorical columns
    df_encoded = df_encoded.drop(categorical_columns, axis=1)

    # Display the resulting dataframe
    print(f"Encoded Employee data : \n{df_encoded}")

if __name__=="__main__":
    main()