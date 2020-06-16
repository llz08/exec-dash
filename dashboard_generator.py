# dashboard_generator.py

import os
import csv
import itertools
import datetime
from operator import itemgetter
import plotly
import plotly.graph_objs as go

def to_usd(my_price):
  # return "${0:,.2f}".format(my_price)
  return f"${my_price:,.2f}"

#
# INFO INPUTS
#

CSV_FILENAME = input("Please input csv file name format (sales-YYYYMM.csv): ") 

csv_filepath = os.path.join("data/monthly-sales", CSV_FILENAME)
print(csv_filepath)
rows = []

# Validation requirements
if not os.path.exists(csv_filepath):
    print("Error Didn't find a file at that location")
    quit()



with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for od in reader:
        rows.append(dict(od)) 


sales_prices = [float(row["sales price"]) for row in rows] 

total_sales = sum(sales_prices)

# Sorting

product_sales = []

date = rows[0]["date"]
print_date = datetime.datetime.strptime(date,"%Y-%m-%d").strftime("%B %Y")


sorted_rows = sorted(rows, key=itemgetter("product"))
rows_by_product = itertools.groupby(sorted_rows, key=itemgetter("product")) 

for product, product_rows in rows_by_product:
    monthly_sales = sum([float(row["sales price"]) for row in product_rows]) 
 
    product_sales.append({"name": product, "monthly_sales": monthly_sales})

sorted_product_sales = sorted(product_sales, key=itemgetter("monthly_sales"), reverse=True)
top_sellers = sorted_product_sales[0:7]

# INFO OUTPUTS


print("-------------------------")
print(f"SALES REPORT")
print("-----------------------")
print(f"MONTH: {print_date}")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL SALES: {to_usd(total_sales)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")

counter = 0
labels = []
values = []
sales_usd_list = []
for top_seller in top_sellers:
    counter = counter + 1
    product_name = top_seller["name"]
    sales_usd = to_usd(top_seller["monthly_sales"])
    sales_usd_list.append(sales_usd)
    print(f"  {counter}. {product_name} ({sales_usd})")  
    labels.append(product_name)
    values.append(top_seller["monthly_sales"])

# Data visualization
# Bar graph

trace = go.Bar(x=labels, y=values, text=sales_usd_list, textposition='auto')
data = [trace]
layout = go.Layout(
    title=f'Top Selling Product {print_date}',
    xaxis_title="Sales (USD)",
    yaxis_title="Product",
    yaxis_tickprefix="$",
    yaxis_tickformat = ',.2f'
)
plotly.offline.plot(dict(data=data, layout=layout), filename="pie_chart.html", auto_open=True)
