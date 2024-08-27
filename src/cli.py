import sys
from autocomplete import autocomplete_command
from suggestions import suggest_commands
from explanations import get_command_explanations

def run_cli():
    print("Enter 'autocomplete', 'suggest', 'explain' or 'exit' to quit.")
    while True:
        user_input = input("> ")

        if user_input.startswith("autocomplete"):
            command_part = user_input.split(" ", 1)[1]
            suggestion = autocomplete_command(command_part)
            print(f"--> : {suggestion}")

        elif user_input.startswith("suggest"):
            command_part = user_input.split(" ", 1)[1]
            suggestions = suggest_commands(command_part)
            print("--> :")
            for suggestion in suggestions:
                print(suggestion)

        elif user_input.startswith("explain"):
            command_part = user_input.split(" ", 1)[1]
            explanation = get_command_explanations(command_part)
            print("--> :")
            print(explanation)
        elif user_input.lower() in ["exit", "quit"]:
            sys.exit(0)
        else:
            print("Unknown command. Try 'autocomplete', 'suggest', 'explain', or 'exit'.")

