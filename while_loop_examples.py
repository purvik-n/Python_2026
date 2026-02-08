def example_basic_counting():
    print("--- Example 1: Basic Counting ---")
    count = 1
    while count <= 5:
        print(f"Count is: {count}")
        count += 1

def example_break_statement():
    print("\n--- Example 2: Break Statement ---")
    num = 0
    while True:
        print(f"Current number: {num}")
        num += 1
        if num >= 3:
            print("Breaking the loop now!")
            break

def example_continue_statement():
    print("\n--- Example 3: Continue Statement ---")
    i = 0
    while i < 5:
        i += 1
        if i == 3:
            print("Skipping 3 using continue")
            continue
        print(f"Value: {i}")

def example_while_else():
    print("\n--- Example 4: While-Else ---")
    n = 0
    while n < 3:
        print(f"Inside loop: {n}")
        n += 1
    else:
        print("Loop finished normally (else block executed)")

def example_input_validation():
    print("\n--- Example 5: User Input Validation ---")
    password = ""
    while password != "secret":
        password = input("Enter the password (hint: secret): ")
        if password == "secret":
            print("Access Granted!")
        else:
            print("Wrong password, try again.")

def main():
    example_basic_counting()
    example_break_statement()
    example_continue_statement()
    example_while_else()
    example_input_validation()

if __name__ == "__main__":
    main()
