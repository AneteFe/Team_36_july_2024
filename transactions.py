import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("/content/transaction_dataset.csv")

gender_counts = dataset['Gender'].value_counts(dropna=False)
gender_counts.plot(kind='bar', color=['skyblue'])

plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Transactions by Gender')

plt.show()
