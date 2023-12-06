
import csv
def read_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        for line in reader:
            data.append(line)
    return data

def process_data(data):
    winners = {}
    countries = set()
    for row in data[1:]:
        name = row[4]
        country = row[1]
        if name in winners:
            winners[name] += 1
        else:
            winners[name] = 1
        countries.add(country)
    return winners, countries
def print_winners(winners):
    print("Wimbledon Champions:")
    for name, wins in winners.items():
        print("{} {}".format(name, wins))
def print_countries(countries):
    countries_list = list(countries)
    countries_list.sort()
    countries_string = ", ".join(countries_list)
    print("These {} countries have won Wimbledon: {}".format(len(countries_list), countries_string))
def main():
    filename = "wimbledon.csv"
    data = read_data(filename)
    winners, countries = process_data(data)
    print_winners(winners)
    print_countries(countries)
if __name__ == "__main__":
    main()