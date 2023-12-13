
class Guitar:
  def __init__(self, name, year, cost):
    self.name = name
    self.year = year
    self.cost = cost
  def __lt__(self, other):

    return self.year < other.year
import csv

guitars = []

with open('guitars.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    guitar = Guitar(row[0], row[1], row[2])
    guitars.append(guitar)

for guitar in guitars:
  print(f'{guitar.name} ({guitar.year}): $ {guitar.cost}')

guitars.sort()

print("\nSorted by year:")
for guitar in guitars:
  print(f'{guitar.name} ({guitar.year}): $ {guitar.cost}')

new_guitars = []
while True:
  name = input("Enter the name of the guitar (or press enter to stop): ")
  if name == "":
    break

  year = input("Enter the year of the guitar: ")
  cost = input("Enter the cost of the guitar: ")
  guitar = Guitar(name, year, cost)
  new_guitars.append(guitar)

guitars.extend(new_guitars)

with open('guitars.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  for guitar in guitars:
    writer.writerow([guitar.name, guitar.year, guitar.cost])


























