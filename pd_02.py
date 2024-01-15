import pandas as pd

df = pd.read_excel('data2.xlsx')

df.dropna(inplace = True)

print(df.to_string)

for 
df.to_excel("data2_result.xlsx")