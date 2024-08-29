// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

contract LunaToken is ERC20, ERC20Detailed, ERC20Mintable {
    uint256 private ethPriceInUSD; // Price of ETH in USD

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    )
        ERC20Detailed(name, symbol, 18) // Pass parameters to ERC20Detailed
        public
    {
        _mint(msg.sender, initialSupply);
    }

    // Function to set the ETH price in USD
    function setEthPriceInUSD(uint256 _price) public {
        ethPriceInUSD = _price;
    }

    // Function to get the ETH price in USD
    function getLatestPrice() public view returns (uint256) {
        return ethPriceInUSD;
    }

    // Function to get the value of 1 LUNA in ETH
    function getLunaValueInETH() public view returns (uint256) {
    uint256 ethPrice = getLatestPrice(); // Price of ETH in USD
    require(ethPrice > 0, "Invalid ETH price");

    uint256 lunaPriceInUSD = 1e18; // 1 LUNA = $1 (represented with 18 decimals)

    // Calculate the price of 1 LUNA in Wei (smallest unit of ETH)
    uint256 lunaValueInWei = (lunaPriceInUSD * 1e18) / ethPrice;

    // Convert Wei to ETH by dividing by 1e18
    uint256 lunaValueInETH = lunaValueInWei / 1e18;

    return lunaValueInETH;
}

    // Function to airdrop LUNA tokens
    function airdrop(address[] memory recipients, uint256 amount) public {
        for (uint256 i = 0; i < recipients.length; i++) {
            _transfer(msg.sender, recipients[i], amount); // Use msg.sender as the source of tokens
        }
    }
}
