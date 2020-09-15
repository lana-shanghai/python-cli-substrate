# A python CLI to interact with an ink Smart Contract 


Ensure that you have the Polkadot Chrome extension. Create an account and save your seed phrase. 
You will need to pass "your twelve words" as a parameter. 

Build the [substrate-node-template](https://github.com/substrate-developer-hub/substrate-node-template) and run the node with 
```
substrate --dev
```

Go to Polkadot [explorer](https://polkadot.js.org/apps/#/explorer) where you should see updating blocks if everything is fine. 

Go to Developer -> Contracts -> Upload Wasm. 
From the dummy_erc20/target folder, upload the erc20.wasm file as the contract, and the metadata.json file as the contract ABI. After uploading, click "Deploy". Make sure to give it an initial total_supply. 
Save the contract address as it will be needed to call the contract. 

Check that everything deployed by going to Contract -> Developer -> Instance -> Messages and call the total_supply() function as an RPC call. 

Have the polkadot-js-api installed locally with 
```
yarn add @polkadot/api
yarn global add @polkadot/api-cli
```

Check that it works with 
```
polkadot-js-api query.timestamp.now
```

CD into the storage_cli directory and add your seed phrase.
The buyer and seller addresses are Alice and Bob's hex addresses. 

activate the environment with 
```
python -m venv env
source env/bin/activate
```

In there, install Click by running  
```
python -m pip install .
```

## Available commands: 

```
storage balance 5FLEkQLanHeoQPJXzuxT3eVBRh8A5rBvb5sMajfJeV8EJyXT 
storage store-trade 5DvtpRYA3hWCwhW3NrrVJCNZinYgSy4W2Sgg38SYkv62LUpQ 0b
storage get-trade 5DvtpRYA3hWCwhW3NrrVJCNZinYgSy4W2Sgg38SYkv62LUpQ 0b
```

Above the address for storing and getting a trade is the contract address. 

## TODO: 

Tools to convert between Polkadot address and hex address, values and hexes, proper data load functions, constants etc. 