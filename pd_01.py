import pandas as pd

df = pd.read_csv('data1.csv')

df.dropna(inplace = True)

print(df.to_string)


'''
for index,row in df.iterrows():
    print(row)
    print()


'''