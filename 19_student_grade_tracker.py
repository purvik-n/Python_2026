# ============================================================
# Program 19: Student Grade Tracker
# Concepts: Dictionaries, lists, functions, statistics, sorting
# ============================================================

# This program lets a teacher:
# - Add students and their subject marks
# - Calculate average, highest, lowest scores
# - Assign letter grades (A, B, C, D, F)
# - Display a sorted leadrboard

def assign_grade(average):
    """
    Return a letter grade based on percentage average.
    Grading scale: A=90+, B=80+, C=70+, D=60+, F=below 60
    """
    if average >= 90:
        return "A 🌟"
    elif average >= 80:
        return "B 👍"
    elif average >= 70:
        return "C 😊"
    elif average >= 60:
        return "D ⚠️"
    else:
        return "F ❌"


def add_student(students):
    """Add a new student with their marks for multiple subjects."""
    name = input("  Student name: ").strip().title()

    if not name:
        print("⚠️  Name cannot be empty.")
        return

    if name in students:
        print(f"⚠️  '{name}' already exists. Use update to add marks.")
        return

    subjects = {}
    print(f"  Enter marks for {name} (type 'done' to stop):")

    while True:
        subject = input("    Subject name (or 'done'): ").strip().title()
        if subject.lower() == "done":
            break
        if not subject:
            continue
        try:
            mark = float(input(f"    Mark for {subject} (0–100): "))
            if 0 <= mark <= 100:
                subjects[subject] = mark
            else:
                print("⚠️  Mark must be between 0 and 100.")
        except ValueError:
            print("⚠️  Invalid mark. Skipping.")

    if subjects:
        students[name] = subjects
        avg = sum(subjects.values()) / len(subjects)
        print(f"✅ {name} added! Average: {avg:.1f} — Grade: {assign_grade(avg)}")
    else:
        print("⚠️  No marks entered. Student not saved.")


def display_all(students):
    """Display full report for all students, sorted by average (high→low)."""
    if not students:
        print("\n📋 No students yet.")
        return

    # Build a list of (name, avg, grade) for sorting
    report = []
    for name, subjects in students.items():
        avg = sum(subjects.values()) / len(subjects)
        grade = assign_grade(avg)
        report.append((name, subjects, avg, grade))

    # Sort by average descending (highest first)
    report.sort(key=lambda x: x[2], reverse=True)

    print("\n" + "=" * 55)
    print(f"{'Rank':<6}{'Name':<20}{'Avg':<8}{'Grade':<12}{'Subjects'}")
    print("=" * 55)

    for rank, (name, subjects, avg, grade) in enumerate(report, start=1):
        subject_str = ", ".join(f"{s}:{m:.0f}" for s, m in subjects.items())
        print(f"  {rank:<4}{name:<20}{avg:<8.1f}{grade:<12}{subject_str}")

    print("=" * 55)

    # Class statistics
    all_avgs = [avg for _, _, avg, _ in report]
    print(f"\n📊 Class Stats: Highest={max(all_avgs):.1f}  Lowest={min(all_avgs):.1f}  "
          f"Class Avg={sum(all_avgs)/len(all_avgs):.1f}")


def main():
    print("=" * 50)
    print("    📚  Student Grade Tracker  📚")
    print("=" * 50)

    students = {}   # { "Student Name": {"Math": 90, "Science": 85} }

    while True:
        print("\n--- Menu ---")
        print("  1. Add Student")
        print("  2. View All Students & Grades")
        print("  3. Quit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all(students)
        elif choice == "3":
            print("\n👋 Goodbye! Keep tracking those grades!")
            break
        else:
            print("⚠️  Invalid option. Choose 1–3.")


if __name__ == "__main__":
    main()
