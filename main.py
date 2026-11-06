def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total):
    return total / 5


def calculate_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 55:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def calculate_result(percentage):
    if percentage >= 40:
        
        return "Pass"
    else:
        return "Fail"


def main():
    while True:
        name = input("\nEnter student name:  ")
        marks = []

        for i in range(5):
            while True:
                try:
                    mark = int(input(f"Enter marks for subject {i+1}: "))

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Invalid marks. Enter a number between 0 and 100.")

                except ValueError:
                    print("Invalid marks. Enter a number between 0 and 100.")

        total = calculate_total(marks)
        percentage = calculate_percentage(total)
        grade = calculate_grade(percentage)
        result = calculate_result(percentage)

        print("\n----- Student Result -----")
        print(f"{name} | Total: {total} | Percentage: {percentage:.2f}% | Grade: {grade} | Result: {result}")

        another = input("\nAnother student? (y/n): ")

        if another.lower() != 'y':
            print("Thank you!")
            break


if __name__ == "__main__":
    main()
