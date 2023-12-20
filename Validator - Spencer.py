from datetime import datetime

from dateutil import parser
# Gets todays date
today = datetime.today()
# Puts it into the dd/mm/yyyy format
today = today.strftime("%d/%m/%Y")


def DateValidation(eventDate):
    
    # Makes sure any invalid dates are inputted
    while True:
        try:
            print(bool(parser.parse(eventDate)))
            return True
        # Doesnt work if invalid
        except ValueError:
            print("Invalid Date")
            return False

    while True:
        # Checks if date is before or after today
        # If its after or is today, it allows the user to store the date
        # If before today, it wont store it since it has already happened.
            if eventDate > today:
                print("Invalid date. Event has already happened")
                return False
            elif eventDate < today:
                print("Event will happen soon.")
                break
            else:
                print("The event is today")
                break

