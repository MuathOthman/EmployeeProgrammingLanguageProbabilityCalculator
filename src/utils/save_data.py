import json

def save_data(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
            print("Data saved successfully")
    except Exception as e:
        print(f"Error: {e}")
    return None