import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Filter rows where Age > 30
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

# Add a new column
df['Salary'] = [70000, 80000, 90000]
print("\nDataFrame with new column:")
print(df)
