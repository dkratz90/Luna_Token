### **Project Title:**  
**LunaToken**: A Decentralized Token Creation and Distribution System with Real-Time Value Tracking

#### ** Project Contributors:
#### David Kratzer, Elizabeth Ogando, Chadwick Sanon, Yousef Sersey

#### **Project Overview:**
The goal of this project is to create a decentralized token on the Ethereum blockchain, named "LunaToken," using the ERC-20 token standard. The project will not only focus on the creation and distribution of LunaToken but also include functionality to track its value against popular cryptocurrencies like ETH and USD. This will provide participants with real-time insights into the worth of their holdings.

#### **Objectives:**
1. **Token Creation:** Develop and deploy a custom ERC-20 token named LunaToken.
2. **Token Distribution:** Implement a distribution mechanism where LunaTokens can be sent to users' wallets.
3. **Value Tracking:** Integrate functionality to track and display the value of LunaToken in ETH and USD.
4. **User Interface:** Develop a simple web-based interface for users to view their LunaToken balance and its current value.
5. **Documentation:** Provide detailed documentation for the token creation, distribution process, and value tracking system.

#### **Scope of Work:**

1. **Token Development:**
   - **Token Name:** LunaToken
   - **Token Symbol:** LUNA
   - **Decimals:** 18 (standard for ERC-20 tokens)
   - **Total Supply:** 1,000,000 LUNA
   - **Smart Contract Development:** Write a smart contract in Solidity to define LunaToken's properties, including minting and burning functions.

2. **Distribution Mechanism:**
   - **Airdrop Functionality:** Develop a function within the smart contract that allows the owner to airdrop LunaTokens to specified Ethereum addresses.
   - **Manual Transfer:** Enable manual token transfer between user accounts via web3.js.

3. **Value Tracking:**
   - **Price Oracle Integration:** Use a Chainlink oracle to fetch real-time price data for ETH/USD and LunaToken/ETH pairs.
   - **Conversion Functionality:** Implement a feature in the smart contract to convert LunaToken balances to their equivalent value in ETH and USD.
   - **Display Value:** Develop a front-end component that fetches and displays the current LunaToken value.

4. **User Interface Development:**
   - **Wallet Connection:** Integrate Metamask for users to connect their Ethereum wallet.
   - **Dashboard:** Create a dashboard showing the user’s LunaToken balance, current LunaToken value in ETH and USD, and recent transactions.
   - **Transaction History:** Display a list of recent LunaToken transfers involving the user.

5. **Testing and Deployment:**
   - **Unit Testing:** Perform extensive unit testing of the smart contract using Truffle.
   - **Testnet Deployment:** Deploy the contract on the Ropsten or Goerli testnet for testing purposes.
   - **Mainnet Deployment:** After successful testing, deploy LunaToken on the Ethereum mainnet.

6. **Documentation:**
   - **Technical Documentation:** Provide a detailed guide on how the LunaToken smart contract works, how to interact with it, and how the value tracking system operates.
   - **User Guide:** Offer a simple user guide for interacting with the LunaToken interface, including wallet connection and token transfer.

#### **Technologies and Tools:**
- **Blockchain:** Ethereum
- **Smart Contract Language:** Solidity
- **Development Framework:** Ganache
- **Front-End:** React.js, web3.js
- **Wallet Integration:** Metamask
- **Testing:** Ganache
- **Deployment:** Remix IDE

#### **Team Roles:**
- **Smart Contract Developer:** Writes the LunaToken smart contract and handles deployment.
- **Front-End Developer:** Develops the user interface for the dashboard.
- **Quality Assurance:** Tests the system for bugs and issues before deployment.

#### **Expected Outcomes:**
- A fully functional ERC-20 token (LunaToken) deployed on the Ethereum blockchain.
- A decentralized system for distributing and tracking the value of LunaToken.
- A user-friendly interface allowing users to view their token balance and its real-time value in ETH and USD.
- Comprehensive documentation to support future development and user interaction.

#### **Budget:**
- **Development Costs:** Estimate based on team rates.
- **Deployment Costs:** Gas fees for deploying on the Ethereum mainnet.
- **Miscellaneous:** Costs for hosting the front-end interface and other operational expenses.

#### **Conclusion:**
This project will provide valuable hands-on experience with token creation, smart contract development, and blockchain integration. It’s a practical project that showcases the ability to create and manage a decentralized token system, making it an excellent addition to any blockchain portfolio.