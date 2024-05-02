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

    /// @notice Test the increment functionality symbolically
    /// @dev Checks that incrementing the counter updates the number correctly
    function check_increment() public {
        uint256 initialNumber = counter.number();
        counter.increment();
        uint256 incrementedNumber = counter.number();
        assertEq(incrementedNumber, initialNumber + 1, "Increment did not increase the number by 1");
    }

    /// @notice Symbolically test setting the counter number
    /// @dev Checks that the number is set correctly
    function check_setNumber(uint256 x) public {
        counter.setNumber(x);
        assertEq(counter.number(), x, "Number was not set correctly");
    }

    /// @notice Ensure that the number does not overflow on increment
    /// @dev Checks for overflow conditions
    function check_noOverflow() public {
        counter.setNumber(type(uint256).max);
        counter.increment();
        uint256 incrementedNumber = counter.number();
        assertEq(incrementedNumber, 0, "Overflow should wrap around to zero");
    }
}
