# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Determine reminder based on priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an undefined priority"

# Modify message if task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ["high", "medium", "low"]:
        message = f"Note: {message}. Consider completing it when you have free time."

# Print the final reminder
print("Reminder:" if time_bound == "yes" else "", message)
