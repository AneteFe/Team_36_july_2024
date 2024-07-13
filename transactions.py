import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("/content/transaction_dataset.csv")

gender_counts = dataset['Gender'].value_counts(dropna=False)
gender_counts.plot(kind='bar', color=['skyblue'])

plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Transactions by Gender')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

#Task 3: Create a filtered DataFrame that includes Category == 'Clothing' and Gender == 'M'. How many rows are there in this filtered DataFrame? Format the result as follows: The filtered DataFrame has XXXX rows. - hard 

dataset = pd.read_csv('/content/transaction_dataset.csv')

#Task 2: Create a horizontal bar chart that shows the top 5 most frequent names in the DataFrame, based on the 'name' column. (First, create a grouped DataFrame (name_df), then filter it using iloc, and finally create the visualization.) -medium
names= dataset['Name']
name_df = pd.DataFrame(names)['Name'].value_counts().reset_index()
filtered_names = name_df.iloc[:5, :]
filtered_names
plt.barh(filtered_names['Name'], filtered_names['count'], color = 'lightgreen')
plt.title('Top 5 most frequent names in the DataFrame')
plt.xlabel('Numbers')
plt.ylabel('Names')
plt.show()
