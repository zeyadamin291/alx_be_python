from datetime import datetime , timedelta

def display_current_datetime ():
    """Displays the current date and time in a human-readable format."""
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date():
    current_date = datetime.now()
    number_of_days =int( input("please enter the number of days: "))
    future_date = current_date +timedelta(days= number_of_days)
    print("Future date: ",future_date.strftime("%Y-%m-%d"))



display_current_datetime()
calculate_future_date()