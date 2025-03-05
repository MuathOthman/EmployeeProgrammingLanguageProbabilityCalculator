def probability(total_employee_per_company, total_employee_per_language_in_company):
    probability = {}
    for company in total_employee_per_company:
        probability[company] = {}
        for language in total_employee_per_language_in_company[company]:
            probability[company][language] = total_employee_per_language_in_company[company][language] / total_employee_per_company[company]
    return probability
