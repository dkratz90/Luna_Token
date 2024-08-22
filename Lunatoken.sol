// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract LunaToken is ERC20, Ownable {
    // Chainlink Price Feed for ETH/USD
    AggregatorV3Interface internal priceFeed;

    // Constructor
    constructor(address _priceFeed) ERC20("LunaToken", "LUNA") Ownable(msg.sender) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        _mint(msg.sender, 1000000 * 10**decimals()); // Mint 1,000,000 LUNA to the contract owner
    }

    // Function to get the latest ETH/USD price from Chainlink
    function getLatestPrice() public view returns (int) {
        (
            , 
            int price, 
            , 
            , 
        ) = priceFeed.latestRoundData();
        return price;
    }

    // Function to get the value of LUNA in ETH
    function getLunaValueInETH() public view returns (uint) {
        // Assuming 1 LUNA = 1 LUNA / ETH price
        return 1e18 / uint(getLatestPrice());
    }

    // Function to get the value of LUNA in USD
    function getLunaValueInUSD() public view returns (uint) {
        uint ethPrice = uint(getLatestPrice());
        uint lunaPriceInETH = getLunaValueInETH();
        return lunaPriceInETH * ethPrice / 1e18;
    }

    // Function to airdrop LUNA tokens
    function airdrop(address[] memory recipients, uint amount) external onlyOwner {
        for (uint i = 0; i < recipients.length; i++) {
            _transfer(owner(), recipients[i], amount);
        }
    }
}
