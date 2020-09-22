# A python CLI to interact with an ink Smart Contract 


Ensure that you have the Polkadot Chrome extension. Create an account and save your seed phrase. 
You will need to pass "your twelve words" as a parameter. 

Build the [substrate-node-template](https://github.com/substrate-developer-hub/substrate-node-template) and run the node with 
```
substrate --dev
```
The version we used was [v2.0.0-rc4](https://github.com/substrate-developer-hub/substrate-node-template/releases/tag/v2.0.0-rc4). 

Go to Polkadot [explorer](https://polkadot.js.org/apps/#/explorer) where you should see updating blocks if everything is fine. In the dropdown menu on the left connect to the local development node.

Install the cargo contract and create the wasm and metadata files with 
```
cargo install cargo-contract --force
cargo +nightly contract build
cargo +nightly contract generate-metadata
```

In accounts, send some funds to your account to be able to pay for fess and make transfers. Alice by default has 1M tokens. 

Go to Developer -> Contracts -> Upload Wasm. 
From the dummy_erc20/target folder, upload the erc20.wasm file as the contract, and the metadata.json file as the contract ABI. From the accounts menu, choose an address and send yourself some tokens (units) - you need those to pay fees. After uploading, click "Deploy". Make sure to give it an initial total_supply. 
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

In .env add your seed phrase.
The buyer and seller addresses are Alice and Bob's addresses from the default test accounts. 

activate the environment with 
```
python -m venv env
source env/bin/activate
```

In there, install Click by running  
```
python -m pip install .
```

## Available commands (replace the contract address with your deployed contract): 

```
storage balance 5FLEkQLanHeoQPJXzuxT3eVBRh8A5rBvb5sMajfJeV8EJyXT 
storage store-trade 5DvtpRYA3hWCwhW3NrrVJCNZinYgSy4W2Sgg38SYkv62LUpQ 0b
storage get-trade 5DvtpRYA3hWCwhW3NrrVJCNZinYgSy4W2Sgg38SYkv62LUpQ 0b
```

Above the address for storing and getting a trade is the contract address. 

## TODO: 

Tools to convert between Polkadot address and hex address, values and hexes, proper data load functions, constants etc. 