// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test} from "forge-std/Test.sol";
contract MyContract is Test {
  mapping (address => uint) balances;
  function prove_single_fail(address recv, uint amt) public {
    require(balances[recv] < 100);
    if (balances[recv] + amt >= 100) { revert(); }
    balances[recv] += amt;
    assert(balances[recv] < 100);
  }
}