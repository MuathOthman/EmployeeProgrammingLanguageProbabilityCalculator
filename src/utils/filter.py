def filter(data):
    return [person for person in data if len(person['companies']) >= 3]