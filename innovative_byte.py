import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def read_data(path):
    data=pd.read_csv(path)
    return data

def data_cleaning(df):
    df.dropna(how="all",inplace=True)
    df.drop_duplicates(inplace=True)
    df.drop('Discount',axis=1,inplace=True)
    
    string_columns = df.select_dtypes(include='object').columns
    for col in string_columns:
        df[col] = df[col].str.strip()
    return df
def descriptive_stats(df):
    total_sales = df['Sales'].sum()
    average_order_value = df['Sales'].mean()
    return total_sales, average_order_value

def vizualize_descriptive_stats(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Sales'], kde=True)
    plt.title('Distribution of Sales')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(df['Quantity'], kde=True)
    plt.title('Distribution of Order Quantity')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df['Sales'])
    plt.title('Boxplot of Sales')
    plt.show()

def customer_segmentation(df):
    df = df.reset_index()
    customer_data = df.groupby(df.index).agg(TotalSales=('Sales', 'sum'), NumPurchases=('Sales', 'count'))
    if len(customer_data['TotalSales'].unique()) >= 4:
        customer_data['SalesSegment'] = pd.qcut(customer_data['TotalSales'], 4, labels=['Low', 'Medium', 'High', 'Very High'])
    else:
        customer_data['SalesSegment'] = 'Low'

    if len(customer_data['NumPurchases'].unique()) >= 4:
        customer_data['PurchasesSegment'] = pd.qcut(customer_data['NumPurchases'], 4, labels=['Low', 'Medium', 'High', 'Very High'])
    else:
        customer_data['PurchasesSegment'] = 'Low'
    return customer_data 

def customer_segmentation_analysis(customer_data):
    sales_segment_stats = customer_data.groupby('SalesSegment', observed=False)[['TotalSales', 'NumPurchases']].describe()
    purchases_segment_stats = customer_data.groupby('PurchasesSegment', observed=False)[['TotalSales', 'NumPurchases']].describe()

    print("Sales Segment Stats:\n", sales_segment_stats)
    print("Purchases Segment Stats:\n", purchases_segment_stats)

def top_selling_products(df):
    top_products = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
    print("Top selling products:\n", top_products.head())

    top_categories = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    print("Top selling categories:\n", top_categories.head())

def vizualization(df):
    total_sales_by_category = df.groupby('Category')['Sales'].sum()
    total_sales_by_category.plot(kind='bar')
    plt.title('Total Sales by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Sales')
    plt.show()
    plt.hist(df['Sales'], bins=30)
    plt.title('Distribution of Order Values')
    plt.xlabel('Order Value')
    plt.ylabel('Frequency')
    plt.show()

    numeric_cols = df.select_dtypes(include=[np.number])
    correlation_matrix = numeric_cols.corr()
    sns.heatmap(correlation_matrix, annot=True)
    plt.title('Correlation Matrix of Numerical Variables')
    plt.show()

path="comprehensive_retail_sale_analysis/SampleSuperstore.csv"
df=read_data(path)
df=data_cleaning(df)
total_sales, average_order_value = descriptive_stats(df)
print("Sum_of_sales:",total_sales,"average_order_value:",average_order_value)
vizualize_descriptive_stats(df)
customer_data = customer_segmentation(df)
print(customer_data.head())
customer_segmentation_analysis(customer_data)
top_selling_products(df)
vizualization(df)

