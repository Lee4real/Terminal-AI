from gemini_api import generate_text

def get_command_explanations(command_part):
    command_part_with_prompt = f"""
    You are an expert in writing Linux/macOS commands. I will give you a command, 
    and your task is to provide a detailed explanation of what this command does. 
    Include any options or arguments if applicable, but avoid extra formatting or explanations. 
    Return the explanation as plain text.

    Here is the command: {command_part}
    """
    
    # Call the Gemini API to get command explanations
    try:
        response = generate_text(command_part_with_prompt)
    except Exception as e:
        return f"Error: {str(e)}"
    
    
    # Return the explanation
    return response or "No explanation found."


