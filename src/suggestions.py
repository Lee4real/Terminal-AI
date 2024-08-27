import re
from gemini_api import generate_text

def suggest_commands(command_part, max_suggestions=5):
    command_part_with_prompt = f"""
    You are an expert in writing Linux/macOS commands. I will give you an incomplete command, 
    and your task is to suggest a list of possible completed commands. Only return the commands 
    themselves, separated by newlines, without any additional words, details, explanations, or formatting.

    For example, if I give you 'git ch', you should return a list like:
    git checkout
    git cherry-pick
    git chmod

    Here is the incomplete command: {command_part}
    """
    
    # Call the Gemini API to get suggestions
    try:
        response = generate_text(command_part_with_prompt)
    except Exception as e:
        return f"Error: {str(e)}"
    
    
    # Use regex to extract individual command suggestions
    # Assuming each command is on a new line
    command_suggestions = re.findall(r"^[a-zA-Z]+\s+[\S]+", response, re.MULTILINE)
    
    # Filter suggestions to start with the command_part
    filtered_suggestions = [cmd for cmd in command_suggestions if cmd.startswith(command_part)]
    
    # Limit the number of suggestions
    limited_suggestions = filtered_suggestions[:max_suggestions]
    
    if limited_suggestions:
        # Return the list of commands
        return limited_suggestions
    else:
        # Fallback if no valid suggestions are found
        return ["No valid suggestions found."]


