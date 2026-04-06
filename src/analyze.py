import pandas as pd
customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

print("Customers Data Sample : \n",customers.head())
print("\nOrders Data Sample : \n",orders.head())

print("\nCustomers Info :")
customers.info()

print("\nOrders Info :")
orders.info()

print("\nMissing Values (Customers):")
print(customers.isnull().sum())

print("\nMissing Values (Orders):")
print(orders.isnull().sum())

customers.fillna("Unknown", inplace = True)
orders = orders.copy()

orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'], errors='coerce')
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'], errors='coerce')

orders['delivery_time_days'] = (orders['order_delivered_customer_date'] -
                                orders['order_purchase_timestamp']).dt.days
orders['order_year'] = orders['order_purchase_timestamp'].dt.year
orders['order_month'] = orders['order_purchase_timestamp'].dt.month

customers.drop_duplicates(inplace=True)
orders.drop_duplicates(inplace=True)

customers.to_csv("data/cleaned/customers_cleaned.csv", index=False)
orders.to_csv("data/cleaned/orders_cleaned.csv", index=False)


