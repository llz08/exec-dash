# dashboard_generator.py

import os
import csv
import itertools
from operator import itemgetter

def to_usd(my_price):
  # return "${0:,.2f}".format(my_price)
  return f"${my_price:,.2f}"

#
# INFO INPUTS
#

CSV_FILENAME = "sales-201803.csv"

csv_filepath = os.path.join("data/monthly-sales", CSV_FILENAME)
print(csv_filepath)
rows = []

with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for od in reader:
        rows.append(dict(od)) 


sales_prices = [float(row["sales price"]) for row in rows] 

total_sales = sum(sales_prices)

# Sorting

product_sales = []

sorted_rows = sorted(rows, key=itemgetter("product"))
rows_by_product = itertools.groupby(sorted_rows, key=itemgetter("product")) 

for product, product_rows in rows_by_product:
    monthly_sales = sum([float(row["sales price"]) for row in product_rows]) 
    product_sales.append({"name": product, "monthly_sales": monthly_sales})

sorted_product_sales = sorted(product_sales, key=itemgetter("monthly_sales"), reverse=True)
top_sellers = sorted_product_sales[0:3]

month = "MARCH" # TODO: get from file name or date values
year = 2018 # TODO: get from file name or date values


# INFO OUTPUTS


print("-------------------------")
print(f"SALES REPORT")
print("-----------------------")
print(f"MONTH: {month} {year}")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL SALES: {to_usd(total_sales)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")

counter = 0
for top_seller in top_sellers:
    counter = counter + 1
    product_name = top_seller["name"]
    sales_usd = to_usd(top_seller["monthly_sales"])
    print(f"  {counter}. {product_name} ({sales_usd})")