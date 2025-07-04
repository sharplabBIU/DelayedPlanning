import pandas as pd

# Load the CSV file
df = pd.read_csv('study2_demographics.csv')

# Filter the DataFrame for subjects with Status == "APPROVED"
approved_df = df[df['Status'] == 'APPROVED']

# Convert the 'Age' column to numeric values, coercing errors to NaN
approved_df['Age'] = pd.to_numeric(approved_df['Age'], errors='coerce')

# Calculate the average age, skipping NaN values
average_age = approved_df['Age'].mean()

# Calculate the distribution of sex
sex_distribution = approved_df['Sex'].value_counts(normalize=True) * 100

# Display the results
print(f'Average Age: {average_age:.2f}')
print('Sex Distribution:')
print(sex_distribution)

# Optionally, you can print the distribution in a more readable format
for sex, percentage in sex_distribution.items():
    print(f'{sex}: {percentage:.2f}%')
