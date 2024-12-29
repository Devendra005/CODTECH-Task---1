import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')
print(df.head())
df.info()
df.isnull().sum()
df.describe()

fig, axs = plt.subplots(9, 1, dpi=95, figsize=(7, 17))
i = 0
for col in df.columns:
    axs[i].boxplot(df[col], vert=False)
    axs[i].set_ylabel(col)
    i += 1
plt.show()

plt.pie(df.Outcome.value_counts(),
        labels=['Diabetes', 'Not Diabetes'],
        autopct='%.f', shadow=True)
plt.title('Outcome Proportionality')
plt.show()
