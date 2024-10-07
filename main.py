
import pandas as pd


def avg_prices(data):
    data["Average"] = (data["2020-01"] + data["2020-02"]) / 2


def sort(data):
    sorted_data = data.sort_values(by='Average')
    return sorted_data

def filter_data(data, value):
    filtered_data = data[data.Average < value]
    return filtered_data


def display_menu():
    selection = input("Select 1\n"
                      "0 - Filter\n"
                      "1 - Sort\n"
                      "2 - View table\n"
                      "- ")
    return selection


sales_prices = pd.read_csv("Sale_Prices_City.csv")
avg_prices(sales_prices)
selection = display_menu()
if selection == '0':
    filtered_data = filter_data(sales_prices, 186871)
    print(filtered_data)
elif selection == '1':
    sorted_data = sort(sales_prices)
    print(sorted_data.head(10))
elif selection == '2':
    print(sales_prices)
#print(sales_prices)
