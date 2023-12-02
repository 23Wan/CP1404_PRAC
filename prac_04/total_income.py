"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    numOfMonths = int(input("How many months? "))
    print('')
    for month in range(1, numOfMonths + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    display_Report(numOfMonths, incomes)
def display_Report(monthsCount, incomesList):
    """This function will print the report in tabular format"""
    print("\nIncome Report\n-------------")
    total = 0

    for month in range(1, monthsCount + 1):
        income = incomesList[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()