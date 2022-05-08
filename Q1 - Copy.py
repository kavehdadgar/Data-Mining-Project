import pandas as pd
import numpy as np

df = pd.read_csv('SARS-CoV-2 Dataset Updated.csv')

df.drop(index=df[df['location'] == 'Northern Cyprus'].index, inplace=True)
df.drop(index=df[df['location'] == 'International'].index, inplace=True)

cols = ["people_vaccinated" , "new_cases" , "new_deaths"]
cols2 = ["total_vaccinations" , "people_fully_vaccinated"]

df.update(df.groupby("location")[cols].fillna(0))
df.update(df.groupby("location")[cols2].ffill().fillna(0))

df.to_csv('Output1.csv')
print("Done!")
