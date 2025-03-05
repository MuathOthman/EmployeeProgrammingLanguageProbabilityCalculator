from utils.save_data import save_data
from utils.load_data import load_data
from utils.filter import filter
from utils.identification import identify
from utils.total_employees_per_company import total_employees_per_company
from utils.employees_knowing_language_per_company import employees_knowing_language_per_company
from utils.probability import probability
from colorama import Fore, Back, Style, init

init()


def main():
    # Step 1: Load data from JSON file
    print(Fore.GREEN + 'Loading data from JSON file...' + Fore.RESET)
    data = load_data('json/data.json')

    # Step 2: Identify companies and languages
    print(Fore.GREEN + 'Identifying companies and languages...' + Fore.RESET)
    companies, languages = identify(data)

    # Step 3: Filter data
    print(Fore.GREEN + 'Filtering data...' + Fore.RESET)
    filtered_data = filter(data)

    # Step 4: Save filtered data to JSON file
    print(Fore.GREEN + 'Saving filtered data to JSON file...' + Fore.RESET)
    save_data(filtered_data, 'json/filtered_data.json')

    # Step 5: Print total employees per company
    print(Fore.GREEN + 'Calculating total employees per company...' + Fore.RESET)
    employees_per_company = total_employees_per_company(filtered_data)

    # Step 6: Print total employees per language in company
    print(Fore.GREEN + 'Calculating total employees per language in company...' + Fore.RESET)
    employees_per_language_in_company = employees_knowing_language_per_company(filtered_data)

    # Step 7: Probability calculation
    print(Fore.GREEN + 'Calculating probability...' + Fore.RESET)
    probability_data = probability(employees_per_company, employees_per_language_in_company)

    # Step 8: Print probability data
    print(Fore.GREEN + 'Printing probability data...' + Fore.RESET)
    for company in probability_data:
        for language in probability_data[company]:
            print(f'P({language}|{company}) = {probability_data[company][language]}')

    # Step 9: Save probability data to JSON file
    print(Fore.GREEN + 'Saving probability data to JSON file...' + Fore.RESET)
    save_data(probability_data, 'json/probability_data.json')






if __name__ == "__main__":
    main()
