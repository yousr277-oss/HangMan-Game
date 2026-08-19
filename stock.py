# 1. dictionery to store stock data
stock_data = {
    "AAPL": 250,
    "GOOGL": 1800,
    "MSFT": 300,
    "AMZN": 3300,
    "TSLA": 700,
    "NVDA": 500,
    "DOW JONES": 860
}

print ("Welcome\n Happy to assist you \n How can I help you?")

# 2. user input to get stock symbol
stock_symbol = input("Enter the stock symbol(e.g., AAPL): ").upper()
if stock_symbol in stock_data:
    quantity = int(input("Enter the quantity of shares: "))
    # 3. calculate total value of the stock
    price = stock_data[stock_symbol]
    total_value = quantity * price
    print(f"Total value of {quantity} shares of {stock_symbol}: ${total_value}")

print ("Come Back Soon!")
    #save the stock data to a txt file
    with open("stock_data.txt", "a") as file:
      file.write(f"{stock_symbol}: {quantity} shares at ${price} each, Total Value: ${total_value}\n")
    print("Stock data saved to stock_data.txt")
else:
    print("Stock symbol not found in the data.")
