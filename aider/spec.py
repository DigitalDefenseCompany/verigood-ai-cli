import os
from pathlib import Path

from aider.coders import spec_prompts
from aider import utils
from aider.sendchat import simple_send_with_retries


class Spec:
    def __init__(self, io, models, abs_fnames, coder, verbose_logging):
        self.io = io
        self.models = models
        self.abs_fnames = list(abs_fnames)  # Convert abs_fnames to a list
        self.coder = coder
        self.cur_messages = []
        self.done_messages = []
        self.partial_response_content = ""
        self.partial_response_function_call = dict()
        self.fence = spec_prompts.fence
        self.verbose_logging = verbose_logging

    def run(self, context):
        try:
            spec_response = self.generate_spec(context)
            if not spec_response:
                return
            if self.verbose_logging:
                self.io.tool_output("Response:")
                self.io.tool_output(spec_response)

            self.apply_updates(spec_response)

        except KeyboardInterrupt:
            self.io.tool_error("\n\n^C KeyboardInterrupt")
            return

    def generate_spec(self, context):
        self.io.tool_output("Generating Halmos specification...")
        content = ""
        if context:
            content += context + "\n"
        content += self.get_foundry_files_content()

        self.cur_messages += [dict(role="user", content=content)]
        messages = self.format_messages()

        if self.verbose_logging:
            self.io.tool_output("Messages:")
            utils.show_messages(messages)

        self.io.tool_output("Sending code and context to the language model...")

        spec_response = simple_send_with_retries(self.models[0].name, messages)
        if not spec_response:
            self.io.tool_error("Failed to generate Halmos specification!")
            return

        self.done_messages += self.cur_messages
        self.cur_messages = []

        return spec_response

    def format_messages(self):
        main_sys = self.fmt_system_prompt(spec_prompts.spec_system)
        main_sys += "\n" + self.fmt_system_prompt(spec_prompts.spec_reminder)

        messages = [dict(role="system", content=main_sys)]
        messages += self.done_messages
        messages += self.cur_messages

        return messages

    def apply_updates(self, content):
        self.coder.partial_response_content = content
        edits = self.coder.get_edits()

        # Convert foundry_path to string
        foundry_path_str = str(self.coder.foundry_path)

        filtered_edits = []
        for edit in edits:
            filtered_edits.append(edit)

        if not filtered_edits:
            self.io.tool_error("No valid edits found in the generated diff.")
            return

        spec_file = self.coder.get_edits()[0][0]

        # Read the existing content of the spec file
        existing_content = ""
        if spec_file and os.path.exists(spec_file):
            with open(spec_file, "r") as f:
                existing_content = f.read()

        # Check if the generated content already exists in the spec file
        if content.strip() in existing_content.strip():
            self.io.tool_output(
                "Halmos specification already exists in the file. No changes made."
            )
            return

        # Apply the edits
        self.coder.apply_edits(filtered_edits)

        # Add the spec file to self.abs_fnames
        if spec_file:
            spec_file_abs_path = str(spec_file)
            if spec_file_abs_path not in self.abs_fnames:
                self.abs_fnames.append(spec_file_abs_path)
                self.io.tool_output(f"Added {spec_file} to the LLM context.")

        self.io.tool_output("Halmos specification generated and applied successfully!")

    def get_foundry_files_content(self):
        foundry_files = self.get_foundry_files()
        if not foundry_files:
            return ""

        content = "Foundry files:\n"
        for file in foundry_files:
            with open(file, "r") as f:
                file_content = f.read()
            content += f"\n{file}\n{self.fence[0]}\n{file_content}\n{self.fence[1]}\n"

        return content

    def get_foundry_files(self):
        return [
            str(file)
            for file in self.abs_fnames
            if "lib" not in str(file)
            and str(file).endswith(".sol")
        ]

    def fmt_system_prompt(self, prompt):
        prompt = prompt.format(fence=self.fence)
        return prompt
