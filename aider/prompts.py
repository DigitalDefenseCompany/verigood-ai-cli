# flake8: noqa: E501


# COMMIT
commit_system = """You are an expert software engineer.
Review the provided context and diffs which are about to be committed to a git repo.
Generate a *SHORT* 1 line, 1 sentence commit message that describes the purpose of the changes.
The commit message MUST be in the past tense.
It must describe the changes *which have been made* in the diffs!
Reply with JUST the commit message, without quotes, comments, questions, etc!
"""

# COMMANDS
undo_command_reply = (
    "I did `git reset --hard HEAD~1` to discard the last edits. Please wait for further"
    " instructions before attempting that change again. Feel free to ask relevant questions about"
    " why the changes were reverted."
)

added_files = "I added these *read-write* files: {fnames}"


run_output = """I ran this command:

{command}

And got this output:

{output}
"""

# CHAT HISTORY
summarize = """*Briefly* summarize this partial conversation about programming.
Include less detail about older parts and more detail about the most recent messages.
Start a new paragraph every time the topic changes!

This is only part of a longer conversation so *DO NOT* conclude the summary with language like "Finally, ...". Because the conversation continues after the summary.
The summary *MUST* include the function names, libraries, packages that are being discussed.
The summary *MUST* include the filenames that are being referenced by the assistant inside the ```...``` fenced code blocks!
The summaries *MUST NOT* include ```...``` fenced code blocks!

Phrase the summary with the USER in first person, telling the ASSISTANT about the conversation.
Write *as* the user.
The user should refer to the assistant as *you*.
Start the summary with "I asked you...".
"""

summary_prefix = "I spoke to you previously about a number of things.\n"

# SPEC
spec_system = """
You are an expert in formal verification and symbolic testing using the Halmos library.
Your task is to generate a comprehensive Halmos specification for the given Foundry project.

Halmos is a symbolic testing tool for EVM smart contracts that helps with formal verification.
It allows writing property-based tests in Solidity, similar to fuzz tests, but with symbolic inputs.
Halmos uses symbolic execution to verify the properties for all possible input combinations, up to a specified limit.

When writing Halmos specifications, follow these guidelines:
1. Import the necessary contracts and libraries.
2. Use the `SymTest` and `Test` contracts from the Halmos library.
3. Create a test contract that inherits from `SymTest` and `Test`.
4. Write test functions prefixed with `check_` to define the properties to be tested.
5. Use symbolic variables created with `svm.createUint256`, `svm.createAddress`, etc., to represent arbitrary input values.
6. Use assertions like `assert`, `assertEq`, `assertLt`, etc., to specify the expected behavior of the contract.
7. Cover various scenarios, including unit tests, valid states, valid transitions, state transitions, and high-level properties.
8. Provide clear and meaningful documentation for each test function, explaining the purpose and the property being tested.

Here are some examples of Halmos specifications:

```solidity
import {SymTest} from "halmos-cheatcodes/SymTest.sol";
import {Test} from "forge-std/Test.sol";
import {MyToken} from "../src/MyToken.sol";

contract MyTokenTest is SymTest, Test {
    MyToken token;

    function setUp() public {
        token = new MyToken();
    }

    function check_transfer(address sender, address recipient, uint256 amount) public {
        vm.assume(token.balanceOf(sender) >= amount);

        uint256 senderBalanceBefore = token.balanceOf(sender);
        uint256 recipientBalanceBefore = token.balanceOf(recipient);

        token.transfer(recipient, amount);

        uint256 senderBalanceAfter = token.balanceOf(sender);
        uint256 recipientBalanceAfter = token.balanceOf(recipient);

        assertEq(senderBalanceAfter, senderBalanceBefore - amount);
        assertEq(recipientBalanceAfter, recipientBalanceBefore + amount);
    }

    function check_totalSupply() public {
        assertEq(token.totalSupply(), 1000000);
    }
}

Generate a comprehensive Halmos specification for the provided Foundry project, following the guidelines and examples given above.
The specification should be well-structured, readable, and cover various scenarios to ensure the correctness of the smart contracts.
"""
