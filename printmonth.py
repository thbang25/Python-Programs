month =input("Enter the month ('January', ..., 'December'): ")
day =input("Enter the start day ('Monday', ..., 'Sunday'): ")



# Get the number of days in the months
if month in ["January", "March", "May", "July", "August", "October", "December"]:
    x = 31
elif month in ["February"]:
    x = 28
else:
    x = 30

# Get the number of "blank spaces" we need to skip for the first week, and when to break
DAY_OFF = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
off = DAY_OFF.index(day)

print(month)
print("Mo Tu We Th Fr Sa Su")
# Print empty "cells" when the first day starts after Monday
for i in range(off):
    print("  ", end=' ')
# Print days of the month
for i in range(x):
    print("%2d" % (i+1), end=' ')
    # If we just printed the last day of the week, print a newline
    if (i + off) % 7 == 6: print()