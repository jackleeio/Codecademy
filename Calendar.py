"""
This program did the function of Calendar Application

Author: Jack Lee
"""
from time import sleep, strftime

USER_FIRST_NAME = raw_input("Enter your first name: ")
calendar = {}
def welcome():
  print("Welcome, " + USER_FIRST_NAME + ".")
  print("Calendar starting...")
  sleep(1)
  print("Today is: " + strftime("%A %B %d, %Y"))
  print("Current time is: " + strftime("%H:%M:%S"))
  sleep(1)
  print("What would you like to do ?")
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print("Calendar Empty.")
      else:
        print(calendar)
    elif user_choice == "U":
      date = raw_input("What date?(MM/DD/YYYY) ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print("Updating successful!")
      print(calendar )
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date(MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print("The date you entered is invalid.")
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue # start the loop from the beginning again
        else:
          start = False
          print("Exit...")
          sleep(1)
      else:
        calendar[date] = event
        print("Added successful!")
        print(calendar)
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print("You calendar is empty!")
      else:
        event = raw_input("What event?")
        for date in calendar.keys():
          if calendar[date] == event:
            del calendar[date]
            print("Delete successfully!")
            print(calendar)
          else:
            print("The event you specified is incorrect.")
    elif user_choice == "X":
      start = False
      print("Exiting...")
      sleep(1)
    else:
      print("Your command is invalid.")
      start = Flase
          
start_calendar()
            


























    
  
  
