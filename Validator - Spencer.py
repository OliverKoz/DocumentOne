
from datetime import datetime
# Module checks if date is valid
from dateutil import parser
# Gets todays date
today = datetime.today()
# Puts it into the dd/mm/yyyy format
today = today.strftime("%d/%m/%Y")


def DateValidation(eventDate):
# eventDate: str -> the user inputs when the event takes place
    # Makes sure any invalid dates are inputted e.g.(30/02/2024)
    while True:
        try:
            validDate = (bool(parser.parse(eventDate)))           
            if validDate == True:
                break
            else:
                continue
                
        # Doesnt work if invalid
        # Returns to the beginning of the function
        except ValueError:
            return("Invalid Date")
            
                
            
    while eventDate < today:
    # Checks if date is before or after today
    # If its after or is today, it allows the user to store the date
    # If before today, it wont store it since it has already happened. 

        if eventDate < today:
            return("Event will happen soon.")        
            
        elif eventDate == today:
            return("The event is today.")
            
        else:
            return("Event has already happened.")
            

            


