#showing a calender in python with ***Kelly***

#import calender built-in python libraries
import calendar
import dateime

#set the calendar to begin on a sunday
calendar.setfirstweekday(calendar.Sunday)

#shows the current year and month
print("----Python Calender---\n")
print(calendar.month(2020,4),"\n")

#checks the current date in other system
current=datetime.datetime.now()

#this will indicate the current year,month, and give the day of the week
day_index=calendar.weekday(2020,2,7)
month_index=calendar.month(2020,4)

#display full calendar

# %A is a full day
# %B is the full month name month
# %d is the day of the month
# &Y is the full year
print ("Today is", current.strftime('%A %B %d %Y'))
