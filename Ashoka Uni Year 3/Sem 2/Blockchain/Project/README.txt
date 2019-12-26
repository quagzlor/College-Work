Code: https://github.com/quagzy/League_Eth/blob/master/README.md

I recommend using terminal for Unix systems, and Bash for Windows for Windows systems.

First, install the npm packages. Can be done with the command <sudo sudo npm install --save ethereumjs-wallet react react-bootstrap - react-dom react-scripts truffle truffle-contract truffle-hdwallet-provider web3> (The sudo sudo is so that you avoid a TON of issues)

You can deploy the contracts via the command <truffle migrate --network ropsten>
You can start the website via the command <npm start>
You need to have Metamask installed and setup, and with privacy mode off. If you see your wallet address displayed on the front-end page, it's working.

I recommend using Remix IDE to test the contract, due to issues with the front end. The contract is in the /contracts/ folder, named 'Betting.sol'