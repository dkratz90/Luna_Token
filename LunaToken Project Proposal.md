# **Project Title:** **LunaToken**: A Decentralized Token Creation and Distribution System with Real-Time Value Tracking

### ** Project Contributors:
### David Kratzer, Elizabeth Ogando, Chadwick Sanon, Yousef Sersy

#### **Project Overview:**
The goal of this project is to create a decentralized token on the Ethereum blockchain, named "LunaToken," using the ERC-20 token standard. The project will not only focus on the creation and distribution of LunaToken but also include functionality to track its value against popular cryptocurrencies like ETH. This will provide participants with real-time insights into the worth of their holdings.

#### **Objectives:**
1. **Token Creation:** Develop and deploy a custom ERC-20 token named LunaToken.
2. **Token Distribution:** Implement a distribution mechanism where LunaTokens can be sent to users' wallets.
3. **Value Tracking:** Integrate functionality to track and display the value of LunaToken in ETH.
4. **User Interface:** Develop a simple web-based interface for users to view their LunaToken balance and its current value.
5. **Documentation:** Provide detailed documentation for the token creation, distribution process, and value tracking system.

#### **Scope of Work:**

1. **Token Development:**
   - **Token Name:** LunaToken
   - **Token Symbol:** LUNA
   - **Decimals:** 18 (standard for ERC-20 tokens)
   - **Total Supply:** 1,000,000 LUNA
   - **Smart Contract Development:** Write a smart contract in Solidity to define LunaToken's properties, including minting functions.

2. **Distribution Mechanism:**
   - **Airdrop Functionality:** Develop a function within the smart contract that allows the owner to airdrop LunaTokens to specified Ethereum addresses.


3. **Value Tracking:**
   - **Price Oracle Integration:** Use a Chainlink oracle to fetch real-time price data for ETH/USD and LunaToken/ETH pairs.
   - **Conversion Functionality:** Implement a feature in the smart contract to convert LunaToken balances to their equivalent value in ETH and USD.
   - **Display Value:** Develop a front-end component that fetches and displays the current LunaToken value.

4. **User Interface Development:**
   - **Wallet Connection:** Integrate Metamask for users to connect their Ethereum wallet.
   - **Dashboard:** Create a dashboard showing the user’s LunaToken balance, current LunaToken value in ETH and USD, and recent transactions.
   - **Transaction History:** Display a list of recent LunaToken transfers involving the user.

5. **Testing and Deployment:**
   - **Unit Testing:** Perform extensive unit testing of the smart contract using Ganache.
   - **Testing Deployment:** Deploy the contract on Remix IDE for testing purposes.

#### **Technologies and Tools:**
- **Solidity**: The programming language used for writing the smart contract.
- **OpenZeppelin Contracts**: A library of secure and reusable smart contracts.
  - `ERC20`: Standard interface for fungible tokens.
  - `ERC20Detailed`: Provides additional metadata for the token (name, symbol, decimals).
  - `ERC20Mintable`: Allows minting of new tokens.
- **Ethereum**: The blockchain network for deploying the LunaToken contract.
- **Remix IDE**: An integrated development environment for writing, compiling, and deploying Solidity smart contracts.
- **Ganache**: A personal Ethereum blockchain used for development, testing, and deployment.
- **Web3.js**: A JavaScript library to interact with the Ethereum blockchain from the front end (optional).

#### **Expected Outcomes:**
- A fully functional ERC-20 token (LunaToken) deployed on the Ethereum blockchain.
- A decentralized system for distributing and tracking the value of LunaToken.
- A user-friendly interface allowing users to view their token balance and its real-time value in ETH.


#### **Conclusion:**
The LunaToken smart contract aims to provide a versatile and efficient token with dynamic pricing and easy distribution mechanisms. This project will serve as a foundational example for integrating real-time data into token economics and optimizing token distribution strategies.
