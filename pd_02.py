import pandas as pd

df = pd.read_csv('Data_dup.csv')
df_dupResul=df.duplicated()

for index in df_dupResul:
    print(index)

#df.to_excel("Data_dup.xlsx")