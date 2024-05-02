# VeriGood.ai : AI-Assisted Formal Verification for Smart Contracts

This project, powered by VeriGood.ai, aims to leverage the power of AI and Large Language Models (LLMs) to support formal verification of smart contracts. By integrating AI capabilities into the formal verification process, we can enhance the efficiency and effectiveness of verifying the correctness and security of smart contracts.

![Demo GIF](assets/verigood-ai-demo.gif)

## Overview

Formal verification is a critical technique for ensuring the correctness and security of smart contracts. However, writing formal specifications and conducting thorough verification can be time-consuming and require specialized expertise. This project, powered by VeriGood.ai, addresses these challenges by harnessing the capabilities of AI and LLMs to assist in the formal verification process.

## Features

- 🧠 **AI-Assisted Specification Generation**: Utilize AI models to automatically generate formal specifications based on smart contract code and user requirements. The AI models are trained on a vast corpus of smart contract code and formal verification techniques to produce high-quality specifications.

- 🌟 **Intelligent Verification Guidance**: Leverage LLMs to provide intelligent guidance and suggestions throughout the formal verification process. The LLMs can analyze the smart contract code, identify potential vulnerabilities, and offer recommendations for verifying specific properties.

- 🔧 **Seamless Integration with Halmos**: Seamlessly integrate with the Halmos library, a symbolic testing tool for EVM smart contracts. Halmos allows writing property-based tests in Solidity and uses symbolic execution to verify the properties for all possible input combinations.

- 🎯 **Comprehensive Verification Coverage**: Generate comprehensive test cases and verification scenarios using AI techniques. The AI models can explore various input spaces, consider edge cases, and generate targeted tests to achieve high verification coverage.

- 💻 **Intuitive User Interface**: Provide an intuitive and user-friendly interface for interacting with the AI-assisted formal verification system. Users can input their smart contract code, specify requirements, and receive automated specifications and verification results.

## Getting Started

To get started with AI-assisted formal verification for smart contracts with VeriGood.ai, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-formal-verification.git
  ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   verigood --foundry [PATH_TO_FOUNDRY_PROJECT]
  ```

Follow the prompts and instructions provided by the tool to generate formal specifications and perform verification.

Once in the application, you can generate the specifications for your smart contract by running the following command:

```bash
/spec [--verbose]
```

You can then proceed to verify the smart contract using the generated specifications:

```bash
/verify [--verbose]
```

## Examples

Here are a few examples demonstrating the capabilities of AI-assisted formal verification with VeriGood.ai:

- **Simple Token Contract**: Verify the correctness of a basic token contract using AI-generated specifications and Halmos.
- **Crowdsale Contract**: Utilize AI guidance to identify potential vulnerabilities and verify the security properties of a crowdsale contract.
- **Voting Contract**: Generate comprehensive test cases using AI techniques to achieve high verification coverage for a voting contract.

## Contributing

Contributions to this project are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Make sure to follow the contribution guidelines outlined in `CONTRIBUTING.md`.

## Acknowledgements

We would like to express our gratitude to the following projects and resources that have inspired and supported the development of this AI-assisted formal verification tool:

- [Aider](https://github.com/paul-gauthier/aider): Aider is an AI pair programming tool that has served as a foundation for scaffolding this project. We appreciate the work done by Paul Gauthier and the Aider community in creating an intuitive and efficient AI coding assistant.

- [Halmos](https://github.com/a16z/halmos): Halmos is a symbolic testing library for EVM smart contracts that enables writing property-based tests in Solidity. We are grateful for the Halmos team's efforts in developing this powerful verification tool.

- [OpenAI](https://openai.com/) and [Anthropic](https://www.anthropic.com/): We acknowledge the contributions of OpenAI and Anthropic in advancing the field of artificial intelligence and providing state-of-the-art language models that power the AI capabilities of this project.