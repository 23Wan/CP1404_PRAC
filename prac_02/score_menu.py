def get_valid_score():
    while True:
        score = float(input("Enter score (0-100): "))
        if score >= 0 and score <= 100:
            return score
        else:
            print("Invalid score, please try again.")
def calculate_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 50 and score < 90:
        return "Passable"
    elif score >= 90 and score <= 100:
        return "Excellent"
    else:
        return "Bad"
def show_stars(score):
    print("*" * int(score))
def main():
    score = get_valid_score()
    while True:
        print("\nMenu:")
        print("G)et a valid score")
        print("P)rint result")
        print("S)how stars")
        print("Q)uit")
        choice = input("\nEnter your choice: ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = calculate_score_result(score)
            print("Result:", result)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()