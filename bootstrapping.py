import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
data = pd.read_csv('/content/Housing Form Edited.csv')
data = data.drop(columns=['Timestamp'], axis=1)
data.head(20)
data['Name Of Apartment/ Area of House?'].value_counts()
sns.countplot(x='Name Of Apartment/ Area of House?', data = data)
plt.xticks(rotation=90, ha='center')
plt.show() 
from pandas.tseries import frequencies
categorical_columns = ['What Is Your Major?','What Type Of Housing Are You In?','Name Of Apartment/ Area of House?','How many roommates/ flatmates do you have?','How Much Is Your Individual Rent?','Rate Your Convenience for Commuting to College','Rate Your Housing Facilities (ie pool, gym etc.)','Rate Your Rent Value (Is it value for your money?)','Rate Your Apartment Safety','Rate Your Apartment Layout','Rate Proximity To Grocery Stores/ Restaurants','Does Your Apartment Allow Subleasing?','Please Rate Your Housing Overall']
num_samples = 200 - len(data)

sampled_data = pd.DataFrame(columns=data.columns)
for col in categorical_columns:
  frequencies = data[col].value_counts(normalize=True)

  samples = np.random.choice(frequencies.index, size = num_samples, p=frequencies.values)

  new_data = pd.DataFrame({col: samples})
  sampled_data = pd.concat([sampled_data, new_data], axis=1)
extended_data = pd.concat([data, sampled_data], axis=1)

extended_data = extended_data.reset_index(drop=True)
extended_data.to_csv("Output.csv", index=False)
files.download('Output.csv')
NewData = pd.read_csv('/content/Output Form Edited.csv')
len(NewData)
for col in categorical_columns:
  NewData[col].value_counts()
  sns.countplot(x=NewData[col], data = NewData)
  plt.xticks(rotation=90, ha='center')
  plt.show()
