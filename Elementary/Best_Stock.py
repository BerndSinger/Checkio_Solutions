'''
You are given the current stock prices in a dictonary. The key is the name of the stock
the value is the price of the stock
Your program should return the price and name of the highest stock in the dictonary

'''
stock1 = {'CAC': 10.0, 'ATX': 390.2, 'WIG': 1.2}
stock2 = {'CAC': 91.1, 'ATX': 1.01, 'TASI': 120.9}

def best_market_price(stock):
   # Initializing the max_price and storing it later in the variable answer
    max_price=0
    answer=''

    # looping through the dictonary and checking if the current price is higher than
    # the last one you checked
    # Storing the name of the highest stock in the variable
    for s in stock:
        if stock[s] > max_price:
            max_price= stock[s]
            indexNumber=s
        answer= max_price
        name = indexNumber

    # Ausgabe von Wert der Aktie und Name der Aktie
    return (answer,name)


print(best_market_price(stock1))
