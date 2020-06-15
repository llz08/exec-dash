# dashboard_generator.py

import os
import csv

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

month = "MARCH" # TODO: get from file name or date values
year = 2018 # TODO: get from file name or date values

#
# INFO OUTPUTS
#


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
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")