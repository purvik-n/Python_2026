# =============================================================================
# Program 7: Word Frequency Counter
# =============================================================================
# Concepts Used: String methods (.split(), .lower(), .strip()), Dictionaries,
#                for loop, Sorting, f-strings
#
# What this program does:
#   - Asks the user to enter a sentence or paragraph
#   - Splits the text into individual words
#   - Counts how many times each word appears using a dictionary
#   - Displays the word frequencies sorted from most to least common
# =============================================================================

# --- Step 1: Getting text from the user ---
print("📝 Word Frequency Counter\n")
text = input("Enter a sentence or paragraph:\n> ")

# --- Step 2: Cleaning and splitting the text ---
# .lower() converts everything to lowercase so "Hello" and "hello" count as same
# .split() breaks the string into a LIST of words (splits on spaces by default)
words = text.lower().split()

# Let's see what split() produced
print(f"\n🔍 Total words found: {len(words)}")
print(f"   Words list: {words}")

# --- Step 3: Counting word frequencies using a dictionary ---
# A dictionary stores KEY:VALUE pairs. Here, KEY = word, VALUE = count.
# We start with an empty dictionary {}.
word_count = {}

for word in words:
    # .strip(".,!?;:'\"") removes common punctuation from both ends of the word
    # This way "hello!" and "hello" are treated as the same word
    clean_word = word.strip(".,!?;:'\"")

    # Check if the word is already in our dictionary
    if clean_word in word_count:
        # If YES, increase its count by 1
        word_count[clean_word] += 1
    else:
        # If NO, add it to the dictionary with a count of 1
        word_count[clean_word] = 1

# --- Step 4: Displaying the results ---
print(f"\n{'=' * 40}")
print(f"📊 WORD FREQUENCIES:")
print(f"{'=' * 40}")
print(f"  {'Word':<20} {'Count':<10}")
print(f"  {'-' * 30}")

# sorted() with key parameter sorts dictionary items by value (count)
# reverse=True sorts from highest to lowest
# .items() returns a list of (key, value) pairs from the dictionary
sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

for word, count in sorted_words:
    # Create a simple bar chart using "█" characters
    bar = "█" * count
    print(f"  {word:<20} {count:<5} {bar}")

# --- Step 5: Finding the most common word ---
if sorted_words:
    most_common = sorted_words[0]  # First item after sorting = most common
    print(f"\n🏆 Most common word: '{most_common[0]}' (appeared {most_common[1]} times)")

print(f"\n📖 Unique words: {len(word_count)}")

# --- What we learned ---
# 1. String methods: .lower() for case, .split() to break into words, .strip() for cleanup
# 2. Dictionaries: store key-value pairs, perfect for counting occurrences
# 3. 'in' keyword: checks if a key exists in a dictionary
# 4. sorted() with key parameter: sorts based on a custom criteria
# 5. lambda: a mini anonymous function used for sorting
# 6. .items(): returns all key-value pairs from a dictionary
