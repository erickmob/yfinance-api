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

    if 'ticker' in request.args:
        ticker = request.args['ticker']
    else:
        return "Error: No ticker provided. Please specify an ticker."


    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_quote = (data.tail(1)['Close'].iloc[0])
    print(ticker, last_quote)
    response = jsonify(last=last_quote)
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


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