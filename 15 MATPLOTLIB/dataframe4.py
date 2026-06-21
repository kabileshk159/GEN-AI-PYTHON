import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "Sales": [20000,25000,22000,30000,35000,40000],
    "Orders": [120,150,130,180,220,250],
    "Profit": [5000,7000,6000,9000,12000,15000]
}

df = pd.DataFrame(data)

print(df)


# 1. BAR GRAPH - Sales
plt.figure(figsize=(7,4))
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# 2. LINE GRAPH - Sales Trend
plt.figure(figsize=(7,4))
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Sales Growth Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# 3. LINE GRAPH - Profit
plt.figure(figsize=(7,4))
plt.plot(df["Month"], df["Profit"], marker="o")
plt.title("Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()


# 4. PIE CHART - Order Distribution
plt.figure(figsize=(6,6))
plt.pie(df["Orders"], labels=df["Month"], autopct="%1.1f%%")
plt.title("Orders Percentage")
plt.show()


# 5. SCATTER GRAPH - Sales vs Profit
plt.figure(figsize=(7,4))
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit Relationship")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()


# 6. BAR GRAPH - Orders
plt.figure(figsize=(7,4))
plt.bar(df["Month"], df["Orders"])
plt.title("Monthly Orders")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.show()
