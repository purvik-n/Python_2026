# -----------------------------------------------------------------------------------
# Level 10: Mini Project Combined
# Concept: Putting it all together
#
# Goal: Build a "Student Grade Manager" using all concepts learned:
# Variables, Input, Casting, Conditions, Loops, Functions, Lists/Dicts, Files, Classes.
# -----------------------------------------------------------------------------------

import os # For checking if file exists

# Managing student records via a class
class StudentManager:
    def __init__(self, filename):
        self.filename = filename
        self.students = [] # List to hold student dictionaries
        self.load_data() # Load existing data on startup

    def load_data(self):
        """Reads student data from the file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    # Format in file: Name,Score
                    parts = line.strip().split(",")
                    if len(parts) == 2:
                        name = parts[0]
                        score = int(parts[1])
                        self.students.append({"name": name, "score": score})
            print(f"Loaded {len(self.students)} students from file.")
        else:
            print("No existing data found. Starting fresh.")

    def save_data(self):
        """Writes learner data to the file."""
        with open(self.filename, "w") as file:
            for student in self.students:
                file.write(f"{student['name']},{student['score']}\n")
        print("Data saved successfully.")

    def add_student(self):
        """Gets user input and adds a new student."""
        # Getting user input step
        print("\n--- Add New Student ---")
        name = input("Enter Student Name: ")
        
        try:
            score_input = input("Enter Student Score (0-100): ")
            score = int(score_input)
            
            if 0 <= score <= 100:
                # Store as a dictionary inside the list
                new_student = {"name": name, "score": score}
                self.students.append(new_student)
                print(f"Added {name} with score {score}.")
            else:
                print("Error: Score must be between 0 and 100.")

        except ValueError:
            print("Error: Please enter a valid number for the score.")

    def view_students(self):
        """Displays all students and their calculated grades."""
        print("\n--- Student Report ---")
        if not self.students:
            print("No students recorded yet.")
            return

        print(f"{'Name':<15} {'Score':<10} {'Grade':<10}")
        print("-" * 35)

        for student in self.students:
            grade = self.calculate_grade(student["score"])
            print(f"{student['name']:<15} {student['score']:<10} {grade:<10}")

    def calculate_grade(self, score):
        """Determines grade based on score (Conditions/Logic)."""
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        else: return "F"

    def run(self):
        """Main program loop."""
        while True:
            print("\n=== CLASSROOM MANAGER MENU ===")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Save & Exit")
            
            choice = input("Choose an option (1-3): ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.save_data()
                print("Goodbye!")
                break # Exit the loop
            else:
                print("Invalid choice, please try again.")

# --- Execution Starts Here ---
if __name__ == "__main__":
    # Create the manager object
    manager = StudentManager("class_data.txt")
    # Start the application
    manager.run()
