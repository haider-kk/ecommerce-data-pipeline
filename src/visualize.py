import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/final_dataset.csv")

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

monthly_revenue = df.groupby(
    df['order_purchase_timestamp'].dt.to_period('M')
    )['revenue'].sum()

monthly_revenue.plot()

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Remove")
plt.show()



top_cities = df.groupby('customer_city')['revenue'].sum().sort_values(ascending=False).head(10)

top_cities.plot(kind='bar')

plt.title("Top 10 Cities by Revenue")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()



df['delivery_time_days'].plot(kind='hist',bins=30)

plt.title("Delivery Time Distribution")
plt.xlabel("Days")
plt.ylabel("Number of Orders")
plt.show()



top_customers = df.groupby('customer_unique_id')['revenue'].sum().sort_values(ascending=False).head(10)

top_customers.plot(kind='bar')

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer")
plt.ylabel("Revenue")
plt.show()
