
import pandas as pd
import matplotlib.pyplot as plt

# Bitte noch folgende Module installieren
# pip install matplotlib
# pip install openpyxl

'''
df = pd.DataFrame({'length': [1.5, 0.5, 1.2, 0.9, 3],
                  'width': [0.7, 0.2, 0.15, 0.2, 1.1]},
                  index=['pig', 'rabbit', 'duck', 'chicken', 'horse'])
'''

df = pd.read_excel("pd_04_to_excel.xlsx")
print(df)
df=df.set_index("Town")

print(df)

plot = df.plot(title="DataFrame Plot")

plt.show()
