// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {SymTest} from "halmos-cheatcodes/SymTest.sol";
import {Test} from "forge-std/Test.sol";
import {Counter} from "../src/Counter.sol";

/// @title Symbolic testing for the Counter contract
contract CounterSpecTest is SymTest, Test {
    Counter counter;

    function setUp() public {
        counter = new Counter();
        counter.setNumber(0);
    }

    /// @notice Test increment function with symbolic execution
    /// @dev Checks that incrementing the counter updates the number correctly
    function check_increment() public {
        uint256 initialNumber = svm.createUint256("initialNumber");
        vm.assume(initialNumber < type(uint256).max);

        counter.setNumber(initialNumber);
        counter.increment();

        assertEq(counter.number(), initialNumber + 1, "Increment does not update number correctly");
    }

    /// @notice Test setNumber function with symbolic execution
    /// @dev Checks that setting the number updates the state correctly
    function check_setNumber(uint256 newNumber) public {
        counter.setNumber(newNumber);
        assertEq(counter.number(), newNumber, "setNumber does not update number correctly");
    }
}
