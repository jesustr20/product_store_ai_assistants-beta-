import os

def load_prompt(filename: str) -> str:
        base_path = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_path, filename)        
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"the file {filepath} does not exist in 'prompts'.")        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read().strip()
        if not content:
            raise ValueError(f"the file {filename} is empty.")        
        return content