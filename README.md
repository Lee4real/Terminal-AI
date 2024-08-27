# AI-Powered Terminal

This project is a command-line interface (CLI) tool that uses AI to autocomplete, suggest, and explain Linux/macOS commands.

## Features

- **Autocomplete**: Complete partial commands.
- **Suggest**: Provide a list of possible commands based on partial input.
- **Explain**: Explain what a given command does.

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/lee4real/ai-terminal.git
   cd ai-terminal
   python -m unittest discover
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a .env file in the project root.

   - Add your Gemini API key to the .env file:

   ```sh
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the CLI:

```sh
python main.py
```

## Testing

Run unit test:

```sh
python -m unittest discover
```

## License

This project is licensed under the MIT License.
