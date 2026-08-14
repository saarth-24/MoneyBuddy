import os
import json

def validateinput(data: dict):
    requiredkeys = ["salary", "expense", "debt"]
    return all(key in data and isinstance(data[key], (int, float)) for key in requiredkeys)

def loadknowledgebase(filepath:str=None):
    if filepath is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "knowledge_base.json")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Knowledge base file not found at {file_path}")
    with open(file_path, 'r') as file:
        knowledge_base = json.load(file)
    return knowledge_base
