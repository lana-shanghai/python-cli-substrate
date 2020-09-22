import base58

def address_to_hex(address):
	try:
		hex_address = base58.b58decode(address).hex()[2:-4]
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise

