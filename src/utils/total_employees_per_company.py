def total_employees_per_company(data):
    workers = {}
    for person in data:
        for company in person['companies']:
            if company in workers:
                workers[company] += 1
            else:
                workers[company] = 1
    print(workers)
    return workers