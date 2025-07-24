"""
Code by Sara Nuss

A tool to analyze housing market data using pandas.
This program uses a dataset of house prices by city
"""
import pandas as pd

# Add a column with the average of the months in 2020
def avg_prices(data):
    data["Average2020"] = (data["2020-01"] + data["2020-02"]) / 2

# sort the data from least to greatest and display the first 10 cities
def sort(data):
    sorted_data = data.sort_values(by='Average2020')
    print(sorted_data.head(10))

# filter the data based on a user-given price.
def filter_data(data):\
    # what price should we filter by?
    value = input("Enter price: ")
    # show data less than or greater than?
    direction = input("Show data greater than or less than entered price? Enter 'g' or 'l' ")
    filtered_data = None
    if direction == 'g':
        filtered_data = data[data.Average2020 > float(value)]
    elif direction == 'l':
        filtered_data = data[data.Average2020 < float(value)]
    print(filtered_data)

# display the row of a given city
def find_city(sales_prices):
    # what city?
    user_location = input("City: ")
    sp_city = sales_prices[(sales_prices["RegionName"] == user_location)]
    print(sp_city)

# put amenu on the screen
def display_menu():
    user_selection = input("Select 1\n"
                      "0 - Filter by house price\n"
                      "1 - See 10 least expensive cities\n"
                      "2 - View table\n"
                      "3 - Find City\n"
                      "- ")
    return user_selection

# run the program

# make a data frame with dataset
sales_prices_unedited = pd.read_csv("Sale_Prices_City.csv")

# add the average column
avg_prices(sales_prices_unedited)

# remove unwanted columns
sales_prices = sales_prices_unedited[["RegionName", "StateName", "SizeRank", "Average2020"]]

# what does the user want to do?
selection = display_menu()
if selection == '0':
    filter_data(sales_prices)
elif selection == '1':
    sort(sales_prices)
elif selection == '2':
    print(sales_prices)
elif selection == '3':
    find_city(sales_prices)

