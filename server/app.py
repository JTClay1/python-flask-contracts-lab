#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

# mock contract data the tests will look through
contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

# list of known customers (lowercase on purpose)
customers = ["bob", "bill", "john", "sarah"]

# initialize the Flask app
app = Flask(__name__)

# only run the server if this file is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.get("/contract/<int:id>")
def get_contract(id):
    # look for a contract with a matching id
    contract = next((c for c in contracts if c["id"] == id), None)

    # if no contract exists, return a 404
    if contract is None:
        return "", 404

    # return the contract info as plain text with a 200 status
    return contract["contract_information"], 200


@app.get("/customer/<customer_name>")
def get_customer(customer_name):
    # check if the customer exists in the list
    if customer_name in customers:
        # customer exists but data is sensitive, so return no content
        return "", 204

    # customer not found
    return "", 404
