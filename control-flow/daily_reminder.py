task_variable = str(input("Enter a task description: "))
task_priority = str(input("Enter priority (high/ medium/low): " ))
time_bound = str(input("Is it time bound ? (yes/no): "))

match task_priority:
    case "high":
        print(f"{task_variable} is a high priority task that requires immediate attention today! ")
    case "medium":
        print(f"{task_variable} is a medium priority task that doesn't require immediate attention today! ")
    case "low":
        print(f"{task_variable} is a low priority task. consider completing it5 when you have free time. ")
    case _:
        print(f"Invalid priority task")

if time_bound == "yes":
    print("Reminder: The task is time bound, fix ASAP. ")
else:
    print("Note: The task is not time bound, take your time. ")
