from gemini_api import generate_text
import re

def autocomplete_command(command_part):
    command_part_with_prompt = f"""
    You are an expert in writing Linux/macOS commands. I will give you an incomplete command, 
    and your task is to complete it. Only return the exact completed command without any additional 
    words, details, explanations, or formatting like ``` or $ symbols. Just return the command itself.

    For example, if I give you 'git ch', you should return 'git checkout' without anything else.

    Here is the incomplete command: {command_part}
    """
    
    # Call the Gemini API to get autocomplete suggestions
    try:
        response = generate_text(command_part_with_prompt)
    except Exception as e:
        return f"Error: {e}"    
    
    # Use regex to find the first valid command
    # Assuming commands start with a word followed by a space and then options/arguments
    match = re.search(r"^[a-zA-Z]+\s+[\S]+", response)

    if match:
        # Extract and return the matched command
        command = match.group(0).strip()
        return command
    else:
        # Fallback if no valid command is found
        return "No valid command found."


