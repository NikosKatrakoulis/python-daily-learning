# Create a list containing a series of reminder messages.
# Pass the list to a function called show_reminders(),
# which prints each reminder message.

def show_reminders(reminders):
    """Print all reminders in the list."""
    for reminder in reminders:
        print(reminder)


reminders = ["Haircut Appointment Sunday at 14:00",
             "Dentist Appointment Friday at 17:30"]
show_reminders(reminders)
