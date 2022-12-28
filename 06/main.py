import json
import requests
from flask import Flask, request

from blockchain import Blockchain


app = Flask(__name__)
blockchain = Blockchain()

# curl  http://127.0.0.1:5000/chain
@app.route("/chain", methods=["GET"])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data), "chain": chain_data})

# curl  http://127.0.0.1:5000/add_transaction?transaction=some_transaction
@app.route("/add_transaction")
def add_transaction():
    transaction = request.args.get("transaction")
    blockchain.add_new_transaction(transaction)
    return "Transaction added"

# curl  http://127.0.0.1:5000/mine
@app.route("/mine")
def mine():
    blockchain.mine()
    return "all transactions are mined"


app.run(debug=True, port=5000)