task = input("Enter a task description: ")
priority = input("Enter priority (high/medium/low): ").lower()
time_bound = input("Is it time bound ? (yes/no): ").lower()

match priority:
    case "high":
        level = "high"

    case "medium":
        level = "medium"

    case "low":
        level = "low"

    case _:
        level = "Invalid priority task"

if time_bound == "yes":
    print(f"Reminder: {task} is a {level} priority task that requires immediate attention today! ")
else:
    print(f"Note: {task} is a {level} priority task. Consider completing it when you have free time. ")
