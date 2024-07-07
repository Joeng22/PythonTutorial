import pandas as pd


def main():
    l1 = [1,2,3,4,5]
    df = pd.DataFrame(l1)
    print("l1:",type(l1))
    print("df:",type(df))
    print(df)


    dict_1 = {"A":[1,2,3],"B":[2,3,4],"C":[3,4,5],"D":[4,5,6]}
    df2 = pd.DataFrame(dict_1)
    print(df2)
if __name__=="__main__":
    main()