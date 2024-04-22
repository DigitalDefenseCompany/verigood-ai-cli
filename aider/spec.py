import os
from pathlib import Path

from aider import prompts
from aider.sendchat import simple_send_with_retries


class Spec:
    def __init__(self, io, models, abs_fnames):
        self.io = io
        self.models = models
        self.abs_fnames = list(abs_fnames)  # Convert abs_fnames to a list

    def generate_spec(self, context):
        self.io.tool_output("Generating Halmos specification...")

        content = ""
        if context:
            content += context + "\n"

        content += self.get_foundry_files_content()

        messages = [
            dict(role="system", content=prompts.spec_system),
            dict(role="user", content=content),
        ]

        self.io.tool_output("Sending code and context to the language model...")

        for model in self.models:
            spec = simple_send_with_retries(model.name, messages)
            if spec:
                break

        if not spec:
            self.io.tool_error("Failed to generate Halmos specification!")
            return

        self.io.tool_output("Saving the generated Halmos specification...")
        self.save_spec(spec)

        self.io.tool_output("Halmos specification generated successfully!")
        return spec

    def get_foundry_files_content(self):
        foundry_files = self.get_foundry_files()
        if not foundry_files:
            return ""

        content = "Foundry files:\n"
        for file in foundry_files:
            with open(file, "r") as f:
                file_content = f.read()
            content += f"\n{file}\n```solidity\n{file_content}\n```\n"

        return content

    def get_foundry_files(self):
        return [
            str(file)
            for file in self.abs_fnames
            if "lib" not in str(file)
            and "test" not in str(file)
            and str(file).endswith(".sol")
        ]

    def save_spec(self, spec):
        if not self.abs_fnames:
            self.io.tool_error("No Foundry files found to generate the specification.")
            return

        test_dir = Path(self.abs_fnames[0]).parent / "test"
        spec_file = test_dir / "Spec.t.sol"

        os.makedirs(
            test_dir, exist_ok=True
        )  # Create the test directory if it doesn't exist

        with open(spec_file, "w") as f:
            f.write(spec)
        self.io.tool_output(f"Saved Halmos specification to {spec_file}")
