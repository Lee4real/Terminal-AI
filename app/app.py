from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import InMemoryHistory
from rich.console import Console

# Initialize the console
console = Console()

# Command completer with a list of commands
command_completer = WordCompleter(['help', 'exit', 'list', 'show'], ignore_case=True)

def main():
    history = InMemoryHistory()

    while True:
        try:
            # Read user input with autocompletion
            user_input = prompt('> ', completer=command_completer, history=history)

            # Handle commands
            if user_input == 'exit':
                break
            elif user_input == 'help':
                console.print("Available commands: help, exit, list, show")
            elif user_input == 'list':
                console.print("Listing items...")
            elif user_input == 'show':
                console.print("Showing details...")
            else:
                console.print(f"Unknown command: {user_input}")

        except (KeyboardInterrupt, EOFError):
            console.print("\nExiting...")
            break

if __name__ == "__main__":
    main()
