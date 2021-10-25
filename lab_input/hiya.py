import datetime

# below is a function containing our code
def main():
    week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    Day = (week_days[datetime.datetime.now().weekday()])
    # pause the program and wait for the user to provide input
    user_input = input("Please enter your name:")
    
    # display the input back to the user.
    print("Hello " + user_input +"! Happy " + Day +"!" )

main()
