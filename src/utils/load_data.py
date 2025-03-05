import json

def load_data(filename):
    try:
        with open(filename) as f:
            data = json.load(f)
            print("Data loaded successfully")
    except Exception as e:
        print(f"Error: {e}")
    return data
