from car import *
from taxi import *
from silver_service_taxi import *
MENU = "C)hoose taxi \nD)rive \nQ)uit"
def main():
    bill_cost = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
      if choice == "c":
         print("Taxis available:")
         printing_taxis(taxis)
         taxis_choice = int(input("Choose taxi: "))
         try:
              current_taxi = taxis[taxis_choice]
         except IndexError:
                print("Invalid taxi choice")
      elif choice == "d":
         if current_taxi:
            current_taxi.start_fare()
            drive_distance = float(input("Drive how far?: "))
            current_taxi.drive(drive_distance)
            cost = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
            bill_cost += cost
         else:
              print("You need to choose a taxi before you can drive")
      else:
            print("Invalid option")
            print(f"Bill to date: ${bill_cost:.2f}")
            print(MENU)
            choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill_cost:.2f}")
    print("Taxis are now: ")
    printing_taxis(taxis)
def printing_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
if __name__ == '__main__':
    main()