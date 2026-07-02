def load_prompt_template():
    with open("prompts/transform_prompt.txt", "r") as f:
        return f.read()