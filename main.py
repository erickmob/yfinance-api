import yfinance as yf
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
@app.route('/', methods=['GET'])
def home():
    return "Hello!"

@app.route('/api/v1/resources/ticker', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
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

app.run()
