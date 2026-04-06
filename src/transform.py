import pandas as pd

customers = pd.read_csv("data/cleaned/customers_cleaned.csv")
orders = pd.read_csv("data/cleaned/orders_cleaned.csv")

print("Customers rows : ", len(customers))
print("Orders rows :", len(orders))

merged_data = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="inner"
)

print("Merged Rows : ", len(merged_data))

print("\nMerged data Sample :")
print(merged_data.head())

merged_data.to_csv("data/cleaned/merged_data.csv", index =False)
print("\nMerged dataset created successfully")

payments = pd.read_csv("data/raw/olist_order_payments_dataset.csv")
print("Payments rows:", len(payments))

final_data = pd.merge(
    merged_data,
    payments,
    on="order_id",
    how="inner"
)
print("Final merged rows :", len(final_data))

final_data['revenue'] = final_data['payment_value']

final_data.to_csv("data/cleaned/final_dataset.csv", index=False)
print("Final dataset with revenue created")
