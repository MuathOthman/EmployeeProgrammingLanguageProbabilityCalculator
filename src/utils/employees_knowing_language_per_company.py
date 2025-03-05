def employees_knowing_language_per_company(data):
    workers = {}
    for person in data:
        for company in person['companies']:
            for language in person['skills']:
                if company in workers:
                    if language in workers[company]:
                        workers[company][language] += 1
                    else:
                        workers[company][language] = 1
                else:
                    workers[company] = {language: 1}
    print(workers)
    return workers