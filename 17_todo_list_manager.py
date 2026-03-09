# ============================================================
# Program 17: To-Do List Manager
# Concepts: Lists, functions, enumerate, string formatting, loop
# ============================================================

# A simple command-line to-do list that lets users:
# - Add tasks
# - View all tasks with completion status
# - Mark tasks as done
# - Delete tasks

def display_tasks(tasks):
    """
    Display all tasks with their index and completion status.
    Uses enumerate() to get index + value at the same time.
    """
    if not tasks:
        print("\n📋 Your to-do list is empty!")
        return

    print("\n📋 Your To-Do List:")
    print("-" * 40)
    for i, (task, done) in enumerate(tasks, start=1):
        # Choose ✅ for done, ⬜ for pending
        status = "✅" if done else "⬜"
        print(f"  {i}. {status} {task}")
    print("-" * 40)

    # Count pending vs done
    done_count    = sum(1 for _, done in tasks if done)
    pending_count = len(tasks) - done_count
    print(f"  Total: {len(tasks)} | Done: {done_count} | Pending: {pending_count}")


def add_task(tasks, task_name):
    """Add a new task. Each task is stored as (name, is_done) tuple."""
    tasks.append((task_name.strip(), False))  # New tasks are not done
    print(f"✅ Task added: '{task_name}'")


def mark_done(tasks, index):
    """Mark a task as completed by its 1-based index."""
    if 1 <= index <= len(tasks):
        task_name, _ = tasks[index - 1]
        tasks[index - 1] = (task_name, True)  # Update done status
        print(f"✅ Marked as done: '{task_name}'")
    else:
        print("⚠️  Invalid task number.")


def delete_task(tasks, index):
    """Remove a task from the list by its 1-based index."""
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"🗑️  Deleted: '{removed[0]}'")
    else:
        print("⚠️  Invalid task number.")


def main():
    print("=" * 45)
    print("     ✅  To-Do List Manager  ✅")
    print("=" * 45)

    tasks = []  # List of (task_name, is_done) tuples

    while True:
        print("\n--- Menu ---")
        print("  1. Add Task")
        print("  2. View Tasks")
        print("  3. Mark Task as Done")
        print("  4. Delete Task")
        print("  5. Quit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            name = input("Enter task name: ").strip()
            if name:
                add_task(tasks, name)
            else:
                print("⚠️  Task name cannot be empty.")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            if tasks:
                try:
                    idx = int(input("Enter task number to mark done: "))
                    mark_done(tasks, idx)
                except ValueError:
                    print("⚠️  Please enter a valid number.")

        elif choice == "4":
            display_tasks(tasks)
            if tasks:
                try:
                    idx = int(input("Enter task number to delete: "))
                    delete_task(tasks, idx)
                except ValueError:
                    print("⚠️  Please enter a valid number.")

        elif choice == "5":
            print("\n👋 Goodbye! Stay productive!")
            break

        else:
            print("⚠️  Invalid choice. Select 1–5.")


if __name__ == "__main__":
    main()
