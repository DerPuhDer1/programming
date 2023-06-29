import requests
import time
from bs4 import BeautifulSoup

def export_data(list_of_stocks):
    export_file = open("stocks.csv", "w")

    #Write a header row in the csv file
    header_row = ""
    for key in list_of_stocks[0]:
        header_row += key+","

    export_file.write(f"{header_row}\n")

    #loop through list of stocks
    for stock in list_of_stocks:
        stock_record = ""
        #Write stock indicators to the file
        for indicator, value in stock.items():
            stock_record += value+","
        #Write record to file
        export_file.write(f"{stock_record}\n")
    export_file.close()
    return

def main():
    headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
    
    symbols_list = ["GOOGL", "IBM", "SBUX", "AMC", "NFLX", "TSLA", "BA"]
    list_of_stock_dictionaries = []
    for symbol in symbols_list:
        print(f"Requesting data for {symbol} stock")
        url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'

        #Request the page
        response = requests.get(url, headers = headers)

        #parse html and create a beautiful soup object
        soup = BeautifulSoup(response.text, 'html.parser')

        stock_dictionary = {}
        stock_dictionary['symbol'] = symbol

        stock_dictionary = {}

        counter = 1
        #Loop through the cell in the table
        for cell in soup.find_all('td'):
            #odd iterations are keys. Set key on odd number iteration
            if counter % 2 != 0:
                key = cell.text
            else:
                #enter key, value info into the dictionary on even iteratons
                stock_dictionary[key] = cell.text
            #increment counter
            counter += 1
        #append stock dictionary to the list of dictionaries
        list_of_stock_dictionaries.append(stock_dictionary)

    export_data(list_of_stock_dictionaries)

main()