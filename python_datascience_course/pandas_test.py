import pandas as pd
x = {'Name': ['Samir', 'Jane', 'Ron'], 'Age': [18, 23, 16], 'College': ['UMBC', 'UMBC', 'UMBC']}
df = pd.DataFrame(x)
print(df)
df1 = df[df['Age'] < 20]
print(df1)