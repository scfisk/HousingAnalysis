# Code by Sara Nuss

# A tool to analyze housing market data using pandas.
# This program uses a dataset of house prices by city

import pandas as pd


def avg_prices(data):
    data["Average2020"] = (data["2020-01"] + data["2020-02"]) / 2

def sort(data):
    sorted_data = data.sort_values(by='Average2020')
    print(sorted_data.head(10))

def filter_data(data):
    value = input("Enter price: ")
    direction = input("Show data greater than or less than entered price? Enter 'g' or 'l' ")
    filtered_data = None
    if direction == 'g':
        filtered_data = data[data.Average2020 > float(value)]
    elif direction == 'l':
        filtered_data = data[data.Average2020 < float(value)]
    print(filtered_data)

def display_menu():
    user_selection = input("Select 1\n"
                      "0 - Filter by house price\n"
                      "1 - Sort\n"
                      "2 - View table\n"
                      "3 - Find City\n"
                      "- ")
    return user_selection

def find_city(sales_prices):
    user_location = input("City: ")
    sp_city = sales_prices[(sales_prices["RegionName"] == user_location)]
    print(sp_city)

sales_prices_unedited = pd.read_csv("Sale_Prices_City.csv")
avg_prices(sales_prices_unedited)
sales_prices = sales_prices_unedited[["RegionName", "StateName", "SizeRank", "Average2020"]];
selection = display_menu()
if selection == '0':
    filter_data(sales_prices)
elif selection == '1':
    sort(sales_prices)
elif selection == '2':
    print(sales_prices)
elif selection == '3':
    find_city(sales_prices)
#print(sales_prices)
