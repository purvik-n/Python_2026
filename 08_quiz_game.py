# =============================================================================
# Program 8: Python Quiz Game
# =============================================================================
# Concepts Used: Lists of Dictionaries, for loop with enumerate, Conditionals,
#                Score tracking with variables, String comparison (.lower())
#
# What this program does:
#   - Stores quiz questions in a list of dictionaries
#   - Each dictionary contains: question, options, and correct answer
#   - Loops through questions, takes user answers, and checks correctness
#   - Keeps score and shows a final grade with feedback
# =============================================================================

# --- Step 1: Defining the quiz data ---
# We use a LIST of DICTIONARIES. Each dictionary represents one question.
# This is a powerful way to organize structured data in Python.
quiz_questions = [
    
        "question": "What is the output of print(type(10))?",
        "options": ["A. str", "B. int", "C. float", "D. number"],
        "answer": "b"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. func", "C. def", "D. define"],
        "answer": "c"
    },
    {
        "question": "What does len([1, 2, 3]) return?",
        "options": ["A. 2", "B. 3", "C. 4", "D. Error"],
        "answer": "b"
    },
    {
        "question": "Which method adds an item to the END of a list?",
        "options": ["A. .add()", "B. .insert()", "C. .push()", "D. .append()"],
        "answer": "d"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /* */", "D. --"],
        "answer": "b"
    },
]

# --- Step 2: Setting up the game ---
score = 0  # Variable to track correct answers
total_questions = len(quiz_questions)  # Total number of questions

print("🐍 PYTHON QUIZ GAME 🐍")
print("=" * 40)
print(f"Answer {total_questions} questions to test your Python knowledge!")
print("Type the letter (A, B, C, or D) for your answer.\n")

# --- Step 3: Looping through each question ---
# enumerate() gives us both the INDEX (i) and the VALUE (q) for each item.
# start=1 makes the numbering begin from 1 instead of 0.
for i, q in enumerate(quiz_questions, start=1):
    # Display the question number and the question text
    print(f"Question {i}/{total_questions}: {q['question']}")

    # Display all the options for this question
    for option in q["options"]:
        print(f"  {option}")

    # Get the user's answer
    user_answer = input("\nYour answer: ").lower().strip()

    # --- Step 4: Checking the answer ---
    # Compare user's answer with the correct answer (both lowercase)
    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1  # Increase score by 1
    else:
        # Show the correct answer if they got it wrong
        correct_letter = q["answer"].upper()
        print(f"❌ Wrong! The correct answer was: {correct_letter}\n")

# --- Step 5: Displaying the final score ---
percentage = (score / total_questions) * 100  # Calculate percentage

print("=" * 40)
print(f"🏆 QUIZ COMPLETE!")
print(f"   Score: {score}/{total_questions} ({percentage:.0f}%)")

# Give feedback based on the score using if/elif/else
if percentage == 100:
    print("   🌟 PERFECT! You're a Python master!")
elif percentage >= 80:
    print("   🎉 Excellent! Great Python knowledge!")
elif percentage >= 60:
    print("   👍 Good job! Keep learning!")
elif percentage >= 40:
    print("   📚 Not bad! Review the basics.")
else:
    print("   💪 Keep practicing! You'll get better!")
print("=" * 40)

# --- What we learned ---
# 1. List of Dictionaries: organize related data (question + options + answer)
# 2. Accessing dictionary values: q["question"], q["options"], q["answer"]
# 3. enumerate(list, start=1): get index + value while looping
# 4. Score tracking: initialize to 0, increment with += 1
# 5. Percentage calculation: (part / total) * 100
# 6. Multiple conditions: if/elif/else chain for grading
