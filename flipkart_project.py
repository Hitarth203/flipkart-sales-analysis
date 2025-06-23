import pandas as pd
from datetime import datetime 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_excel("/Users/hitarthwadhwani/Desktop/practice_files/OnlineOrders_of_a_ecommerce_website.xlsx")

df["brand"] = df["brand"].str.title()

# Checking if there are any outliers present in the data 

z_scores = np.abs(stats.zscore(df['retail_price']))
outliers = df[z_scores > 3]
# print(f"Number of outliers in Retail Price: {len(outliers)}")

#Dropping the outliers
z = np.abs(stats.zscore(df['retail_price']))
df = df[z < 3].copy()

#Extracting date and time components from a crawl_timestamp column 

df['crawl_timestamp'] = pd.to_datetime(df['crawl_timestamp'], errors='coerce')

df['year'] = df['crawl_timestamp'].dt.year
df['month'] = df['crawl_timestamp'].dt.month
df['day'] = df['crawl_timestamp'].dt.day
df['hour'] = df['crawl_timestamp'].dt.hour
df['minute'] = df['crawl_timestamp'].dt.minute
df['date_only'] = df['crawl_timestamp'].dt.date
df['time_only'] = df['crawl_timestamp'].dt.time


#Q1:Exctracting best month for sales, How much was earned that month.
monthly_sales = df.groupby('month')['discounted_price'].sum().sort_values(ascending=False)

best_month = monthly_sales.idxmax()
best_amount = monthly_sales.max()

print(f"Best month for sales: {best_month}")
print(f"Total revenue in that month: ₹{best_amount:,.2f}")

# Converting PeriodIndex to string 
monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(8, 8))
plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%', startangle=140)

plt.title("Sales Distribution by Month (Q1)")
plt.axis('equal') 
plt.tight_layout()
plt.savefig("/Users/hitarthwadhwani/Desktop/flipkart-sales-analysis/monthly_sales_pie1.png", dpi=300)
# plt.show()


#Q2:What time should we display advertisements to maximize purchases?
hourly_orders = df['hour'].value_counts().sort_index()

hourly_orders.plot(kind='line')
plt.title("Purchases by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Orders")
plt.grid(True)
plt.tight_layout()
plt.savefig("/Users/hitarthwadhwani/Desktop/flipkart-sales-analysis/hourly_sales_line1.png", dpi=300)
# plt.show()

#Q4:Top 10 products sold most in that six-month period?

top_products = df['product_name'].value_counts().head(10)

top_products.plot(kind='bar')
plt.title("Top 10 Sold Products")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("/Users/hitarthwadhwani/Desktop/flipkart-sales-analysis/top_10_products_sold1.png", dpi=300)
# plt.show()

# Remove square brackets and quotes, then split by >>
df['Main_Category'] = df['product_category_tree'].str.strip("[]").str.replace("'", "", regex=False)
df['Main_Category'] = df['Main_Category'].str.strip().str.strip('"')
category_counts = df['Main_Category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Count']


#Visualize Top 10 Product Categories by Sales Count
plt.figure(figsize=(12, 6))
sns.barplot(data=category_counts.head(10), x='Count', y='Category')
plt.title("Top 10 Product Categories by Sales Count")
plt.xlabel("Number of Products Sold")
plt.ylabel("Main Category")
plt.tight_layout()
plt.savefig("/Users/hitarthwadhwani/Desktop/flipkart-sales-analysis/top_categories_bar1.png", dpi=300)
# plt.show()

#Adding Serial number
df["Sr. No."] = range(1,len(df)+1)

# Reordering the columns 
cols = ['Sr. No.', 'crawl_timestamp', 'product_name', 'retail_price', 'discounted_price',
        'brand', 'product_category_tree', 'Main_Category',
        'year', 'month', 'day', 'hour', 'minute', 'date_only', 'time_only']

df = df[cols]

#Dropping the crawl_timestamp Column
df.drop(columns=['crawl_timestamp'], inplace=True)

df.to_excel("/Users/hitarthwadhwani/Desktop/practice_files/cleaned_flipkart_data_final.xlsx", index=False)

print("Reached end of script")
