companies = set()
languages = set()

def identify(data):
    for person in data:
        for company in person['companies']:
            companies.add(company)
        for language in person['skills']:
            languages.add(language)
    print(companies)
    print(languages)
    return companies, languages
