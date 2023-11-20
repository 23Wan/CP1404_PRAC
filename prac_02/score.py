def calculate_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 50 and score < 90:
        return "Passable"
    elif score >= 90 and score <= 100:
        return "Excellent"
    else:
        return "Bad"
def main():
    score = float(input("Enter score: "))
    result = calculate_score_result(score)
    print(result)
if __name__ == "__main__":
    main()