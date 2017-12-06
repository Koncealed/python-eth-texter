#I bought 2 ETH on Dec/4/2017 in the CSI Library. I wrote this script to keep me, and my father notified of the price. Losing the money is possiblity but if we do, we do. It's an experince.


import requests
import time
from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

def send_message(numbers, message): # Pass number as Array to add verified numbers
    for number in numbers:
        print('Sent to {}'.format(number))
        client.messages.create(to=number, from_=my_twilio, body=message)

def get_ethereum():
    return requests.get('https://api.coinbase.com/v2/prices/ETH-USD/spot').json()['data']

def get_start_data(e): #This function will take time to build on. This is due to me using Coinbase API. This does not include the 24 hour percentage. I work create a JSON documenting all the prices.
    return {
        'start_price': 466.61,  # Starting price in which I purchased
        'cumulative_percentage': round((float(e['amount']) / 466.61) * 100 - 100,2),    # Formula to get Cumlative Percentage change
        'cumulative_change': round(float(e['amount']) - 466.61, 2)  # Formula to get Cumulative Money change.
    }

def main():
    eth = get_ethereum()
    start_data = get_start_data(eth)
    send_message([my_cell], ' Good Morning. The price of Ethereum is valued at ' + eth['amount']
                 + 'We purchased ETH at $' + str(start_data['start_price']) + '. '
                 + ' Our Cumulative Percentage is currently at ' + str(start_data['cumulative_percentage']) + '%'
                 + ' Our Cumulative Value gained is currently at $' + str(start_data['cumulative_change']))
    seconds = 1
    minutes = 1  # The values need to start at one. In order for the. The timer to work properly do not change!
    hours = 1
    print("Value of ETH is $" + eth['amount'])
    while True:
        eth = get_ethereum()
        time.sleep(60)
        if minutes % 60 is 0:
            hours += 1
        if minutes % 360 is 0:
            send_message([my_cell], 'Hello, it has been 6 hours since the last update. '
                                    + 'ETH is currently valued at {}'.format(eth['amount']))
        if hours % 24 is 0:
            send_message([my_cell], ' Good Morning. The price of Ethereum is valued at ' + eth['amount']
                         + ' We purchased ETH at $' + str(start_data['start_price']) + '. '
                         + ' Our Cumulative Percentage is currently at %' + str(start_data['cumulative_percentage']) + '%'
                         + ' Our Cumulative Value gained is currently at $' + str(start_data['cumulative_change']))


if __name__ == '__main__':
   main()