import os
import yfinance as yf
import flask
from flask import request, jsonify
from time import time, sleep
from datetime import datetime

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
@app.route('/', methods=['GET'])
def home():
    return "Hello!"


#Examples: MXRF11.SA;AAPL;ITSA4.SA;VTI; BTC-USD
@app.route('/api/v1/resources/ticker', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    teste = 1234567890123456789

    if 'ticker' in request.args:
        ticker = request.args['ticker']
    else:
        return "Error: No ticker provided. Please specify an ticker."

    # Create an empty list for our results
    results = []
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_quote = (data.tail(1)['Close'].iloc[0])
    print(ticker, last_quote)
    # results.append(last_quote)
    # print(jsonify(results))
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    # for book in books:
    #     if book['id'] == id:
    #         results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(last=last_quote)


@app.route('/api/v1/resources/tickerEveryTime', methods=['GET'])
def api_id2():

    if 'ticker' in request.args:
        ticker = request.args['ticker']
    else:
        return "Error: No ticker provided. Please specify an ticker."

    while True:
        sleep(60 - time() % 60)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        ticker_yahoo = yf.Ticker(ticker)
        data = ticker_yahoo.history()
        last_quote = (data.tail(1)['Close'].iloc[0])
        print(dt_string, " ->", ticker,"|", last_quote)


    return jsonify(last=last_quote)

# app.run()

#teste localhost
'''if __name__ == '__main__':
    app.run(debug=True)'''

#teste heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)