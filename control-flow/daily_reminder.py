# (link unavailable)

def get_task_info():
    """Prompt user for task information"""
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound

def process_task(task, priority, time_bound):
    """Process the task based on priority and time sensitivity"""
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an unknown priority"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    return reminder

def main():
    task, priority, time_bound = get_task_info()
    reminder = process_task(task, priority, time_bound)
    print("Reminder:", reminder)

if __name__ == "__main__":
    main()

