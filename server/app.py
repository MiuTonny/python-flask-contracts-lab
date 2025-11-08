#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response, jsonify

app = Flask(__name__)

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},
             {"id": 2, "contract_information": "This contract is for a deck for a business"},
             {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]

customers = ["bob","bill","john","sarah"]


#default
@app.route('/')
def index():
    return "Welcome to the Contracts API!"

#route to list all customers
@app.get("/customers")
def customers_index():
    return jsonify(customers)
#route to list all contracts
@app.get("/contracts")
def contracts_index():
    return jsonify(contracts)

#route to get contract by id
@app.get("/contract/<int:contract_id>")
def contract_info(contract_id):
    for contract in contracts:
        if contract["id"] == contract_id:
           #contract found, give info
           return contract["contract_information"], 200
    return "Contract not found", 404

#route to get customer by name
@app.get("/customer/<customer_name>")
def customer_info(customer_name: str):
    if customer_name.lower() in (name.lower() for name in customers):
        return "", 204
    else:
        return jsonify({"error": "Customer not found"}), 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)

    
