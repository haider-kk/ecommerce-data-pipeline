import pandas as pd

df = pd.read_csv("data/cleaned/final_dataset.csv")

print("Data loaded. Rows : ", len(df))

total_revenue = df['revenue'].sum()
print("Total Revenue:", total_revenue)

total_orders = df['order_id'].nunique()
print("Total Orders:", total_orders)


df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

monthly_revenue = df.groupby(df['order_purchase_timestamp'].dt.to_period('M'))['revenue'].sum()

print("\nMonthly Revenue : \n", monthly_revenue)



top_cities = df.groupby('customer_city')['revenue'].sum().sort_values(ascending=False).head(10)

print("\nTop Citiews by Revenue : \n", top_cities)



avg_delivery_time = df['delivery_time_days'].mean()

print("\nAverage delivery Time:", avg_delivery_time)



top_customers = df.groupby('customer_unique_id')['revenue'].sum().sort_values(ascending=False).head(10)

print("\nTop Customers: \n", top_customers)




print("\n--- BUSINESS INSIGHTS ---")

# Revenue concentration (Top cities)
top_5_city_revenue = df.groupby('customer_city')['revenue'].sum().sort_values(ascending=False).head(5)
top_5_total = top_5_city_revenue.sum()
overall_total = df['revenue'].sum()

print(f"\nTop 5 cities contribute {round((top_5_total / overall_total) * 100, 2)}% of total revenue")

# High value customers contribution
top_10_customers = df.groupby('customer_unique_id')['revenue'].sum().sort_values(ascending=False).head(10)
top_10_total = top_10_customers.sum()

print(f"Top 10 customers contribute {round((top_10_total / overall_total) * 100, 2)}% of total revenue")

# Delivery performance insight
avg_delivery = df['delivery_time_days'].mean()

if avg_delivery > 7:
    print("Delivery is slow — may affect customer satisfaction")
else:
    print(" Delivery speed is acceptable")
