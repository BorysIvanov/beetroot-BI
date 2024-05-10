weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

weekdays_dict = {i + 1: day for i, day in enumerate(weekdays)}
reverse_weekdays_dict = {day: i + 1 for i, day in enumerate(weekdays)}

print(weekdays_dict, "\n", reverse_weekdays_dict)

