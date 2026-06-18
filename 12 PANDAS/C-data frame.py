import pandas as pd
import numpy as np

employees = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Ragul", "Kabilesh", "Kathir", "Vel", "pradeep"],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Salary": [50000, 45000, 60000, 55000, 70000],
    "Experience": [2, 1, 4, 3, 5]
}

df = pd.DataFrame(employees)

# View data
print(df.head())
# Check dataset information
df.info()
# Select required columns
print(df[["Name", "Department", "Salary"]])
# Filter employees with salary above 55000
high_salary = df[df["Salary"] > 55000]
print(high_salary)
# Add new column
df["Bonus"] = [2000,1000,4000,3000,5000]
print(df)
# Update employee salary
df.loc[df["Employee_ID"] == 102, "Salary"] = 50000
print(df)
# Sort employees by salary
sorted_data = df.sort_values(by="Salary", ascending=False)
print(sorted_data)
# Find average salary
average_salary = df["Salary"].mean()
print(average_salary)
# Remove a column
df = df.drop("Bonus", axis=1)
print(df)
# Save cleaned data
df.to_csv("employee_data.csv", index=False)

employees= pd.read_csv("employee_data.csv")
print(employees)

