import click
import struct
import subprocess
import utils
from decouple import config

seed_phrase = config("seed_phrase")
buyer = config("bob_address")
seller = config("alice_address")
value_to_contract = "0"
gas = "1000000000000"
default_rate = "0c" # 0x0c in hexadecimal is 12 in decimal
function_ids = {
	"get_trade":"0x52bd11c0",
	"store_trade":"0x8fce8545"
}
value = "0000c16ff28623000000000000000000"



@click.group()
def main():
	pass

@main.command()
@click.argument('account')
def balance(account):
	'''
	A function to get an account's balance. 

    Parameters:
    account (str): account queried for balance, e.g. 5FLEkQLanHeoQPJXzuxT3eVBRh8A5rBvb5sMajfJeV8EJyXT

    Returns:
    json: a dictionary of the accounts balances. 
	'''
	query_balance = subprocess.run(["polkadot-js-api", "query.system.account", "{}".format(account)])
	click.echo('Exit code {}'.format(query_balance.returncode))

@main.command()
@click.argument('contract_address')
@click.argument('trade_id')
def store_trade(contract_address, trade_id, buyer=buyer, seller=seller, seed_phrase=seed_phrase, 
	value_to_contract=value_to_contract, gas=gas, fid=function_ids["store_trade"], rate=default_rate):
	'''
	A function to call the dummy ERC20 contract and store a trade. 

    Parameters:
    contract_address (str): address of the deployed contract, 
    	e.g. 5DvtpRYA3hWCwhW3NrrVJCNZinYgSy4W2Sgg38SYkv62LUpQ
	trade_id (str): a number between 00 and 63 representing a trade ID in hex (e.g. 10 = 0a).
	seed_phrase (str): a string of 12 words to restore a Polkadot account. 
	value_to_contract (str): the value sent to the contract within this transaction (0 in this case).
	gas (str): the maximum allowed gas for this transaction. 
	fid (str): the hex representation of the function, generated in the metadata. 

	'''
	buyer_addr = utils.address_to_hex(buyer)
	seller_addr = utils.address_to_hex(seller)
	store_trades = subprocess.run(["polkadot-js-api", 
		"--seed", 
		"\""+seed_phrase+"\"",
		"tx.contracts.call", 
		"{}".format(contract_address), 
		value_to_contract, 
		gas,
		fid  + "{}".format(trade_id) + "{}".format(buyer_addr) + "{}".format(seller_addr) + \
		"{}".format(value)  + "{}".format(rate) ])

@main.command()
@click.argument('contract_address')
@click.argument('trade_id')
def get_trade(contract_address, trade_id, seed_phrase=seed_phrase, value_to_contract=value_to_contract, 
	gas=gas, fid=function_ids["get_trade"]):
	'''
	A function to call the dummy ERC20 contract and retrieve an executed trade by its id. 

    Parameters:
    contract_address (str): address of the deployed contract, 
    	e.g. 5DvtpRYA3hWCwhW3NrrVJCNZinYgSy4W2Sgg38SYkv62LUpQ
	trade_id (str): a number between 00 and 63 representing a trade ID. Has to consist of 2 digits. 
	seed_phrase (str): a string of 12 words to restore a Polkadot account. 
	value_to_contract (str): the value sent to the contract within this transaction (0 in this case).
	gas (str): the maximum allowed gas for this transaction. 
	fid (str): the hex representation of the function, generated in the metadata. 

	'''

	query_storage = subprocess.run(["polkadot-js-api", 
		"--seed",
		"\""+seed_phrase+"\"",
		"tx.contracts.call", 
		"{}".format(contract_address), 
		value_to_contract, 
		gas, 
		fid + "{}".format(trade_id)])

