# Program to display calendar of the given month and year

# importing calendar module
import calendar

yy = 2024  # year
mm = 8   # month


yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# Display the Calendar
print(calendar.month(yy, mm ))